#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client.py
@Time    :   2024/06/16 11:14:08
@Desc    :
'''

from curses import meta
import io
import hashlib
import math
from typing import Tuple, Union
from urllib import response
import grpc
from google.api import httpbody_pb2 as httpbody
from begonia_python_sdk.client.base import BaseClient
from begonia_python_sdk.api.file.v1.file_pb2_grpc import FileServiceStub
from begonia_python_sdk.api.file.v1.file_pb2 import DownloadRequest, \
    DownloadResponse, UploadFileRequest, FileMetadataRequest, FileMetadataResponse
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


class FileAPIGrpcClient(BaseClient):
    def __init__(self, host: str, port: int, access_key: str, secret_key: str, engine: str) -> None:
        self.host = host
        self.port = port
        self.client = grpc.insecure_channel(f'{host}:{port}')
        self.file_stub = FileServiceStub(self.client)
        self.signer = AppAuthSignerImpl(access_key, secret_key)
        self.engine = engine

    def get_host(self) -> str:
        return self.host

    def get_port(self) -> int:
        return self.port

    def get_file_stub(self) -> FileServiceStub:
        return self.file_stub

    def make_dir(self, bucket: str, folder: str) -> str:
        hash_obj = hashlib.sha256()
        hash_obj.update(b"")
        sha256 = hash_obj.hexdigest()
        request = UploadFileRequest(
            key=f"{folder}/.keep",
            content=b"",
            sha256=sha256,
            bucket=bucket,
            engine=self.engine)
        response, _ = self.call(request, self.file_stub.Upload)
        uid = response.uid
        return uid

    def get(self, fid: str, dst: str, read_request: ReadFileRequest = None) -> FileDetails:
        file = self.metadata(fid, read_request)
        if file.size > 16 * 1024 * 1024:
            return self.get_large_file(fid, dst, read_request)
        return self.get_file(fid, dst, read_request)
    
    def put_file(self, src: Union[str,bytes], bucket: str, key: str) -> str:
        data = src
        if isinstance(src, str):
            with open(src, "rb") as f:
                data = f.read()
        hash_obj = hashlib.sha256()
        hash_obj.update(data)
        sha256 = hash_obj.hexdigest()
        request = UploadFileRequest(key=key, content=data, sha256=sha256, bucket=bucket, engine=self.engine)
        response,_ = self.call(request, self.file_stub.Upload)
        return response.uri
        
    def get_file(self, fid: str, dst: str, read_request: ReadFileRequest = None) -> FileDetails:
        request = DownloadRequest(
            file_id=fid,
            key=read_request.key if read_request else None,
            version=read_request.version if read_request else None,
            bucket=read_request.bucket if read_request else None,
            engine=self.engine)

        response, server_metadata = self.call(request, self.file_stub.Download)
        metadata = {item.key: item.value for item in server_metadata}
        size = metadata.get(get_metadata_key("Content-Length"), 0)
        sha256 = metadata.get(get_metadata_key("X-File-Sha256"), '')
        version = metadata.get(get_metadata_key("X-File-Version"), '')
        bucket = metadata.get(get_metadata_key("X-File-Bucket"), '')
        name = metadata.get(get_metadata_key("X-File-Name"), '')
        content_type = response.content_type
        with open(dst, "wb") as f:
            f.write(response.data)
        return FileDetails(sha256=sha256, content_type=content_type, size=size,
                           version=version, bucket=bucket,name=name)

    def metadata(self, fid: str, read_request: ReadFileRequest = None) -> FileDetails:
        request = FileMetadataRequest(
            file_id=fid,
            engine=self.engine,
            key=read_request.key if read_request else None,
            version=read_request.version if read_request else None,
            bucket=read_request.bucket if read_request else None,
        )
        response: FileMetadataResponse = None
        response, _ = self.call(request, self.file_stub.Metadata)

        return FileDetails(sha256=response.version, content_type=response.content_type, size=response.size,
                           version=response.version, bucket=response.bucket,name=response.name)

    def range_download(self, start: int, end: int, fid: str, read_request: ReadFileRequest = None) -> bytes:
        request = DownloadRequest(
            file_id=fid,
            key=read_request.key if read_request else None,
            version=read_request.version if read_request else None,
            bucket=read_request.bucket if read_request else None,
            engine=self.engine,
        )
        metadata = (("Range", f"bytes={start}-{end}"))
        response, _ = self.call(request, self.file_stub.Download, metadata)
        return response.data

    def get_large_file(self, fid: str, dst: str, read_request: ReadFileRequest = None) -> FileDetails:
        file = self.metadata(fid, read_request)
        size = file.size
        part_size = 4 * 1024 * 1024
        part_num = math.ceil(size / part_size)
        with open(dst, "wb") as f:
            for i in range(part_num):
                start = i * part_size
                end = min((i + 1) * part_size - 1, size - 1)
                data = self.range_download(start, end, fid, read_request)
                f.write(data)
        return FileDetails(
            sha256=file.sha256,
            content_type=file.content_type,
            size=size,
            bucket=file.bucket,
            version=file.version,
            name=file.name
            )
        # response, server_metadata = self.call(request, self.file_stub.Download)
        # return response.data


if __name__ == "__main__":
    client = FileAPIGrpcClient("127.0.0.1", 12139, "RXS5ncjYwkJKEKKoTjdEagvp1iIIL4mD",
                               "zdlWogPdYGp40ilDBoqoiUkqxeO89etGTbvKPsndsD3ddkhjHlpkkJUj1JprHIpO", FILE_ENGINE_MINIO)
    # file, data = client.get_file("458092175117258752", FILE_ENGINE_MINIO)
    file = client.get("458092175117258752", "example.pdf")
    print(file)
    uri=client.put_file("example.pdf", "openkb", "example.pdf")
    print(f"uri:{uri}")
