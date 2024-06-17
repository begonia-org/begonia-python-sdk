from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as _options_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileSvrStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_UNKNOWN: _ClassVar[FileSvrStatus]
    FILE_UPLOAD_NOT_INITIATE_ERR: _ClassVar[FileSvrStatus]
    FILE_SHA256_NOT_MATCH_ERR: _ClassVar[FileSvrStatus]
    FILE_UPLOADID_MISSING_ERR: _ClassVar[FileSvrStatus]
    FILE_PARTNUMBER_MISSING_ERR: _ClassVar[FileSvrStatus]
    FILE_NOT_FOUND_UPLOADID_ERR: _ClassVar[FileSvrStatus]
    FILE_INVALIDATE_KEY_ERR: _ClassVar[FileSvrStatus]
    FILE_INVALIDATE_RANGE_ERR: _ClassVar[FileSvrStatus]
    FILE_INVALIDATE_BUCKET_ERR: _ClassVar[FileSvrStatus]
    FILE_INVALIDATE_ENGINE_ERR: _ClassVar[FileSvrStatus]

class FileEngine(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_ENGINE_UNKNOWN: _ClassVar[FileEngine]
    FILE_ENGINE_LOCAL: _ClassVar[FileEngine]
    FILE_ENGINE_MINIO: _ClassVar[FileEngine]
    FILE_ENGINE_S3: _ClassVar[FileEngine]
    FILE_ENGINE_OSS: _ClassVar[FileEngine]
FILE_UNKNOWN: FileSvrStatus
FILE_UPLOAD_NOT_INITIATE_ERR: FileSvrStatus
FILE_SHA256_NOT_MATCH_ERR: FileSvrStatus
FILE_UPLOADID_MISSING_ERR: FileSvrStatus
FILE_PARTNUMBER_MISSING_ERR: FileSvrStatus
FILE_NOT_FOUND_UPLOADID_ERR: FileSvrStatus
FILE_INVALIDATE_KEY_ERR: FileSvrStatus
FILE_INVALIDATE_RANGE_ERR: FileSvrStatus
FILE_INVALIDATE_BUCKET_ERR: FileSvrStatus
FILE_INVALIDATE_ENGINE_ERR: FileSvrStatus
FILE_ENGINE_UNKNOWN: FileEngine
FILE_ENGINE_LOCAL: FileEngine
FILE_ENGINE_MINIO: FileEngine
FILE_ENGINE_S3: FileEngine
FILE_ENGINE_OSS: FileEngine

class InitiateMultipartUploadRequest(_message.Message):
    __slots__ = ("key", "engine")
    KEY_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    key: str
    engine: str
    def __init__(self, key: _Optional[str] = ..., engine: _Optional[str] = ...) -> None: ...

class InitiateMultipartUploadResponse(_message.Message):
    __slots__ = ("upload_id",)
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class UploadMultipartFileRequest(_message.Message):
    __slots__ = ("key", "content", "upload_id", "part_number", "sha256", "engine")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    key: str
    content: bytes
    upload_id: str
    part_number: int
    sha256: str
    engine: str
    def __init__(self, key: _Optional[str] = ..., content: _Optional[bytes] = ..., upload_id: _Optional[str] = ..., part_number: _Optional[int] = ..., sha256: _Optional[str] = ..., engine: _Optional[str] = ...) -> None: ...

class UploadMultipartFileResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadFileRequest(_message.Message):
    __slots__ = ("key", "content", "content_type", "sha256", "use_version", "bucket", "engine")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    USE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    key: str
    content: bytes
    content_type: str
    sha256: str
    use_version: bool
    bucket: str
    engine: str
    def __init__(self, key: _Optional[str] = ..., content: _Optional[bytes] = ..., content_type: _Optional[str] = ..., sha256: _Optional[str] = ..., use_version: bool = ..., bucket: _Optional[str] = ..., engine: _Optional[str] = ...) -> None: ...

class FileSystemEngine(_message.Message):
    __slots__ = ("name", "endpoint", "access_key", "secret_key")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    endpoint: str
    access_key: str
    secret_key: str
    def __init__(self, name: _Optional[str] = ..., endpoint: _Optional[str] = ..., access_key: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class ListFilesRequest(_message.Message):
    __slots__ = ("bucket", "engine", "page", "page_size")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    engine: str
    page: int
    page_size: int
    def __init__(self, bucket: _Optional[str] = ..., engine: _Optional[str] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ...) -> None: ...

class ListFilesResponse(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[Files]
    def __init__(self, files: _Optional[_Iterable[_Union[Files, _Mapping]]] = ...) -> None: ...

class MakeBucketRequest(_message.Message):
    __slots__ = ("bucket", "Region", "object_locking", "engine")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LOCKING_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    Region: str
    object_locking: bool
    engine: str
    def __init__(self, bucket: _Optional[str] = ..., Region: _Optional[str] = ..., object_locking: bool = ..., engine: _Optional[str] = ...) -> None: ...

class MakeBucketResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadFileResponse(_message.Message):
    __slots__ = ("uri", "version", "uid")
    URI_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    uri: str
    version: str
    uid: str
    def __init__(self, uri: _Optional[str] = ..., version: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class CompleteMultipartUploadRequest(_message.Message):
    __slots__ = ("upload_id", "key", "content_type", "sha256", "use_version", "bucket", "engine")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    USE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    key: str
    content_type: str
    sha256: str
    use_version: bool
    bucket: str
    engine: str
    def __init__(self, upload_id: _Optional[str] = ..., key: _Optional[str] = ..., content_type: _Optional[str] = ..., sha256: _Optional[str] = ..., use_version: bool = ..., bucket: _Optional[str] = ..., engine: _Optional[str] = ...) -> None: ...

class CompleteMultipartUploadResponse(_message.Message):
    __slots__ = ("uri", "sha256", "version", "uid")
    URI_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    uri: str
    sha256: str
    version: str
    uid: str
    def __init__(self, uri: _Optional[str] = ..., sha256: _Optional[str] = ..., version: _Optional[str] = ..., uid: _Optional[str] = ...) -> None: ...

class AbortMultipartUploadRequest(_message.Message):
    __slots__ = ("upload_id", "engine")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    engine: str
    def __init__(self, upload_id: _Optional[str] = ..., engine: _Optional[str] = ...) -> None: ...

class AbortMultipartUploadResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UploadAPIResponse(_message.Message):
    __slots__ = ("uri", "sha256")
    URI_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    uri: str
    sha256: str
    def __init__(self, uri: _Optional[str] = ..., sha256: _Optional[str] = ...) -> None: ...

class DownloadRequest(_message.Message):
    __slots__ = ("key", "version", "bucket", "engine", "file_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    version: str
    bucket: str
    engine: str
    file_id: str
    def __init__(self, key: _Optional[str] = ..., version: _Optional[str] = ..., bucket: _Optional[str] = ..., engine: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class DownloadResponse(_message.Message):
    __slots__ = ("content", "part_number")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    part_number: int
    def __init__(self, content: _Optional[bytes] = ..., part_number: _Optional[int] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("key", "version", "bucket", "engine", "file_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    version: str
    bucket: str
    engine: str
    file_id: str
    def __init__(self, key: _Optional[str] = ..., version: _Optional[str] = ..., bucket: _Optional[str] = ..., engine: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FileMetadataRequest(_message.Message):
    __slots__ = ("key", "version", "bucket", "engine", "file_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    version: str
    bucket: str
    engine: str
    file_id: str
    def __init__(self, key: _Optional[str] = ..., version: _Optional[str] = ..., bucket: _Optional[str] = ..., engine: _Optional[str] = ..., file_id: _Optional[str] = ...) -> None: ...

class FileMetadataResponse(_message.Message):
    __slots__ = ("key", "size", "sha256", "content_type", "etag", "modify_time", "name", "version", "uid", "bucket")
    KEY_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    key: str
    size: int
    sha256: str
    content_type: str
    etag: str
    modify_time: int
    name: str
    version: str
    uid: str
    bucket: str
    def __init__(self, key: _Optional[str] = ..., size: _Optional[int] = ..., sha256: _Optional[str] = ..., content_type: _Optional[str] = ..., etag: _Optional[str] = ..., modify_time: _Optional[int] = ..., name: _Optional[str] = ..., version: _Optional[str] = ..., uid: _Optional[str] = ..., bucket: _Optional[str] = ...) -> None: ...

class Files(_message.Message):
    __slots__ = ("ID", "uid", "key", "bucket", "engine", "is_deleted", "created_at", "updated_at", "owner", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ID: int
    uid: str
    key: str
    bucket: str
    engine: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    owner: str
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, ID: _Optional[int] = ..., uid: _Optional[str] = ..., key: _Optional[str] = ..., bucket: _Optional[str] = ..., engine: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., owner: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class Buckets(_message.Message):
    __slots__ = ("ID", "uid", "engine", "bucket", "owner", "is_deleted", "created_at", "updated_at", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    IS_DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ID: int
    uid: str
    engine: str
    bucket: str
    owner: str
    is_deleted: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, ID: _Optional[int] = ..., uid: _Optional[str] = ..., engine: _Optional[str] = ..., bucket: _Optional[str] = ..., owner: _Optional[str] = ..., is_deleted: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
