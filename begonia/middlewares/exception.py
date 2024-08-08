#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   exception.py
@Time    :   2024/07/15 11:33:20
@Desc    :
'''

import inspect
import traceback
from typing import Callable, Tuple, Iterable
import grpc
from grpc_status import rpc_status

from google.rpc import status_pb2, code_pb2

from google.protobuf import any_pb2
from begonia.api.v1 import web_pb2
from begonia.utils.logger import logger, BegoniaLogger


def _unary_unary_rpc_terminator(code, details):

    def terminate(ignored_request, context: grpc.ServicerContext):
        context.abort(code, details)

    return grpc.unary_unary_rpc_method_handler(terminate)


def get_rsp_code(rpc_code: int) -> int:
    if rpc_code == code_pb2.OK:
        return int(web_pb2.Code.OK)
    elif rpc_code == code_pb2.CANCELLED:
        return grpc.StatusCode.CANCELLED.value[0]
    elif rpc_code == code_pb2.UNKNOWN:
        return int(web_pb2.Code.UNKNOWN)
    elif rpc_code == code_pb2.INVALID_ARGUMENT:
        return int(web_pb2.PARAMS_ERROR)
    elif rpc_code == code_pb2.DEADLINE_EXCEEDED:
        return grpc.StatusCode.DEADLINE_EXCEEDED.value[0]
    elif rpc_code == code_pb2.NOT_FOUND:
        return int(web_pb2.NOT_FOUND)
    elif rpc_code == code_pb2.ALREADY_EXISTS:
        return int(web_pb2.CONFLICT)
    elif rpc_code == code_pb2.PERMISSION_DENIED:
        return int(web_pb2.AUTH_ERROR)
    elif rpc_code == code_pb2.RESOURCE_EXHAUSTED:
        return grpc.StatusCode.RESOURCE_EXHAUSTED.value[0]
    elif rpc_code == code_pb2.FAILED_PRECONDITION:
        return grpc.StatusCode.FAILED_PRECONDITION.value[0]
    elif rpc_code == code_pb2.ABORTED:
        return grpc.StatusCode.ABORTED.value[0]
    elif rpc_code == code_pb2.OUT_OF_RANGE:
        return grpc.StatusCode.OUT_OF_RANGE.value[0]
    elif rpc_code == code_pb2.UNIMPLEMENTED:
        return int(web_pb2.NOT_FOUND)
    elif rpc_code == code_pb2.INTERNAL:
        return int(web_pb2.INTERNAL_ERROR)
    elif rpc_code == code_pb2.UNAVAILABLE:
        return grpc.StatusCode.UNAVAILABLE.value[0]
    elif rpc_code == code_pb2.DATA_LOSS:
        return grpc.StatusCode.DATA_LOSS.value[0]
    else:
        return grpc.StatusCode.UNKNOWN.value[0]


class ExceptionInterceptor:
    def __init__(self, resolver: Callable = None) -> None:
        super().__init__()
        self.resolver: Callable = resolver
        self.log = BegoniaLogger(logger)

    def exception(self, func):
        log = self.log
        resolver = self.resolver

        def wrapper(self, req, ctx: grpc.ServicerContext):
            try:
                ret = func(self, req, ctx)
                return ret
            except Exception as e:
                metadata = dict(ctx.invocation_metadata())
                metadata["method"] = ctx._rpc_event.call_details.method
                log.opt(depth=1).error(traceback.format_exc(), metadata)
                # 在这里可以进行日志记录等操作
                tb = traceback.extract_tb(e.__traceback__)
                filename, line, fn, text = tb[-1]  # 获取最后一条堆栈信息
                stack = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                # 转换异常为 gRPC 的状态码和详情
                code = grpc.StatusCode.INTERNAL.value[0]
                msg = "Internal server error"
                client_msg = ""

                if resolver:
                    code, msg, client_msg = resolver(e)
                details: web_pb2.Errors = web_pb2.Errors(
                    code=get_rsp_code(code),
                    message=msg,
                    to_client_message=client_msg,
                    stack=stack,
                    file=filename,
                    line=line,
                    fn=str(fn))
                d = any_pb2.Any()
                d.Pack(details)
                status = status_pb2.Status(code=code, message=msg, details=[d])
                ctx.abort_with_status(rpc_status.to_status(status))

        return wrapper
