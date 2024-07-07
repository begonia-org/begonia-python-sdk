#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   base.py
@Time    :   2024/06/18 15:27:19
@Desc    :   
'''


from typing import Any,Callable, Tuple,Union

import grpc

from begonia.client.sign import AppAuthSignerImpl, GatewayRequest, new_gateway_request_from_grpc


class BaseClient:
    def __init__(self, host: str, port: int, access_key: str, secret_key: str) -> None:
        self.host = host
        self.port = port
        self.access_key = access_key
        self.secret_key = secret_key
        self.client = grpc.insecure_channel(f'{host}:{port}')
        self.signer = AppAuthSignerImpl(access_key, secret_key)

    def get_host(self) -> str:
        return self.host

    def get_port(self) -> int:
        return self.port

    def get_access_key(self) -> str:
        return self.access_key

    def get_secret_key(self) -> str:
        return self.secret_key
    
    def call(self,request:Any,method:grpc.UnaryUnaryMultiCallable,metadata:Tuple[Tuple[str, Any]] =None)->Tuple[Any,Tuple[Tuple[str, str]]]:
        req = new_gateway_request_from_grpc(request, method._method.decode("utf-8"), self.host,metadata=metadata)
        md: GatewayRequest = self.signer.sign_request(req)
        client_metadata = [(k, v) for k, v in md.headers.headers.items()]
        response, call = method.with_call(request, metadata=client_metadata)
        return response,call.initial_metadata()
        
        
