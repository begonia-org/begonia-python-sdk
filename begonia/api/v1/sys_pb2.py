# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sys.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from begonia.api.v1 import options_pb2 as begonia_dot_api_dot_v1_dot_options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsys.proto\x12\x0f\x62\x65gonia.org.sdk\x1a google/protobuf/descriptor.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1c\x62\x65gonia/api/v1/options.proto\"\r\n\x0bInfoRequest\"B\n\x0cInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0e\n\x06\x63ommit\x18\x02 \x01(\t\x12\x11\n\tbuildTime\x18\x03 \x01(\t2\x92\x01\n\rSystemService\x12\\\n\x03Get\x12\x1c.begonia.org.sdk.InfoRequest\x1a\x1d.begonia.org.sdk.InfoResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/gateway/info\x1a#\x88\xb7\x18\x01\xb2\xb7\x18\x1b\x62\x65gonia.api.v1.HttpResponseB&Z$github.com/begonia-org/go-sdk/api/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sys_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/begonia-org/go-sdk/api/v1'
  _globals['_SYSTEMSERVICE']._options = None
  _globals['_SYSTEMSERVICE']._serialized_options = b'\210\267\030\001\262\267\030\033begonia.api.v1.HttpResponse'
  _globals['_SYSTEMSERVICE'].methods_by_name['Get']._options = None
  _globals['_SYSTEMSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\022\022\020/v1/gateway/info'
  _globals['_INFOREQUEST']._serialized_start=124
  _globals['_INFOREQUEST']._serialized_end=137
  _globals['_INFORESPONSE']._serialized_start=139
  _globals['_INFORESPONSE']._serialized_end=205
  _globals['_SYSTEMSERVICE']._serialized_start=208
  _globals['_SYSTEMSERVICE']._serialized_end=354
# @@protoc_insertion_point(module_scope)
