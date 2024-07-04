from google.protobuf import timestamp_pb2 as _timestamp_pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as _options_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Business(_message.Message):
    __slots__ = ("business_id", "business_name", "tags", "description", "created_by", "is_deleted", "created_at", "updated_at", "update_mask")
    BUSINESS_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    business_id: str
    business_name: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    description: str
    created_by: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, business_id: _Optional[str] = ..., business_name: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., created_by: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class PostBusinessRequest(_message.Message):
    __slots__ = ("business_name", "description", "tags")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, business_name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class PatchBusinessRequest(_message.Message):
    __slots__ = ("business_name", "description", "tags", "business_id", "name", "update_mask")
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    business_name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    business_id: str
    name: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, business_name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., business_id: _Optional[str] = ..., name: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetBusinessRequest(_message.Message):
    __slots__ = ("business",)
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    business: str
    def __init__(self, business: _Optional[str] = ...) -> None: ...

class DeleteBusinessRequest(_message.Message):
    __slots__ = ("business",)
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    business: str
    def __init__(self, business: _Optional[str] = ...) -> None: ...

class ListBusinessRequest(_message.Message):
    __slots__ = ("tags", "page", "page_size")
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedScalarFieldContainer[str]
    page: int
    page_size: int
    def __init__(self, tags: _Optional[_Iterable[str]] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListBusinessResponse(_message.Message):
    __slots__ = ("business",)
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    business: _containers.RepeatedCompositeFieldContainer[Business]
    def __init__(self, business: _Optional[_Iterable[_Union[Business, _Mapping]]] = ...) -> None: ...

class DeleteBusinessResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
