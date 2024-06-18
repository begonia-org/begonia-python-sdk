#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client.py
@Time    :   2024/06/16 11:14:08
@Desc    :
'''

import io
from typing import Tuple
import grpc
from google.api import httpbody_pb2 as httpbody

from begonia_python_sdk.api.file.v1.file_pb2_grpc import FileServiceStub
from begonia_python_sdk.api.file.v1.file_pb2 import DownloadRequest, DownloadResponse
from begonia_python_sdk.api.file.v1.file_pb2 import FileEngine
from begonia_python_sdk.client.models import FileDetails, ReadFileRequest
from begonia_python_sdk.client.sign import AppAuthSignerImpl, new_gateway_request_from_grpc, GatewayRequest
# const (
# 	MetadataKeyPrefix = "x-begonia"
# )

# func GetMetadataKey(key string) string {
# 	return MetadataKeyPrefix + "-" + strings.ToLower(key)
# }
METADATA_KEY_PREFIX = "x-begonia"
FILE_ENGINE_MINIO = "FILE_ENGINE_MINIO"


def get_metadata_key(key: str) -> str:
    return METADATA_KEY_PREFIX + "-" + key.lower()


class FileAPIGrpcClient:
    def __init__(self, host: str, port: int, access_key: str, secret_key: str) -> None:
        self.host = host
        self.port = port
        self.client = grpc.insecure_channel(f'{host}:{port}')
        self.file_stub = FileServiceStub(self.client)
        self.signer = AppAuthSignerImpl(access_key, secret_key)

    def get_host(self) -> str:
        return self.host

    def get_port(self) -> int:
        return self.port

    def get_file_stub(self) -> FileServiceStub:
        return self.file_stub

    def get_file(self, fid: str, read_request: ReadFileRequest = None) -> Tuple[FileDetails, io.BytesIO]:
        request = DownloadRequest(
            file_id=fid,
            key=read_request.key if ReadFileRequest else None,
            version=read_request.version if ReadFileRequest else None,
            bucket=read_request.bucket if ReadFileRequest else None,
            engine=read_request.engine if ReadFileRequest else None)
        req = new_gateway_request_from_grpc(request, self.file_stub.Download._method.decode("utf-8"), self.host)
        md: GatewayRequest = self.signer.sign_request(req)
        client_metadata = [(k, v) for k, v in md.headers.headers.items()]
        response, call = self.file_stub.Download.with_call(request, metadata=client_metadata)
        data = response.data
        server_metadata = call.initial_metadata()
        metadata = {item.key: item.value for item in server_metadata}
        # print(f"metadata:{metadata}")
        size = metadata.get(get_metadata_key("Content-Length"), 0)
        sha256 = metadata.get(get_metadata_key("X-File-Sha256"), '')
        version = metadata.get(get_metadata_key("X-File-Version"), '')
        bucket = metadata.get(get_metadata_key("X-File-Bucket"), '')
        content_type = response.content_type
        return FileDetails(sha256=sha256, content_type=content_type, size=size,
                           version="", bucket=bucket), io.BytesIO(data)
        # return io.BytesIO(response.)


if __name__ == "__main__":
    client = FileAPIGrpcClient("127.0.0.1", 12139, "RXS5ncjYwkJKEKKoTjdEagvp1iIIL4mD",
                               "zdlWogPdYGp40ilDBoqoiUkqxeO89etGTbvKPsndsD3ddkhjHlpkkJUj1JprHIpO")
    file, data = client.get_file(None, ReadFileRequest(engine=FILE_ENGINE_MINIO,
                                 bucket="openkb", key="0500_石羊农科SRM_采购策略管理_操作手册_V1.0.pdf", version=""))
    print(file)
