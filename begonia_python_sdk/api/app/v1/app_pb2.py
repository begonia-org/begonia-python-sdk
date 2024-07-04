# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from begonia_python_sdk.api.common.v1 import options_pb2 as common_dot_options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapp.proto\x12\x0f\x62\x65gonia.org.sdk\x1a google/protobuf/descriptor.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14\x63ommon/options.proto\"\xa7\x03\n\x04\x41pps\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12*\n\x06status\x18\x04 \x01(\x0e\x32\x1a.begonia.org.sdk.APPStatus\x12\r\n\x05\x61ppid\x18\x05 \x01(\t\x12\x1e\n\naccess_key\x18\x06 \x01(\tR\naccess_key\x12\x0e\n\x06secret\x18\x07 \x01(\t\x12\r\n\x05owner\x18\x08 \x01(\t\x12\x12\n\npermission\x18\x0b \x01(\x05\x12\x1e\n\nis_deleted\x18\t \x01(\x08R\nis_deleted\x12\x0c\n\x04tags\x18\n \x03(\t\x12:\n\ncreated_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreated_at\x12:\n\nupdated_at\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdated_at\x12<\n\x0bupdate_mask\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0bupdate_mask\"C\n\x10\x43reateAppRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x08 \x03(\t\"V\n\x0e\x41\x64\x64\x41ppResponse\x12\x14\n\x05\x61ppid\x18\x01 \x01(\tR\x05\x61ppid\x12\x1e\n\naccess_key\x18\x02 \x01(\tR\naccess_key\x12\x0e\n\x06secret\x18\x03 \x01(\t\"!\n\x10\x44\x65leteAppRequest\x12\r\n\x05\x61ppid\x18\x01 \x01(\t\"\x13\n\x11\x44\x65leteAppResponse\"\x8b\x01\n\x0b\x41ppsRequest\x12\x1a\n\x05\x61ppid\x18\x06 \x01(\tB\x04\xb8\xb7\x18\x01R\x05\x61ppid\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04tags\x18\x08 \x03(\t\x12/\n\x0bupdate_mask\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x1e\n\rGetAPPRequest\x12\r\n\x05\x61ppid\x18\x01 \x01(\t\"l\n\x0f\x41ppsListRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x0c\n\x04tags\x18\x03 \x03(\t\x12*\n\x06status\x18\x08 \x03(\x0e\x32\x1a.begonia.org.sdk.APPStatus\"F\n\x10\x41ppsListResponse\x12#\n\x04\x61pps\x18\x01 \x03(\x0b\x32\x15.begonia.org.sdk.Apps\x12\r\n\x05total\x18\x02 \x01(\x05*.\n\tAPPStatus\x12\x0f\n\x0b\x41PP_ENABLED\x10\x00\x12\x10\n\x0c\x41PP_DISABLED\x10\x01*I\n\rAPPPremission\x12\x0c\n\x08\x41PP_READ\x10\x00\x12\r\n\tAPP_WRITE\x10\x01\x12\x0e\n\nAPP_DELETE\x10\x02\x12\x0b\n\x07\x41PP_ALL\x10\x03*\x9d\x03\n\nAPPSvrCode\x12\x0f\n\x0b\x41PP_UNKNOWN\x10\x00\x12)\n\x0e\x41PP_CREATE_ERR\x10\xed\'\x1a\x14\xa2\xb7\x18\x10\x63reate app error\x12.\n\x11\x41PP_DUPLICATE_ERR\x10\xee\'\x1a\x16\xa2\xb7\x18\x12\x64uplicate app name\x12/\n\x11\x41PP_SIGNATURE_ERR\x10\xef\'\x1a\x17\xa2\xb7\x18\x13\x61pp signature error\x12\x31\n\x17\x41PP_REQUEST_EXPIRED_ERR\x10\xf0\'\x1a\x13\xa2\xb7\x18\x0frequest expired\x12\x37\n\x1a\x41PP_ACCESS_KEY_MISSING_ERR\x10\xf1\'\x1a\x16\xa2\xb7\x18\x12missing access key\x12+\n\x14\x41PP_AUTH_MISSING_ERR\x10\xf2\'\x1a\x10\xa2\xb7\x18\x0cmissing auth\x12.\n\x15\x41PP_XDATE_MISSING_ERR\x10\xf3\'\x1a\x12\xa2\xb7\x18\x0emissing x-date\x12)\n\x11\x41PP_NOT_FOUND_ERR\x10\xf4\'\x1a\x11\xa2\xb7\x18\rapp not found2\xa7\x04\n\x0b\x41ppsService\x12^\n\x04Post\x12\x1c.begonia.org.sdk.AppsRequest\x1a\x1f.begonia.org.sdk.AddAppResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/api/v1/apps:\x01*\x12V\n\x06Update\x12\x1c.begonia.org.sdk.AppsRequest\x1a\x15.begonia.org.sdk.Apps\"\x17\x82\xd3\xe4\x93\x02\x11\x1a\x0c/api/v1/apps:\x01*\x12Z\n\x03Get\x12\x1e.begonia.org.sdk.GetAPPRequest\x1a\x15.begonia.org.sdk.Apps\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/api/v1/apps/{appid}\x12m\n\x06\x44\x65lete\x12!.begonia.org.sdk.DeleteAppRequest\x1a\".begonia.org.sdk.DeleteAppResponse\"\x1c\x82\xd3\xe4\x93\x02\x16*\x14/api/v1/apps/{appid}\x12\x61\n\x04List\x12 .begonia.org.sdk.AppsListRequest\x1a!.begonia.org.sdk.AppsListResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/api/v1/apps\x1a\x32\x88\xb7\x18\x01\xb2\xb7\x18*begonia.org.sdk.common.api.v1.HttpResponseB*Z(github.com/begonia-org/go-sdk/api/app/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z(github.com/begonia-org/go-sdk/api/app/v1'
  _globals['_APPSVRCODE'].values_by_name["APP_CREATE_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_CREATE_ERR"]._serialized_options = b'\242\267\030\020create app error'
  _globals['_APPSVRCODE'].values_by_name["APP_DUPLICATE_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_DUPLICATE_ERR"]._serialized_options = b'\242\267\030\022duplicate app name'
  _globals['_APPSVRCODE'].values_by_name["APP_SIGNATURE_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_SIGNATURE_ERR"]._serialized_options = b'\242\267\030\023app signature error'
  _globals['_APPSVRCODE'].values_by_name["APP_REQUEST_EXPIRED_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_REQUEST_EXPIRED_ERR"]._serialized_options = b'\242\267\030\017request expired'
  _globals['_APPSVRCODE'].values_by_name["APP_ACCESS_KEY_MISSING_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_ACCESS_KEY_MISSING_ERR"]._serialized_options = b'\242\267\030\022missing access key'
  _globals['_APPSVRCODE'].values_by_name["APP_AUTH_MISSING_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_AUTH_MISSING_ERR"]._serialized_options = b'\242\267\030\014missing auth'
  _globals['_APPSVRCODE'].values_by_name["APP_XDATE_MISSING_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_XDATE_MISSING_ERR"]._serialized_options = b'\242\267\030\016missing x-date'
  _globals['_APPSVRCODE'].values_by_name["APP_NOT_FOUND_ERR"]._options = None
  _globals['_APPSVRCODE'].values_by_name["APP_NOT_FOUND_ERR"]._serialized_options = b'\242\267\030\rapp not found'
  _globals['_APPSREQUEST'].fields_by_name['appid']._options = None
  _globals['_APPSREQUEST'].fields_by_name['appid']._serialized_options = b'\270\267\030\001'
  _globals['_APPSSERVICE']._options = None
  _globals['_APPSSERVICE']._serialized_options = b'\210\267\030\001\262\267\030*begonia.org.sdk.common.api.v1.HttpResponse'
  _globals['_APPSSERVICE'].methods_by_name['Post']._options = None
  _globals['_APPSSERVICE'].methods_by_name['Post']._serialized_options = b'\202\323\344\223\002\021\"\014/api/v1/apps:\001*'
  _globals['_APPSSERVICE'].methods_by_name['Update']._options = None
  _globals['_APPSSERVICE'].methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\021\032\014/api/v1/apps:\001*'
  _globals['_APPSSERVICE'].methods_by_name['Get']._options = None
  _globals['_APPSSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\026\022\024/api/v1/apps/{appid}'
  _globals['_APPSSERVICE'].methods_by_name['Delete']._options = None
  _globals['_APPSSERVICE'].methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\026*\024/api/v1/apps/{appid}'
  _globals['_APPSSERVICE'].methods_by_name['List']._options = None
  _globals['_APPSSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\016\022\014/api/v1/apps'
  _globals['_APPSTATUS']._serialized_start=1178
  _globals['_APPSTATUS']._serialized_end=1224
  _globals['_APPPREMISSION']._serialized_start=1226
  _globals['_APPPREMISSION']._serialized_end=1299
  _globals['_APPSVRCODE']._serialized_start=1302
  _globals['_APPSVRCODE']._serialized_end=1715
  _globals['_APPS']._serialized_start=184
  _globals['_APPS']._serialized_end=607
  _globals['_CREATEAPPREQUEST']._serialized_start=609
  _globals['_CREATEAPPREQUEST']._serialized_end=676
  _globals['_ADDAPPRESPONSE']._serialized_start=678
  _globals['_ADDAPPRESPONSE']._serialized_end=764
  _globals['_DELETEAPPREQUEST']._serialized_start=766
  _globals['_DELETEAPPREQUEST']._serialized_end=799
  _globals['_DELETEAPPRESPONSE']._serialized_start=801
  _globals['_DELETEAPPRESPONSE']._serialized_end=820
  _globals['_APPSREQUEST']._serialized_start=823
  _globals['_APPSREQUEST']._serialized_end=962
  _globals['_GETAPPREQUEST']._serialized_start=964
  _globals['_GETAPPREQUEST']._serialized_end=994
  _globals['_APPSLISTREQUEST']._serialized_start=996
  _globals['_APPSLISTREQUEST']._serialized_end=1104
  _globals['_APPSLISTRESPONSE']._serialized_start=1106
  _globals['_APPSLISTRESPONSE']._serialized_end=1176
  _globals['_APPSSERVICE']._serialized_start=1718
  _globals['_APPSSERVICE']._serialized_end=2269
# @@protoc_insertion_point(module_scope)
