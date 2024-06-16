from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.api import annotations_pb2 as _annotations_pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EFFECT_UNSPECIFIED: _ClassVar[Effect]
    ALLOW: _ClassVar[Effect]
    DENY: _ClassVar[Effect]

class ConditionOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATOR_UNSPECIFIED: _ClassVar[ConditionOperator]
    StringEquals: _ClassVar[ConditionOperator]
    StringNotEquals: _ClassVar[ConditionOperator]
    StringEqualsIgnoreCase: _ClassVar[ConditionOperator]
    StringNotEqualsIgnoreCase: _ClassVar[ConditionOperator]
    StringLike: _ClassVar[ConditionOperator]
    StringNotLike: _ClassVar[ConditionOperator]
    NumericEquals: _ClassVar[ConditionOperator]
    NumericNotEquals: _ClassVar[ConditionOperator]
    NumericLessThan: _ClassVar[ConditionOperator]
    NumericLessThanEquals: _ClassVar[ConditionOperator]
    NumericGreaterThan: _ClassVar[ConditionOperator]
    NumericGreaterThanEquals: _ClassVar[ConditionOperator]
    BOOL: _ClassVar[ConditionOperator]
    DateEquals: _ClassVar[ConditionOperator]
    DateNotEquals: _ClassVar[ConditionOperator]
    DateLessThan: _ClassVar[ConditionOperator]
    DateLessThanEquals: _ClassVar[ConditionOperator]
    DateGreaterThan: _ClassVar[ConditionOperator]
    DateGreaterThanEquals: _ClassVar[ConditionOperator]
    IpAddress: _ClassVar[ConditionOperator]
    NotIpAddress: _ClassVar[ConditionOperator]
EFFECT_UNSPECIFIED: Effect
ALLOW: Effect
DENY: Effect
OPERATOR_UNSPECIFIED: ConditionOperator
StringEquals: ConditionOperator
StringNotEquals: ConditionOperator
StringEqualsIgnoreCase: ConditionOperator
StringNotEqualsIgnoreCase: ConditionOperator
StringLike: ConditionOperator
StringNotLike: ConditionOperator
NumericEquals: ConditionOperator
NumericNotEquals: ConditionOperator
NumericLessThan: ConditionOperator
NumericLessThanEquals: ConditionOperator
NumericGreaterThan: ConditionOperator
NumericGreaterThanEquals: ConditionOperator
BOOL: ConditionOperator
DateEquals: ConditionOperator
DateNotEquals: ConditionOperator
DateLessThan: ConditionOperator
DateLessThanEquals: ConditionOperator
DateGreaterThan: ConditionOperator
DateGreaterThanEquals: ConditionOperator
IpAddress: ConditionOperator
NotIpAddress: ConditionOperator

class Resource(_message.Message):
    __slots__ = ("id", "name", "description", "type", "parent_id", "owner", "created_at", "updated_at", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    type: str
    parent_id: str
    owner: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[str] = ..., parent_id: _Optional[str] = ..., owner: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ConditionKV(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Iterable[str]] = ...) -> None: ...

class Condition(_message.Message):
    __slots__ = ("kv",)
    class KvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ConditionKV
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ConditionKV, _Mapping]] = ...) -> None: ...
    KV_FIELD_NUMBER: _ClassVar[int]
    kv: _containers.MessageMap[str, ConditionKV]
    def __init__(self, kv: _Optional[_Mapping[str, ConditionKV]] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ("actions", "resource", "effect", "conditions", "principal", "unique_key")
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    resource: str
    effect: Effect
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    principal: str
    unique_key: str
    def __init__(self, actions: _Optional[_Iterable[str]] = ..., resource: _Optional[str] = ..., effect: _Optional[_Union[Effect, str]] = ..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ..., principal: _Optional[str] = ..., unique_key: _Optional[str] = ...) -> None: ...

class PutPolicyRequest(_message.Message):
    __slots__ = ("actions", "resource", "effect", "conditions", "principal", "mask")
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    resource: str
    effect: Effect
    conditions: _containers.RepeatedCompositeFieldContainer[Condition]
    principal: str
    mask: _field_mask_pb2.FieldMask
    def __init__(self, actions: _Optional[_Iterable[str]] = ..., resource: _Optional[str] = ..., effect: _Optional[_Union[Effect, str]] = ..., conditions: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ..., principal: _Optional[str] = ..., mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class AccessEnv(_message.Message):
    __slots__ = ("ip", "user_agent", "referer", "request_id", "created_at")
    IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    REFERER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    user_agent: str
    referer: str
    request_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, ip: _Optional[str] = ..., user_agent: _Optional[str] = ..., referer: _Optional[str] = ..., request_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FailReason(_message.Message):
    __slots__ = ("message", "key", "actual", "operator")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXCEPT_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    message: str
    key: str
    actual: str
    operator: str
    def __init__(self, message: _Optional[str] = ..., key: _Optional[str] = ..., actual: _Optional[str] = ..., operator: _Optional[str] = ..., **kwargs) -> None: ...

class AccessContext(_message.Message):
    __slots__ = ("principal", "resource", "action", "context", "env", "fail")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    principal: str
    resource: _containers.RepeatedScalarFieldContainer[str]
    action: str
    context: _containers.ScalarMap[str, str]
    env: AccessEnv
    fail: FailReason
    def __init__(self, principal: _Optional[str] = ..., resource: _Optional[_Iterable[str]] = ..., action: _Optional[str] = ..., context: _Optional[_Mapping[str, str]] = ..., env: _Optional[_Union[AccessEnv, _Mapping]] = ..., fail: _Optional[_Union[FailReason, _Mapping]] = ...) -> None: ...

class AccessResponse(_message.Message):
    __slots__ = ("message", "fail")
    PASS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FAIL_FIELD_NUMBER: _ClassVar[int]
    message: str
    fail: FailReason
    def __init__(self, message: _Optional[str] = ..., fail: _Optional[_Union[FailReason, _Mapping]] = ..., **kwargs) -> None: ...

class PolicyRequest(_message.Message):
    __slots__ = ("unique_key",)
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    def __init__(self, unique_key: _Optional[str] = ...) -> None: ...

class PutPolicyResponse(_message.Message):
    __slots__ = ("unique_key",)
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    def __init__(self, unique_key: _Optional[str] = ...) -> None: ...

class PatchPolicyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
