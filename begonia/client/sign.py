#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sign.py
@Time    :   2024/06/16 01:30:54
@Desc    :
'''


import hashlib
import hmac
import io
import json
from datetime import datetime, UTC
import logging
from typing import Any, Dict, List, Optional, Tuple
from google.protobuf.json_format import MessageToDict

from urllib.parse import urlparse, quote, urlencode, parse_qs
from urllib.parse import ParseResult

import requests

DATE_FORMAT = "%Y%m%dT%H%M%SZ"
SIGN_ALGORITHM = "X-Sign-HMAC-SHA256"
HEADER_X_DATE = "X-Date"
HEADER_X_HOST = "host"
HEADER_X_AUTHORIZATION = "Authorization"
HEADER_X_CONTENT_SHA256 = "X-Content-Sha256"
HEADER_X_ACCESS_KEY = "X-Access-Key"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建控制台处理器并设置日志级别
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建格式器并将其添加到处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(console_handler)
class RequestHeader:
    def __init__(self) -> None:
        self.headers: Dict[str, str] = {}

    def set(self, key: str, value: str) -> None:
        self.headers[key.lower()] = value

    def get(self, key: str) -> str:
        return self.headers.get(key.lower(), '')

    def delete(self, key: str) -> None:
        self.headers.pop(key.lower(), None)

    def keys(self) -> List[str]:
        return list(self.headers.keys())


class GatewayRequest:
    def __init__(self, headers: RequestHeader, payload: io.BytesIO, method: str, url: ParseResult, host: str) -> None:
        self.headers = headers
        self.payload: io.BytesIO = payload
        self.method = method
        self.url: ParseResult = url
        self.host = host


class AppAuthSignerImpl:
    def __init__(self, key: str, secret: str) -> None:
        self.key = key
        self.secret = secret

    def hmacsha256(self, key_byte: bytes, data_str: str) -> bytes:
        return hmac.new(key_byte, data_str.encode('utf-8'), hashlib.sha256).digest()

    def canonical_request(self, request: GatewayRequest, signed_headers: List[str]) -> str:
        body_data = self.request_payload(request)
        
        hexencode = self.hex_encode_sha256_hash(body_data)

        return f"{request.method.upper()}\n{self.canonical_uri(request)}\n{self.canonical_query_string(request)}\n{self.canonical_headers(request, signed_headers)}\n{';'.join(signed_headers)}\n{hexencode}"

    def canonical_uri(self, request: GatewayRequest) -> str:
        # 分割路径为各个部分
        pattens = request.url.path.split('/')
        # 对每个部分进行转义，但保留 '/' 作为路径分隔符
        uri_slice = [quote(v, safe='') for v in pattens if v]
        # 重新组合路径
        urlpath = '/'.join(uri_slice)
        # 确保路径以 '/' 结尾
        if not urlpath.endswith('/'):
            urlpath += '/'
        # 前面部分的 / 要保留
        if request.url.path.startswith('/'):
            urlpath = '/' + urlpath
        return urlpath

    def canonical_query_string(self, request: GatewayRequest) -> str:
        query_map = parse_qs(request.url.query)
        keys = sorted(query_map.keys())
        query = []
        for key in keys:
            k = quote(key, safe='')
            values = sorted(query_map[key])
            for v in values:
                query.append(f"{k}={quote(v, safe='')}")

        query_str = '&'.join(query)
        return query_str

    def canonical_headers(self, request: GatewayRequest, signer_headers: List[str]) -> str:
        canonical_headers = []
        headers = {k.lower(): v for k, v in request.headers.headers.items()}
        for key in signer_headers:
            value = headers.get(key.lower(), '')
            if key.lower() == HEADER_X_HOST:
                value = request.host
            canonical_headers.append(f"{key}:{value.strip()}")
        return '\n'.join(canonical_headers)

    def signed_headers(self, request: GatewayRequest) -> List[str]:
        headers = request.headers.headers
        return sorted([k.lower() for k in headers.keys() if headers[k] and k.lower() != HEADER_X_AUTHORIZATION.lower()])

    def request_payload(self, request: GatewayRequest) -> io.BytesIO:
        if not request.payload:
            return io.BytesIO(b"")
        return request.payload

    def string_to_sign(self, canonical_request: str, t: datetime) -> str:
        hash_struct = hashlib.sha256()
        hash_struct.update(canonical_request.encode('utf-8'))
        return f"{SIGN_ALGORITHM}\n{t.strftime(DATE_FORMAT)}\n{hash_struct.hexdigest()}"

    def sign_string_to_sign(self, string_to_sign: str, signing_key: bytes) -> str:
        return hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

    def hex_encode_sha256_hash(self, body: io.BytesIO) -> str:
        if not body:
            body = b""
        body.seek(0)
        sha256_hash = hashlib.sha256()
        for byte_block in iter(lambda: body.read(4096), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def auth_header_value(self, signature_str: str, access_key_str: str, signed_headers: List[str]) -> str:
        return f"{SIGN_ALGORITHM} Access={access_key_str}, SignedHeaders={';'.join(signed_headers)}, Signature={signature_str}"

    def sign(self, request: GatewayRequest) -> str:
        unused_header_keys = ["content-type", "content-length", "accept-encoding"]
        for key in request.headers.keys():
            for unused_key in unused_header_keys:
                if key.lower() == unused_key:
                    request.headers.delete(key)
        t = datetime.now(UTC)

        request.headers.set(HEADER_X_DATE, t.strftime(DATE_FORMAT))
        request.headers.set(HEADER_X_ACCESS_KEY, self.key)

        signed_headers = self.signed_headers(request)
        # print(f"signed_headers: {signed_headers}")
        canonical_request = self.canonical_request(request, signed_headers)
        # print(f"canonical_request: {canonical_request}")
        string_to_sign_str = self.string_to_sign(canonical_request, t)
        # print(f"string_to_sign_str: {string_to_sign_str}")
        signature_str = self.sign_string_to_sign(string_to_sign_str, self.secret.encode('utf-8'))
        # print(f"signature_str: {signature_str}")

        return signature_str

    def sign_request(self, request: GatewayRequest) -> GatewayRequest:
        signature = self.sign(request)
        auth_header = self.auth_header_value(signature, self.key, self.signed_headers(request))
        request.headers.set(HEADER_X_AUTHORIZATION, auth_header)
        return request


def new_gateway_request_from_http(req: requests.Request) -> GatewayRequest:
    headers = RequestHeader()
    for k, v in req.headers.items():
        if k.lower() in ["content-type", "content-length", "accept-encoding"]:
            continue
        headers.set(k, v)

    payload = req.body if req.body else b"{}"
    url_info = urlparse(req.url)
    return GatewayRequest(headers, io.BytesIO(payload), req.method, req.url, url_info.netloc)


def new_gateway_request_from_grpc(message: Any, full_method: str, host: str,
                                  metadata: Tuple[Tuple[str, str]] = None) -> GatewayRequest:
    try:
        payload = b"{}"
        payload = json.dumps(MessageToDict(message),separators=(',', ':'),ensure_ascii=False).encode()
        # print(f"payload: {payload}")
        header = RequestHeader()
        if metadata:
            for k, v in metadata:
                header.set(k, v)
        req = GatewayRequest(header, io.BytesIO(payload), full_method, urlparse(f"http://{host}{full_method}"), host)
        return req
    except Exception as e:
        logger.error(f"new_gateway_request_from_grpc error: {e}")
        return None
