from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Resource(_message.Message):
    __slots__ = ("ID", "ResourceKey", "ResourceName", "ResourceTable", "uid", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCEKEY_FIELD_NUMBER: _ClassVar[int]
    RESOURCENAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCETABLE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID: int
    ResourceKey: str
    ResourceName: str
    ResourceTable: str
    uid: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, ID: _Optional[int] = ..., ResourceKey: _Optional[str] = ..., ResourceName: _Optional[str] = ..., ResourceTable: _Optional[str] = ..., uid: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Files(_message.Message):
    __slots__ = ("ID", "name", "uri", "sha", "author", "is_deleted", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID: int
    name: str
    uri: str
    sha: str
    author: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, ID: _Optional[int] = ..., name: _Optional[str] = ..., uri: _Optional[str] = ..., sha: _Optional[str] = ..., author: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
