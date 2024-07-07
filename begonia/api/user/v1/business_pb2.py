# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: business.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from begonia.api.v1 import options_pb2 as begonia_dot_api_dot_v1_dot_options__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x62usiness.proto\x12\x0f\x62\x65gonia.org.sdk\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1c\x62\x65gonia/api/v1/options.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\"\xeb\x02\n\x08\x42usiness\x12 \n\x0b\x62usiness_id\x18\x01 \x01(\tR\x0b\x62usiness_id\x12$\n\rbusiness_name\x18\x02 \x01(\tR\rbusiness_name\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1e\n\ncreated_by\x18\x05 \x01(\tR\ncreated_by\x12\x1e\n\nis_deleted\x18\x0c \x01(\x08R\nis_deleted\x12:\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreated_at\x12:\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdated_at\x12<\n\x0bupdate_mask\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0bupdate_mask\"O\n\x13PostBusinessRequest\x12\x15\n\rbusiness_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\"\xc9\x01\n\x14PatchBusinessRequest\x12$\n\rbusiness_name\x18\x01 \x01(\tR\rbusiness_name\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12&\n\x0b\x62usiness_id\x18\x04 \x01(\tB\x04\xb8\xb7\x18\x01R\x0b\x62usiness_id\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x32\n\x0bupdate_mask\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x01-\"0\n\x12GetBusinessRequest\x12\x1a\n\x08\x62usiness\x18\x01 \x01(\tR\x08\x62usiness\"3\n\x15\x44\x65leteBusinessRequest\x12\x1a\n\x08\x62usiness\x18\x01 \x01(\tR\x08\x62usiness\"O\n\x13ListBusinessRequest\x12\x0c\n\x04tags\x18\x01 \x03(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x1c\n\tpage_size\x18\x03 \x01(\x05R\tpage_size\"C\n\x14ListBusinessResponse\x12+\n\x08\x62usiness\x18\x01 \x03(\x0b\x32\x19.begonia.org.sdk.Business\"\x18\n\x16\x44\x65leteBusinessResponse2\xed\x04\n\x0f\x42usinessService\x12\x63\n\x03\x41\x64\x64\x12$.begonia.org.sdk.PostBusinessRequest\x1a\x19.begonia.org.sdk.Business\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/api/v1/business:\x01*\x12u\n\x06Update\x12%.begonia.org.sdk.PatchBusinessRequest\x1a\x19.begonia.org.sdk.Business\")\x82\xd3\xe4\x93\x02#\x1a\x1e/api/v1/business/{business_id}:\x01*\x12j\n\x03Get\x12#.begonia.org.sdk.GetBusinessRequest\x1a\x19.begonia.org.sdk.Business\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/api/v1/business/{business}\x12~\n\x06\x44\x65lete\x12&.begonia.org.sdk.DeleteBusinessRequest\x1a\'.begonia.org.sdk.DeleteBusinessResponse\"#\x82\xd3\xe4\x93\x02\x1d*\x1b/api/v1/business/{business}\x12m\n\x04List\x12$.begonia.org.sdk.ListBusinessRequest\x1a%.begonia.org.sdk.ListBusinessResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/api/v1/business\x1a#\x88\xb7\x18\x01\xb2\xb7\x18\x1b\x62\x65gonia.api.v1.HttpResponseB+Z)github.com/begonia-org/go-sdk/api/user/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'business_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/begonia-org/go-sdk/api/user/v1'
  _globals['_PATCHBUSINESSREQUEST'].fields_by_name['business_id']._options = None
  _globals['_PATCHBUSINESSREQUEST'].fields_by_name['business_id']._serialized_options = b'\270\267\030\001'
  _globals['_BUSINESSSERVICE']._options = None
  _globals['_BUSINESSSERVICE']._serialized_options = b'\210\267\030\001\262\267\030\033begonia.api.v1.HttpResponse'
  _globals['_BUSINESSSERVICE'].methods_by_name['Add']._options = None
  _globals['_BUSINESSSERVICE'].methods_by_name['Add']._serialized_options = b'\202\323\344\223\002\025\"\020/api/v1/business:\001*'
  _globals['_BUSINESSSERVICE'].methods_by_name['Update']._options = None
  _globals['_BUSINESSSERVICE'].methods_by_name['Update']._serialized_options = b'\202\323\344\223\002#\032\036/api/v1/business/{business_id}:\001*'
  _globals['_BUSINESSSERVICE'].methods_by_name['Get']._options = None
  _globals['_BUSINESSSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\035\022\033/api/v1/business/{business}'
  _globals['_BUSINESSSERVICE'].methods_by_name['Delete']._options = None
  _globals['_BUSINESSSERVICE'].methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\035*\033/api/v1/business/{business}'
  _globals['_BUSINESSSERVICE'].methods_by_name['List']._options = None
  _globals['_BUSINESSSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\022\022\020/api/v1/business'
  _globals['_BUSINESS']._serialized_start=163
  _globals['_BUSINESS']._serialized_end=526
  _globals['_POSTBUSINESSREQUEST']._serialized_start=528
  _globals['_POSTBUSINESSREQUEST']._serialized_end=607
  _globals['_PATCHBUSINESSREQUEST']._serialized_start=610
  _globals['_PATCHBUSINESSREQUEST']._serialized_end=811
  _globals['_GETBUSINESSREQUEST']._serialized_start=813
  _globals['_GETBUSINESSREQUEST']._serialized_end=861
  _globals['_DELETEBUSINESSREQUEST']._serialized_start=863
  _globals['_DELETEBUSINESSREQUEST']._serialized_end=914
  _globals['_LISTBUSINESSREQUEST']._serialized_start=916
  _globals['_LISTBUSINESSREQUEST']._serialized_end=995
  _globals['_LISTBUSINESSRESPONSE']._serialized_start=997
  _globals['_LISTBUSINESSRESPONSE']._serialized_end=1064
  _globals['_DELETEBUSINESSRESPONSE']._serialized_start=1066
  _globals['_DELETEBUSINESSRESPONSE']._serialized_end=1090
  _globals['_BUSINESSSERVICE']._serialized_start=1093
  _globals['_BUSINESSSERVICE']._serialized_end=1714
# @@protoc_insertion_point(module_scope)
