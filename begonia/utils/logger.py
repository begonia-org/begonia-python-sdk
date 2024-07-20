#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   logger.py
@Time    :   2024/07/15 09:46:58
@Desc    :
'''


from logging import Handler
from multiprocessing.context import BaseContext
import sys
from typing import Callable, Optional, TextIO, Union, Dict
import grpc
import grpc._server
from httpx import request
from loguru import logger
import loguru
# from openrag.config import KBConfigure
logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time}</green> <cyan>{file}</cyan>:<cyan>{line}</cyan> <level>{message}</level> <cyan>{extra[method]}</cyan> <cyan>{extra[identity]}</cyan> <cyan>{extra[request_id]}</cyan>",
)
# chat_logger = logger.bind(name="chat")
# es_logger = logger.bind(name="elasticsearch")
# rag_logger = logger.bind(name="rag")
# task_logger = logger.bind(name="task")
# document_logger = logger.bind(name="document")
# minio_logger = logger.bind(name="minio")
# nlp_logger = logger.bind(name="nlp")
# llm_logger = logger.bind(name="llm")
# kb_logger = logger.bind(name="kb")
# test_logger = logger.bind(name="test")
# rpc_logger = logger.bind(name="rpc")


def warp(func):
    def wrapper(self, message: Union[str, dict], context: Union[grpc.ServicerContext, Dict[str, str]] = None) -> None:
        # metadata = dict(ctx.invocation_metadata())
        metadata = context
        bound_logger = self.opt(depth=2)
        identity = ""
        request_id = ""
        method = ""
        if metadata:
            if isinstance(context, grpc.ServicerContext):
                metadata = dict(context.invocation_metadata())
            identity = metadata.get("x-identity", "")
            request_id = metadata.get("x-request-id", "")
            method = metadata.get("method", "")
            # method = ctx._rpc_event.call_details.method.decode("utf-8")

        bound_logger = bound_logger.bind(method=method, identity=identity, request_id=request_id)
        return func(self, bound_logger, message)
    return wrapper


class BegoniaLogger():
    def __init__(self, log) -> None:
        self.logger = log

    def with_context(self, context: Union[grpc.ServicerContext, Dict[str, str]]):
        metadata = context
        identity = ""
        request_id = ""
        method = ""
        if metadata:
            if isinstance(context, grpc.ServicerContext):
                metadata = dict(context.invocation_metadata())
            identity = metadata.get("x-identity", "")
            request_id = metadata.get("x-request-id", "")
            method = metadata.get("method", "")
            # method = ctx._rpc_event.call_details.method.decode("utf-8")
        return self.opt(method=method, identity=identity, request_id=request_id)

    @warp
    def info(self, bound_logger, message: Union[str, dict]) -> None:
        bound_logger.info(message)

    def bind(self, **kwargs):
        return self.logger.bind(**kwargs)

    @warp
    def debug(self, bound_logger, message: Union[str, dict]) -> None:
        bound_logger.debug(message)

    @warp
    def warning(self, bound_logger, message: Union[str, dict]) -> None:
        bound_logger.warning(message)

    @warp
    def error(self, bound_logger, message: Union[str, dict]) -> None:
        bound_logger.error(message)

    @warp
    def exception(self, message: Union[str, dict]) -> None:
        self.logger.exception(message)

    @warp
    def critical(self, bound_logger, message: Union[str, dict]) -> None:
        bound_logger.critical(message)

    @warp
    def success(self, bound_logger, message: Union[str, dict]) -> None:
        bound_logger.success(message)

    def opt(self, **kwargs):
        return BegoniaLogger(self.logger.opt(**kwargs))


if __name__ == "__main__":
    log = BegoniaLogger(logger)
    log.info("hello", {"x-identity": "123344", "x-request-id": "eeddfddd"})
    log.info("hello")
