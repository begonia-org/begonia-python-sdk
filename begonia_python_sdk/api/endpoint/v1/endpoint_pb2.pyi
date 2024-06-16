from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EndpointStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENABLED: _ClassVar[EndpointStatus]
    DISABLED: _ClassVar[EndpointStatus]

class EndpointSvrStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENDPOINT_UNKNOW: _ClassVar[EndpointSvrStatus]
    NOT_SUPPORT_BALANCE: _ClassVar[EndpointSvrStatus]
    SERVICE_NAME_DUPLICATE: _ClassVar[EndpointSvrStatus]
    ENDPOINT_NOT_FOUND: _ClassVar[EndpointSvrStatus]
ENABLED: EndpointStatus
DISABLED: EndpointStatus
ENDPOINT_UNKNOW: EndpointSvrStatus
NOT_SUPPORT_BALANCE: EndpointSvrStatus
SERVICE_NAME_DUPLICATE: EndpointSvrStatus
ENDPOINT_NOT_FOUND: EndpointSvrStatus

class EndpointMeta(_message.Message):
    __slots__ = ("addr", "weight")
    ADDR_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    addr: str
    weight: int
    def __init__(self, addr: _Optional[str] = ..., weight: _Optional[int] = ...) -> None: ...

class Endpoints(_message.Message):
    __slots__ = ("id", "name", "key", "owner", "service_name", "description", "proto_path", "endpoints", "status", "is_deleted", "balance", "version", "descriptor_set", "tags", "created_at", "updated_at", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROTO_PATH_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    key: str
    owner: str
    service_name: str
    description: str
    proto_path: str
    endpoints: _containers.RepeatedCompositeFieldContainer[EndpointMeta]
    status: EndpointStatus
    is_deleted: bool
    balance: str
    version: str
    descriptor_set: bytes
    tags: _containers.RepeatedScalarFieldContainer[str]
    created_at: str
    updated_at: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., key: _Optional[str] = ..., owner: _Optional[str] = ..., service_name: _Optional[str] = ..., description: _Optional[str] = ..., proto_path: _Optional[str] = ..., endpoints: _Optional[_Iterable[_Union[EndpointMeta, _Mapping]]] = ..., status: _Optional[_Union[EndpointStatus, str]] = ..., is_deleted: bool = ..., balance: _Optional[str] = ..., version: _Optional[str] = ..., descriptor_set: _Optional[bytes] = ..., tags: _Optional[_Iterable[str]] = ..., created_at: _Optional[str] = ..., updated_at: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class AddEndpointRequest(_message.Message):
    __slots__ = ("name", "service_name", "description", "proto_path", "endpoints", "balance", "tags", "proto_version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROTO_PATH_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PROTO_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_name: str
    description: str
    proto_path: str
    endpoints: _containers.RepeatedCompositeFieldContainer[EndpointMeta]
    balance: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    proto_version: str
    def __init__(self, name: _Optional[str] = ..., service_name: _Optional[str] = ..., description: _Optional[str] = ..., proto_path: _Optional[str] = ..., endpoints: _Optional[_Iterable[_Union[EndpointMeta, _Mapping]]] = ..., balance: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., proto_version: _Optional[str] = ...) -> None: ...

class UpdateEndpointRequest(_message.Message):
    __slots__ = ("name", "service_name", "description", "proto_path", "endpoint", "balance", "unique_key", "status", "is_deleted", "tags", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROTO_PATH_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_name: str
    description: str
    proto_path: str
    endpoint: _containers.RepeatedCompositeFieldContainer[EndpointMeta]
    balance: str
    unique_key: str
    status: EndpointStatus
    is_deleted: bool
    tags: _containers.RepeatedScalarFieldContainer[str]
    version: str
    def __init__(self, name: _Optional[str] = ..., service_name: _Optional[str] = ..., description: _Optional[str] = ..., proto_path: _Optional[str] = ..., endpoint: _Optional[_Iterable[_Union[EndpointMeta, _Mapping]]] = ..., balance: _Optional[str] = ..., unique_key: _Optional[str] = ..., status: _Optional[_Union[EndpointStatus, str]] = ..., is_deleted: bool = ..., tags: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ...) -> None: ...

class AddEndpointResponse(_message.Message):
    __slots__ = ("unique_key",)
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    def __init__(self, unique_key: _Optional[str] = ...) -> None: ...

class DeleteEndpointRequest(_message.Message):
    __slots__ = ("unique_key",)
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    def __init__(self, unique_key: _Optional[str] = ...) -> None: ...

class DeleteEndpointResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEndpointRequest(_message.Message):
    __slots__ = ("tags", "unique_keys")
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_KEYS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedScalarFieldContainer[str]
    unique_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tags: _Optional[_Iterable[str]] = ..., unique_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class ListEndpointResponse(_message.Message):
    __slots__ = ("endpoints",)
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[Endpoints]
    def __init__(self, endpoints: _Optional[_Iterable[_Union[Endpoints, _Mapping]]] = ...) -> None: ...

class DetailsEndpointRequest(_message.Message):
    __slots__ = ("unique_key",)
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    def __init__(self, unique_key: _Optional[str] = ...) -> None: ...

class DetailsEndpointResponse(_message.Message):
    __slots__ = ("endpoints",)
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    endpoints: Endpoints
    def __init__(self, endpoints: _Optional[_Union[Endpoints, _Mapping]] = ...) -> None: ...

class EndpointSrvConfig(_message.Message):
    __slots__ = ("descriptor_set", "name", "service_name", "description", "endpoints", "balance", "tags")
    DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    descriptor_set: bytes
    name: str
    service_name: str
    description: str
    endpoints: _containers.RepeatedCompositeFieldContainer[EndpointMeta]
    balance: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, descriptor_set: _Optional[bytes] = ..., name: _Optional[str] = ..., service_name: _Optional[str] = ..., description: _Optional[str] = ..., endpoints: _Optional[_Iterable[_Union[EndpointMeta, _Mapping]]] = ..., balance: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class EndpointSrvUpdateRequest(_message.Message):
    __slots__ = ("unique_key", "descriptor_set", "name", "description", "endpoints", "balance", "tags", "update_mask")
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    descriptor_set: bytes
    name: str
    description: str
    endpoints: _containers.RepeatedCompositeFieldContainer[EndpointMeta]
    balance: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, unique_key: _Optional[str] = ..., descriptor_set: _Optional[bytes] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., endpoints: _Optional[_Iterable[_Union[EndpointMeta, _Mapping]]] = ..., balance: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEndpointResponse(_message.Message):
    __slots__ = ("version", "updated_at")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    version: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, version: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SrvEndpoints(_message.Message):
    __slots__ = ("unique_key", "endpoints")
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    endpoints: _containers.RepeatedCompositeFieldContainer[EndpointMeta]
    def __init__(self, unique_key: _Optional[str] = ..., endpoints: _Optional[_Iterable[_Union[EndpointMeta, _Mapping]]] = ...) -> None: ...

class SrvDescriptorSet(_message.Message):
    __slots__ = ("unique_key", "descriptor_set")
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTOR_SET_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    descriptor_set: bytes
    def __init__(self, unique_key: _Optional[str] = ..., descriptor_set: _Optional[bytes] = ...) -> None: ...

class SvrLoadBalance(_message.Message):
    __slots__ = ("unique_key", "balance")
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    balance: str
    def __init__(self, unique_key: _Optional[str] = ..., balance: _Optional[str] = ...) -> None: ...

class SvrStatus(_message.Message):
    __slots__ = ("unique_key", "status")
    UNIQUE_KEY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    unique_key: str
    status: EndpointSvrStatus
    def __init__(self, unique_key: _Optional[str] = ..., status: _Optional[_Union[EndpointSvrStatus, str]] = ...) -> None: ...
