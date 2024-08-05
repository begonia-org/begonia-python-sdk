from google.protobuf import any_pb2 as _any_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PluginRequest(_message.Message):
    __slots__ = ("request", "full_method_name")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    FULL_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    request: _any_pb2.Any
    full_method_name: str
    def __init__(self, request: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., full_method_name: _Optional[str] = ...) -> None: ...

class PluginResponse(_message.Message):
    __slots__ = ("new_request",)
    NEW_REQUEST_FIELD_NUMBER: _ClassVar[int]
    new_request: _any_pb2.Any
    def __init__(self, new_request: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class PluginInfo(_message.Message):
    __slots__ = ("name", "description", "version", "commit")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    version: str
    commit: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., commit: _Optional[str] = ...) -> None: ...
