from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.api import annotations_pb2 as _annotations_pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as _options_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InfoResponse(_message.Message):
    __slots__ = ("version", "commit", "buildTime")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    BUILDTIME_FIELD_NUMBER: _ClassVar[int]
    version: str
    commit: str
    buildTime: str
    def __init__(self, version: _Optional[str] = ..., commit: _Optional[str] = ..., buildTime: _Optional[str] = ...) -> None: ...
