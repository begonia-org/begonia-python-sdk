#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2024/07/04 17:50:58
@Desc    :
'''


import grpc
from begonia_python_sdk.api.user.v1.user_pb2_grpc import UserServiceStub
from begonia_python_sdk.api.user.v1.user_pb2 import GetUserRequest, Users
from begonia_python_sdk.client.base import BaseClient
from begonia_python_sdk.client.sign import AppAuthSignerImpl


class UserAPIGrpcClient(BaseClient):
    def __init__(self, host: str, port: int, access_key: str, secret_key: str) -> None:
        super().__init__(host, port, access_key, secret_key)
        self.user_stub = UserServiceStub(self.client)

    def get_user(self, uid: str) -> Users:
        req = GetUserRequest(uid=uid)
        response, _ = self.call(req, self.user_stub.Get)
        return response


if __name__ == '__main__':
    client = UserAPIGrpcClient("127.0.0.1", 12139, "ofZQdEs1lS1fjqe0KB3F9WZyLxkpUFm8",
                               "j54sXN200DmKps6dnV0OdQZdsoECYINahgI855Yi7JCf5ufOUMS39DyxE3D5KOtQ")
    user = client.get_user("462180662716141568")
    print(f"user tenant is {user.tenant_id}")
