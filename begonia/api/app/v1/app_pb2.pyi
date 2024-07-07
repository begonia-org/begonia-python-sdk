from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.api import annotations_pb2 as _annotations_pb2
from begonia.api.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class APPStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_ENABLED: _ClassVar[APPStatus]
    APP_DISABLED: _ClassVar[APPStatus]

class APPPremission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_READ: _ClassVar[APPPremission]
    APP_WRITE: _ClassVar[APPPremission]
    APP_DELETE: _ClassVar[APPPremission]
    APP_ALL: _ClassVar[APPPremission]

class APPSvrCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    APP_UNKNOWN: _ClassVar[APPSvrCode]
    APP_CREATE_ERR: _ClassVar[APPSvrCode]
    APP_DUPLICATE_ERR: _ClassVar[APPSvrCode]
    APP_SIGNATURE_ERR: _ClassVar[APPSvrCode]
    APP_REQUEST_EXPIRED_ERR: _ClassVar[APPSvrCode]
    APP_ACCESS_KEY_MISSING_ERR: _ClassVar[APPSvrCode]
    APP_AUTH_MISSING_ERR: _ClassVar[APPSvrCode]
    APP_XDATE_MISSING_ERR: _ClassVar[APPSvrCode]
    APP_NOT_FOUND_ERR: _ClassVar[APPSvrCode]
APP_ENABLED: APPStatus
APP_DISABLED: APPStatus
APP_READ: APPPremission
APP_WRITE: APPPremission
APP_DELETE: APPPremission
APP_ALL: APPPremission
APP_UNKNOWN: APPSvrCode
APP_CREATE_ERR: APPSvrCode
APP_DUPLICATE_ERR: APPSvrCode
APP_SIGNATURE_ERR: APPSvrCode
APP_REQUEST_EXPIRED_ERR: APPSvrCode
APP_ACCESS_KEY_MISSING_ERR: APPSvrCode
APP_AUTH_MISSING_ERR: APPSvrCode
APP_XDATE_MISSING_ERR: APPSvrCode
APP_NOT_FOUND_ERR: APPSvrCode

class Apps(_message.Message):
    __slots__ = ("id", "name", "description", "status", "appid", "access_key", "secret", "owner", "permission", "is_deleted", "tags", "created_at", "updated_at", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    status: APPStatus
    appid: str
    access_key: str
    secret: str
    owner: str
    permission: int
    is_deleted: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[APPStatus, str]] = ..., appid: _Optional[str] = ..., access_key: _Optional[str] = ..., secret: _Optional[str] = ..., owner: _Optional[str] = ..., permission: _Optional[int] = ..., is_deleted: bool = ..., tags: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateAppRequest(_message.Message):
    __slots__ = ("name", "description", "tags")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class AddAppResponse(_message.Message):
    __slots__ = ("appid", "access_key", "secret")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    appid: str
    access_key: str
    secret: str
    def __init__(self, appid: _Optional[str] = ..., access_key: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class DeleteAppRequest(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: str
    def __init__(self, appid: _Optional[str] = ...) -> None: ...

class DeleteAppResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AppsRequest(_message.Message):
    __slots__ = ("appid", "name", "description", "tags", "update_mask")
    APPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    appid: str
    name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, appid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetAPPRequest(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: str
    def __init__(self, appid: _Optional[str] = ...) -> None: ...

class AppsListRequest(_message.Message):
    __slots__ = ("page", "page_size", "tags", "status")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    page: int
    page_size: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    status: _containers.RepeatedScalarFieldContainer[APPStatus]
    def __init__(self, page: _Optional[int] = ..., page_size: _Optional[int] = ..., tags: _Optional[_Iterable[str]] = ..., status: _Optional[_Iterable[_Union[APPStatus, str]]] = ...) -> None: ...

class AppsListResponse(_message.Message):
    __slots__ = ("apps", "total")
    APPS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[Apps]
    total: int
    def __init__(self, apps: _Optional[_Iterable[_Union[Apps, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...
