from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from . import user_pb2 as _user_pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginAPIRequest(_message.Message):
    __slots__ = ("auth", "seed", "is_keep_login")
    AUTH_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    IS_KEEP_LOGIN_FIELD_NUMBER: _ClassVar[int]
    auth: str
    seed: int
    is_keep_login: bool
    def __init__(self, auth: _Optional[str] = ..., seed: _Optional[int] = ..., is_keep_login: bool = ...) -> None: ...

class LogoutAPIRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LogoutAPIResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LoginAPIResponse(_message.Message):
    __slots__ = ("user", "token")
    USER_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.Users
    token: str
    def __init__(self, user: _Optional[_Union[_user_pb2.Users, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class AccountAPIRequest(_message.Message):
    __slots__ = ("uids",)
    UIDS_FIELD_NUMBER: _ClassVar[int]
    uids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uids: _Optional[_Iterable[str]] = ...) -> None: ...

class AccountAPIResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.Users]
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.Users, _Mapping]]] = ...) -> None: ...

class UserAuth(_message.Message):
    __slots__ = ("account", "password")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    account: str
    password: str
    def __init__(self, account: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RegsiterAPIRequest(_message.Message):
    __slots__ = ("auth", "ext")
    class ExtEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AUTH_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    auth: str
    ext: _containers.ScalarMap[str, str]
    def __init__(self, auth: _Optional[str] = ..., ext: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RegsiterAPIResponse(_message.Message):
    __slots__ = ("msg",)
    MSG_FIELD_NUMBER: _ClassVar[int]
    msg: str
    def __init__(self, msg: _Optional[str] = ...) -> None: ...

class AuthLogAPIRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class AuthSeed(_message.Message):
    __slots__ = ("seed", "key")
    SEED_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    seed: int
    key: str
    def __init__(self, seed: _Optional[int] = ..., key: _Optional[str] = ...) -> None: ...

class AuthLogAPIResponse(_message.Message):
    __slots__ = ("msg", "timestamp")
    MSG_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    msg: str
    timestamp: str
    def __init__(self, msg: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...
