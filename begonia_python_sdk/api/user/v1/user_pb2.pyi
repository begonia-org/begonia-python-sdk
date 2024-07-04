from google.protobuf import timestamp_pb2 as _timestamp_pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as _options_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADMIN: _ClassVar[Role]

class USER_STATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVE: _ClassVar[USER_STATUS]
    INACTIVE: _ClassVar[USER_STATUS]
    LOCKED: _ClassVar[USER_STATUS]
    DELETED: _ClassVar[USER_STATUS]

class UserSvrCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_UNKNOWN: _ClassVar[UserSvrCode]
    USER_LOGIN_ERR: _ClassVar[UserSvrCode]
    USER_TOKEN_EXPIRE_ERR: _ClassVar[UserSvrCode]
    USER_DISABLED_ERR: _ClassVar[UserSvrCode]
    USER_TOKEN_INVALIDATE_ERR: _ClassVar[UserSvrCode]
    USER_TOKEN_NOT_ACTIVTE_ERR: _ClassVar[UserSvrCode]
    USER_AUTH_DECRYPT_ERR: _ClassVar[UserSvrCode]
    USER_ACCOUNT_ERR: _ClassVar[UserSvrCode]
    USER_PASSWORD_ERR: _ClassVar[UserSvrCode]
    USER_NOT_FOUND_ERR: _ClassVar[UserSvrCode]
    USER_AUTH_MISSING_ERR: _ClassVar[UserSvrCode]
    USER_IDENTITY_MISSING_ERR: _ClassVar[UserSvrCode]
    USER_APIKEY_NOT_MATCH_ERR: _ClassVar[UserSvrCode]
    USER_USERNAME_DUPLICATE_ERR: _ClassVar[UserSvrCode]
ADMIN: Role
ACTIVE: USER_STATUS
INACTIVE: USER_STATUS
LOCKED: USER_STATUS
DELETED: USER_STATUS
USER_UNKNOWN: UserSvrCode
USER_LOGIN_ERR: UserSvrCode
USER_TOKEN_EXPIRE_ERR: UserSvrCode
USER_DISABLED_ERR: UserSvrCode
USER_TOKEN_INVALIDATE_ERR: UserSvrCode
USER_TOKEN_NOT_ACTIVTE_ERR: UserSvrCode
USER_AUTH_DECRYPT_ERR: UserSvrCode
USER_ACCOUNT_ERR: UserSvrCode
USER_PASSWORD_ERR: UserSvrCode
USER_NOT_FOUND_ERR: UserSvrCode
USER_AUTH_MISSING_ERR: UserSvrCode
USER_IDENTITY_MISSING_ERR: UserSvrCode
USER_APIKEY_NOT_MATCH_ERR: UserSvrCode
USER_USERNAME_DUPLICATE_ERR: UserSvrCode

class Users(_message.Message):
    __slots__ = ("ID", "uid", "owner", "dept", "name", "email", "phone", "password", "avatar", "role", "status", "tenant_id", "is_deleted", "created_at", "updated_at", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DEPT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ID: int
    uid: str
    owner: str
    dept: str
    name: str
    email: str
    phone: str
    password: str
    avatar: str
    role: Role
    status: USER_STATUS
    tenant_id: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, ID: _Optional[int] = ..., uid: _Optional[str] = ..., owner: _Optional[str] = ..., dept: _Optional[str] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., password: _Optional[str] = ..., avatar: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., status: _Optional[_Union[USER_STATUS, str]] = ..., tenant_id: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class BasicAuth(_message.Message):
    __slots__ = ("uid", "name", "role", "audience", "issuer", "not_before", "expiration", "issued_at", "is_keep_login", "token")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    NOT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    ISSUED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_KEEP_LOGIN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    uid: str
    name: str
    role: Role
    audience: str
    issuer: str
    not_before: int
    expiration: int
    issued_at: int
    is_keep_login: bool
    token: str
    def __init__(self, uid: _Optional[str] = ..., name: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., audience: _Optional[str] = ..., issuer: _Optional[str] = ..., not_before: _Optional[int] = ..., expiration: _Optional[int] = ..., issued_at: _Optional[int] = ..., is_keep_login: bool = ..., token: _Optional[str] = ...) -> None: ...

class PostUserRequest(_message.Message):
    __slots__ = ("name", "password", "email", "phone", "role", "status", "dept", "owner", "avatar", "tenant_id", "update_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEPT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    password: str
    email: str
    phone: str
    role: Role
    status: USER_STATUS
    dept: str
    owner: str
    avatar: str
    tenant_id: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., password: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., status: _Optional[_Union[USER_STATUS, str]] = ..., dept: _Optional[str] = ..., owner: _Optional[str] = ..., avatar: _Optional[str] = ..., tenant_id: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class DeleteUserResponse(_message.Message):
    __slots__ = ("uid",)
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class PatchUserRequest(_message.Message):
    __slots__ = ("uid", "name", "password", "email", "phone", "role", "status", "dept", "owner", "avatar", "update_mask")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DEPT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    uid: str
    name: str
    password: str
    email: str
    phone: str
    role: Role
    status: USER_STATUS
    dept: str
    owner: str
    avatar: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, uid: _Optional[str] = ..., name: _Optional[str] = ..., password: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., role: _Optional[_Union[Role, str]] = ..., status: _Optional[_Union[USER_STATUS, str]] = ..., dept: _Optional[str] = ..., owner: _Optional[str] = ..., avatar: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
