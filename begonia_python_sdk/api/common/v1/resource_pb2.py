# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/resource.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ommon/resource.proto\x12\x1d\x62\x65gonia.org.sdk.common.api.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc5\x01\n\x08Resource\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x13\n\x0bResourceKey\x18\x02 \x01(\t\x12\x14\n\x0cResourceName\x18\x03 \x01(\t\x12\x15\n\rResourceTable\x18\x04 \x01(\t\x12\x0b\n\x03uid\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xbf\x01\n\x05\x46iles\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x0b\n\x03sha\x18\x04 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\x12\n\nis_deleted\x18\x06 \x01(\x08\x12.\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB-Z+github.com/begonia-org/go-sdk/common/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.resource_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/begonia-org/go-sdk/common/api/v1'
  _globals['_RESOURCE']._serialized_start=90
  _globals['_RESOURCE']._serialized_end=287
  _globals['_FILES']._serialized_start=290
  _globals['_FILES']._serialized_end=481
# @@protoc_insertion_point(module_scope)
