#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   exception.py
@Time    :   2024/07/15 11:33:20
@Desc    :
'''


import traceback
from typing import Callable, Tuple
import grpc

from begonia.api.v1 import web_pb2
from begonia.utils.logger import logger, BegoniaLogger


def _unary_unary_rpc_terminator(code, details):

    def terminate(ignored_request, context: grpc.ServicerContext):
        context.abort(code, details)

    return grpc.unary_unary_rpc_method_handler(terminate)


class ExceptionInterceptor(grpc.ServerInterceptor):
    def __init__(self, resolver: Callable = None) -> None:
        super().__init__()
        self.resolver: Callable = resolver
        self.log = BegoniaLogger(logger)

    def intercept_service(self, continuation, handler_call_details: grpc.HandlerCallDetails):
        try:
            return continuation(handler_call_details)
        except Exception as e:
            metadata = dict(handler_call_details.invocation_metadata)
            metadata["method"] = handler_call_details.method
            self.log.error(metadata, str(e))
            # 在这里可以进行日志记录等操作
            # print(f"Exception caught in interceptor: {e}")
            tb = traceback.extract_tb(e.__traceback__)
            filename, line, func, text = tb[-1]  # 获取最后一条堆栈信息
            stack = "".join(traceback.format_exception(type(e), e, e.__traceback__))
            # 转换异常为 gRPC 的状态码和详情
            # context: grpc.ServicerContext = handler_call_details.invocation_metadata
            code = grpc.StatusCode.INTERNAL
            msg = "Internal server error"
            if self.resolver:
                code, msg, client_msg = self.resolver(e)
            details: web_pb2.Errors = web_pb2.Errors(
                code=code,
                message=msg,
                to_client_message=client_msg,
                stack=stack,
                file=filename,
                line=line,
                func=func)
            return _unary_unary_rpc_terminator(code, details)
            # context.abort(code, details)
