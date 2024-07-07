from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from begonia.api.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumAllow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALLOW: _ClassVar[EnumAllow]
    DENY: _ClassVar[EnumAllow]
ALLOW: EnumAllow
DENY: EnumAllow

class ErrorRequest(_message.Message):
    __slots__ = ("msg", "code")
    MSG_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    msg: str
    code: int
    def __init__(self, msg: _Optional[str] = ..., code: _Optional[int] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("msg", "name")
    MSG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    msg: str
    name: str
    def __init__(self, msg: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class HelloSubRequest(_message.Message):
    __slots__ = ("sub_msg", "sub_name", "sub_age", "update_mask")
    SUB_MSG_FIELD_NUMBER: _ClassVar[int]
    SUB_NAME_FIELD_NUMBER: _ClassVar[int]
    SUB_AGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    sub_msg: str
    sub_name: str
    sub_age: int
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, sub_msg: _Optional[str] = ..., sub_name: _Optional[str] = ..., sub_age: _Optional[int] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class HelloRequestWithValidator(_message.Message):
    __slots__ = ("msg", "name", "age", "sub", "subs", "update_mask", "sub_map", "sub_map2")
    class SubMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: HelloSubRequest
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[HelloSubRequest, _Mapping]] = ...) -> None: ...
    class SubMap2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MSG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    SUB_FIELD_NUMBER: _ClassVar[int]
    SUBS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SUB_MAP_FIELD_NUMBER: _ClassVar[int]
    SUB_MAP2_FIELD_NUMBER: _ClassVar[int]
    msg: str
    name: str
    age: int
    sub: HelloSubRequest
    subs: _containers.RepeatedCompositeFieldContainer[HelloSubRequest]
    update_mask: _field_mask_pb2.FieldMask
    sub_map: _containers.MessageMap[str, HelloSubRequest]
    sub_map2: _containers.ScalarMap[str, str]
    def __init__(self, msg: _Optional[str] = ..., name: _Optional[str] = ..., age: _Optional[int] = ..., sub: _Optional[_Union[HelloSubRequest, _Mapping]] = ..., subs: _Optional[_Iterable[_Union[HelloSubRequest, _Mapping]]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., sub_map: _Optional[_Mapping[str, HelloSubRequest]] = ..., sub_map2: _Optional[_Mapping[str, str]] = ...) -> None: ...

class HelloReply(_message.Message):
    __slots__ = ("message", "name")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    message: str
    name: str
    def __init__(self, message: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RepeatedReply(_message.Message):
    __slots__ = ("replies",)
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    replies: _containers.RepeatedCompositeFieldContainer[HelloReply]
    def __init__(self, replies: _Optional[_Iterable[_Union[HelloReply, _Mapping]]] = ...) -> None: ...

class ExampleMessage(_message.Message):
    __slots__ = ("message", "code", "float_num", "float_data", "byte_data", "bool_data", "allow", "repeated_data", "fixed_data", "sfixed_data", "sfixed32_data", "fixed32_data", "repeated_msg", "msg", "mask")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_NUM_FIELD_NUMBER: _ClassVar[int]
    FLOAT_DATA_FIELD_NUMBER: _ClassVar[int]
    BYTE_DATA_FIELD_NUMBER: _ClassVar[int]
    BOOL_DATA_FIELD_NUMBER: _ClassVar[int]
    ALLOW_FIELD_NUMBER: _ClassVar[int]
    REPEATED_DATA_FIELD_NUMBER: _ClassVar[int]
    FIXED_DATA_FIELD_NUMBER: _ClassVar[int]
    SFIXED_DATA_FIELD_NUMBER: _ClassVar[int]
    SFIXED32_DATA_FIELD_NUMBER: _ClassVar[int]
    FIXED32_DATA_FIELD_NUMBER: _ClassVar[int]
    REPEATED_MSG_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    message: str
    code: int
    float_num: float
    float_data: float
    byte_data: bytes
    bool_data: bool
    allow: EnumAllow
    repeated_data: _containers.RepeatedScalarFieldContainer[int]
    fixed_data: int
    sfixed_data: int
    sfixed32_data: int
    fixed32_data: int
    repeated_msg: _containers.RepeatedCompositeFieldContainer[HelloRequest]
    msg: HelloRequest
    mask: _field_mask_pb2.FieldMask
    def __init__(self, message: _Optional[str] = ..., code: _Optional[int] = ..., float_num: _Optional[float] = ..., float_data: _Optional[float] = ..., byte_data: _Optional[bytes] = ..., bool_data: bool = ..., allow: _Optional[_Union[EnumAllow, str]] = ..., repeated_data: _Optional[_Iterable[int]] = ..., fixed_data: _Optional[int] = ..., sfixed_data: _Optional[int] = ..., sfixed32_data: _Optional[int] = ..., fixed32_data: _Optional[int] = ..., repeated_msg: _Optional[_Iterable[_Union[HelloRequest, _Mapping]]] = ..., msg: _Optional[_Union[HelloRequest, _Mapping]] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ExampleTable(_message.Message):
    __slots__ = ("ID", "uid", "owner", "is_deleted", "created_at", "updated_at", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ID: int
    uid: str
    owner: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, ID: _Optional[int] = ..., uid: _Optional[str] = ..., owner: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
