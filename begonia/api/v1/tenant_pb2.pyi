from google.protobuf import timestamp_pb2 as _timestamp_pb2
from begonia.api.v1 import options_pb2 as _options_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TENANTS_STATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TENANTS_ACTIVE: _ClassVar[TENANTS_STATUS]
    TENANTS_INACTIVE: _ClassVar[TENANTS_STATUS]
    TENANTS_LOCKED: _ClassVar[TENANTS_STATUS]
    TENANTS_DELETED: _ClassVar[TENANTS_STATUS]
TENANTS_ACTIVE: TENANTS_STATUS
TENANTS_INACTIVE: TENANTS_STATUS
TENANTS_LOCKED: TENANTS_STATUS
TENANTS_DELETED: TENANTS_STATUS

class Tenants(_message.Message):
    __slots__ = ("tenant_id", "tenant_name", "description", "tags", "status", "email", "created_by", "is_deleted", "admin_id", "created_at", "updated_at", "update_mask")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    tenant_name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    status: TENANTS_STATUS
    email: str
    created_by: str
    is_deleted: bool
    admin_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tenant_id: _Optional[str] = ..., tenant_name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[TENANTS_STATUS, str]] = ..., email: _Optional[str] = ..., created_by: _Optional[str] = ..., is_deleted: bool = ..., admin_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class TenantsBusiness(_message.Message):
    __slots__ = ("tenant_id", "tenant_name", "business_id", "business_name", "plan", "created_by", "is_deleted", "created_at", "updated_at", "update_mask")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    tenant_name: str
    business_id: str
    business_name: str
    plan: str
    created_by: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tenant_id: _Optional[str] = ..., tenant_name: _Optional[str] = ..., business_id: _Optional[str] = ..., business_name: _Optional[str] = ..., plan: _Optional[str] = ..., created_by: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class PostTenantRequest(_message.Message):
    __slots__ = ("tenant_name", "description", "tags", "email")
    TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    tenant_name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    email: str
    def __init__(self, tenant_name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., email: _Optional[str] = ...) -> None: ...

class PatchTenantRequest(_message.Message):
    __slots__ = ("tenant_name", "description", "tags", "email", "tenant_id", "admin_id", "status", "update_mask")
    TENANT_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tenant_name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    email: str
    tenant_id: str
    admin_id: str
    status: TENANTS_STATUS
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, tenant_name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., email: _Optional[str] = ..., tenant_id: _Optional[str] = ..., admin_id: _Optional[str] = ..., status: _Optional[_Union[TENANTS_STATUS, str]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetTenantRequest(_message.Message):
    __slots__ = ("tenant",)
    TENANT_FIELD_NUMBER: _ClassVar[int]
    tenant: str
    def __init__(self, tenant: _Optional[str] = ...) -> None: ...

class DeleteTenantRequest(_message.Message):
    __slots__ = ("tenant",)
    TENANT_FIELD_NUMBER: _ClassVar[int]
    tenant: str
    def __init__(self, tenant: _Optional[str] = ...) -> None: ...

class DeleteTenantResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTenantsRequest(_message.Message):
    __slots__ = ("tags", "page", "page_size", "status")
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedScalarFieldContainer[str]
    page: int
    page_size: int
    status: _containers.RepeatedScalarFieldContainer[TENANTS_STATUS]
    def __init__(self, tags: _Optional[_Iterable[str]] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., status: _Optional[_Iterable[_Union[TENANTS_STATUS, str]]] = ...) -> None: ...

class ListTenantsResponse(_message.Message):
    __slots__ = ("tenants",)
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    tenants: _containers.RepeatedCompositeFieldContainer[Tenants]
    def __init__(self, tenants: _Optional[_Iterable[_Union[Tenants, _Mapping]]] = ...) -> None: ...

class AddTenantBusinessRequest(_message.Message):
    __slots__ = ("tenant_id", "business_id", "plan")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    business_id: str
    plan: str
    def __init__(self, tenant_id: _Optional[str] = ..., business_id: _Optional[str] = ..., plan: _Optional[str] = ...) -> None: ...

class DeleteTenantBusinessRequest(_message.Message):
    __slots__ = ("tenant_id", "business_id")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_ID_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    business_id: str
    def __init__(self, tenant_id: _Optional[str] = ..., business_id: _Optional[str] = ...) -> None: ...

class DeleteTenantBusinessResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTenantBusinessRequest(_message.Message):
    __slots__ = ("tenant", "page", "page_size")
    TENANT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    tenant: str
    page: int
    page_size: int
    def __init__(self, tenant: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListTenantBusinessResponse(_message.Message):
    __slots__ = ("tenants_business",)
    TENANTS_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    tenants_business: _containers.RepeatedCompositeFieldContainer[TenantsBusiness]
    def __init__(self, tenants_business: _Optional[_Iterable[_Union[TenantsBusiness, _Mapping]]] = ...) -> None: ...
