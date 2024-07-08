#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   endpoint.py
@Time    :   2024/07/07 22:45:16
@Desc    :
'''
from typing import List
from google.protobuf import field_mask_pb2 as _field_mask_pb2

from begonia.client.base import BaseClient
from begonia.api.endpoint.v1.endpoint_pb2_grpc import EndpointServiceStub
from begonia.api.endpoint.v1.endpoint_pb2 import EndpointSrvConfig, EndpointSrvUpdateRequest,UpdateEndpointResponse, AddEndpointResponse, EndpointMeta


class EndpointGrpcAPIClient(BaseClient):
    def __init__(self, host: str, port: int, access_key: str, secret_key: str) -> None:
        super().__init__(host, port, access_key, secret_key)
        self.endpoint_stub = EndpointServiceStub(self.client)

    def register(self, name: str, desc: str,
                 description_set: bytes,
                 endpoints: List[EndpointMeta],
                 loadbalance: str = "RR",
                 tags: List[str] = None
                 ) -> str:
        req = EndpointSrvConfig(name=name,
                                service_name=name,
                                description=desc,
                                descriptor_set=description_set,
                                tags=tags,
                                balance=loadbalance,
                                endpoints=endpoints)
        rsp, _ = self.call(req, self.endpoint_stub.Post)
        return rsp.unique_key

    def update(self, uid: str,
               name: str = None,
               desc: str = None,
               description_set: bytes = None,
               endpoints: List[EndpointMeta] = None,
               loadbalance: str = None,
               tags: List[str] = None
               ) -> str:
        mask = _field_mask_pb2.FieldMask()
        if not name is None:
            mask.paths.append("name")
            mask.paths.append("service_name")
        if not desc is None:
            mask.paths.append("description")
        if not description_set is None:
            mask.paths.append("descriptor_set")
        if not endpoints is None:
            mask.paths.append("endpoints")
        if not loadbalance is None:
            mask.paths.append("balance")
        req = EndpointSrvUpdateRequest(unique_key=uid,
                                       name=name,
                                       service_name=name,
                                       description=desc,
                                       descriptor_set=description_set,
                                       tags=tags,
                                       balance=loadbalance,
                                       endpoints=endpoints,
                                       mask=mask
                                       )
        rsp, _ = self.call(req, self.endpoint_stub.Update)
        return rsp.version


if __name__ == "__main__":
    client = EndpointGrpcAPIClient("127.0.0.1", 12139, "ofZQdEs1lS1fjqe0KB3F9WZyLxkpUFm8",
                                   "j54sXN200DmKps6dnV0OdQZdsoECYINahgI855Yi7JCf5ufOUMS39DyxE3D5KOtQ")
    with open("/data/work/begonia-org/openRAG/openrag/protos/openrag.bin", "rb") as f:
        description_set = f.read()
        endpoints = [
            EndpointMeta(addr="127.0.0.1:2027", weight=0)
        ]
        uid = client.register("openrag_endpoint", "openrag server", description_set, endpoints, loadbalance="RR")
        print(f"endpoint id is {uid}")
