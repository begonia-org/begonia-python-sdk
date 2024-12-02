# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from begonia.api.v1 import options_pb2 as begonia_dot_api_dot_v1_dot_options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a google/protobuf/descriptor.proto\x1a\x19google/api/httpbody.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1c\x62\x65gonia/api/v1/options.proto\")\n\x0c\x45rrorRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\")\n\x0cHelloRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xc9\x01\n\x0fHelloSubRequest\x12\x18\n\x07sub_msg\x18\x01 \x01(\tR\x07sub_msg\x12(\n\x08sub_name\x18\x02 \x01(\tB\x0c\xc2\xb7\x18\x08requiredR\x08sub_name\x12\x34\n\x07sub_age\x18\x04 \x01(\x05\x42\x1a\xc2\xb7\x18\x16required,gte=18,lte=35R\x07sub_age\x12<\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0bupdate_mask\"\xd1\n\n\x19HelloRequestWithValidator\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x03\x61ge\x18\x03 \x01(\x05\x42\x1a\xc2\xb7\x18\x16required,gte=18,lte=35\x12(\n\x04\x61ge2\x18\x0f \x01(\x04\x42\x1a\xc2\xb7\x18\x16required,gte=18,lte=35\x12\x1f\n\tfloat_num\x18\x10 \x01(\x01\x42\x0c\xc2\xb7\x18\x08required\x12*\n\tbool_data\x18\x11 \x01(\x08\x42\x0c\xc2\xb7\x18\x08requiredR\tbool_data\x12,\n\nbytes_data\x18\x12 \x01(\x0c\x42\x0c\xc2\xb7\x18\x08requiredR\nbytes_data\x12\x36\n\x03sub\x18\x04 \x01(\x0b\x32\x1b.helloworld.HelloSubRequestB\x0c\xc2\xb7\x18\x08required\x12\x42\n\x04sub2\x18\x0e \x01(\x0b\x32\x18.helloworld.HelloRequestB\x1a\xc2\xb7\x18\x16required_if=Name hello\x12\x42\n\x04subs\x18\x05 \x03(\x0b\x32\x1b.helloworld.HelloSubRequestB\x11\xc2\xb7\x18\rrequired,diveR\x04subs\x12<\n\x0bupdate_mask\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0bupdate_mask\x12^\n\x07sub_map\x18\x07 \x03(\x0b\x32\x31.helloworld.HelloRequestWithValidator.SubMapEntryB\x11\xc2\xb7\x18\rrequired,diveR\x07sub_map\x12\x61\n\x08sub_map2\x18\x08 \x03(\x0b\x32\x32.helloworld.HelloRequestWithValidator.SubMap2EntryB\x11\xc2\xb7\x18\rrequired,diveR\x08sub_map2\x12\x66\n\x07\x65x_enum\x18\t \x01(\x0e\x32\x17.helloworld.ExampleEnumB3\xc2\xb7\x18/required,oneof=EX_STARTED EX_RUNNING EX_STOPPEDR\x07\x65x_enum\x12\x41\n\x08\x65x_enums\x18\n \x03(\x0e\x32\x17.helloworld.ExampleEnumB\x0c\xc2\xb7\x18\x08requiredR\x08\x65x_enums\x12 \n\x04strs\x18\x0b \x03(\tB\x0c\xc2\xb7\x18\x08requiredR\x04strs\x12[\n\x08\x65num_map\x18\x0c \x03(\x0b\x32\x32.helloworld.HelloRequestWithValidator.EnumMapEntryB\x0c\xc2\xb7\x18\x08requiredR\x07str_map\x12Q\n\tenum_map2\x18\r \x03(\x0b\x32\x33.helloworld.HelloRequestWithValidator.EnumMap2EntryR\tenum_map2\x1aJ\n\x0bSubMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.helloworld.HelloSubRequest:\x02\x38\x01\x1a.\n\x0cSubMap2Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aG\n\x0c\x45numMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0e\x32\x17.helloworld.ExampleEnum:\x02\x38\x01\x1aH\n\rEnumMap2Entry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0e\x32\x17.helloworld.ExampleEnum:\x02\x38\x01\"+\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"8\n\rRepeatedReply\x12\'\n\x07replies\x18\x01 \x03(\x0b\x32\x16.helloworld.HelloReply\"\x90\x04\n\x0e\x45xampleMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x1c\n\tfloat_num\x18\x03 \x01(\x01R\tfloat_num\x12\x1e\n\nfloat_data\x18\x0e \x01(\x02R\nfloat_data\x12\x1c\n\tbyte_data\x18\x04 \x01(\x0cR\tbyte_data\x12\x1c\n\tbool_data\x18\x05 \x01(\x08R\tbool_data\x12$\n\x05\x61llow\x18\x06 \x01(\x0e\x32\x15.helloworld.EnumAllow\x12$\n\rrepeated_data\x18\x07 \x03(\x03R\rrepeated_data\x12\x1e\n\nfixed_data\x18\x08 \x01(\x06R\nfixed_data\x12 \n\x0bsfixed_data\x18\t \x01(\x10R\x0bsfixed_data\x12$\n\rsfixed32_data\x18\n \x01(\x0fR\rsfixed32_data\x12\"\n\x0c\x66ixed32_data\x18\x0b \x01(\x07R\x0c\x66ixed32_data\x12<\n\x0crepeated_msg\x18\x0c \x03(\x0b\x32\x18.helloworld.HelloRequestR\x0crepeated_msg\x12%\n\x03msg\x18\r \x01(\x0b\x32\x18.helloworld.HelloRequest\x12(\n\x04mask\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x8c\x02\n\x0c\x45xampleTable\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x1e\n\nis_deleted\x18\x0c \x01(\x08R\nis_deleted\x12:\n\ncreated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreated_at\x12:\n\nupdated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdated_at\x12<\n\x0bupdate_mask\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0bupdate_mask*M\n\x0b\x45xampleEnum\x12\x0e\n\nEX_UNKNOWN\x10\x00\x12\x0e\n\nEX_STARTED\x10\x01\x12\x0e\n\nEX_RUNNING\x10\x02\x12\x0e\n\nEX_STOPPED\x10\x03* \n\tEnumAllow\x12\t\n\x05\x41LLOW\x10\x00\x12\x08\n\x04\x44\x45NY\x10\x01\x32\xb9\x06\n\x07Greeter\x12]\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/api/v1/example/post:\x01*\x12\x41\n\x0bSayHelloRPC\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12_\n\x0bSayHelloGet\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/api/v1/example/{name}\x12|\n\x17SayHelloServerSideEvent\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"-\xc8\xb7\x18\x01\x82\xd3\xe4\x93\x02#\x12!/api/v1/example/server/sse/{name}0\x01\x12w\n\x14SayHelloClientStream\x12\x18.helloworld.HelloRequest\x1a\x19.helloworld.RepeatedReply\"(\x82\xd3\xe4\x93\x02\"\"\x1d/api/v1/example/client/stream:\x01*(\x01\x12s\n\x11SayHelloWebsocket\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"(\x82\xd3\xe4\x93\x02\"\x12 /api/v1/example/server/websocket(\x01\x30\x01\x12X\n\x0cSayHelloBody\x12\x14.google.api.HttpBody\x1a\x14.google.api.HttpBody\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x14/api/v1/example/body\x12\x65\n\rSayHelloError\x12\x18.helloworld.ErrorRequest\x1a\x16.helloworld.HelloReply\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/api/v1/example/error/testBe\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01Z-github.com/begonia-org/begonia/example/api/v1\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001Z-github.com/begonia-org/begonia/example/api/v1\242\002\003HLW'
  _globals['_HELLOSUBREQUEST'].fields_by_name['sub_name']._options = None
  _globals['_HELLOSUBREQUEST'].fields_by_name['sub_name']._serialized_options = b'\302\267\030\010required'
  _globals['_HELLOSUBREQUEST'].fields_by_name['sub_age']._options = None
  _globals['_HELLOSUBREQUEST'].fields_by_name['sub_age']._serialized_options = b'\302\267\030\026required,gte=18,lte=35'
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAPENTRY']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAPENTRY']._serialized_options = b'8\001'
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAP2ENTRY']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAP2ENTRY']._serialized_options = b'8\001'
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAPENTRY']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAPENTRY']._serialized_options = b'8\001'
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAP2ENTRY']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAP2ENTRY']._serialized_options = b'8\001'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['age']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['age']._serialized_options = b'\302\267\030\026required,gte=18,lte=35'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['age2']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['age2']._serialized_options = b'\302\267\030\026required,gte=18,lte=35'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['float_num']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['float_num']._serialized_options = b'\302\267\030\010required'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['bool_data']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['bool_data']._serialized_options = b'\302\267\030\010required'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['bytes_data']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['bytes_data']._serialized_options = b'\302\267\030\010required'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub']._serialized_options = b'\302\267\030\010required'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub2']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub2']._serialized_options = b'\302\267\030\026required_if=Name hello'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['subs']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['subs']._serialized_options = b'\302\267\030\rrequired,dive'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub_map']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub_map']._serialized_options = b'\302\267\030\rrequired,dive'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub_map2']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['sub_map2']._serialized_options = b'\302\267\030\rrequired,dive'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['ex_enum']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['ex_enum']._serialized_options = b'\302\267\030/required,oneof=EX_STARTED EX_RUNNING EX_STOPPED'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['ex_enums']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['ex_enums']._serialized_options = b'\302\267\030\010required'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['strs']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['strs']._serialized_options = b'\302\267\030\010required'
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['enum_map']._options = None
  _globals['_HELLOREQUESTWITHVALIDATOR'].fields_by_name['enum_map']._serialized_options = b'\302\267\030\010required'
  _globals['_GREETER'].methods_by_name['SayHello']._options = None
  _globals['_GREETER'].methods_by_name['SayHello']._serialized_options = b'\202\323\344\223\002\031\"\024/api/v1/example/post:\001*'
  _globals['_GREETER'].methods_by_name['SayHelloGet']._options = None
  _globals['_GREETER'].methods_by_name['SayHelloGet']._serialized_options = b'\202\323\344\223\002\030\022\026/api/v1/example/{name}'
  _globals['_GREETER'].methods_by_name['SayHelloServerSideEvent']._options = None
  _globals['_GREETER'].methods_by_name['SayHelloServerSideEvent']._serialized_options = b'\310\267\030\001\202\323\344\223\002#\022!/api/v1/example/server/sse/{name}'
  _globals['_GREETER'].methods_by_name['SayHelloClientStream']._options = None
  _globals['_GREETER'].methods_by_name['SayHelloClientStream']._serialized_options = b'\202\323\344\223\002\"\"\035/api/v1/example/client/stream:\001*'
  _globals['_GREETER'].methods_by_name['SayHelloWebsocket']._options = None
  _globals['_GREETER'].methods_by_name['SayHelloWebsocket']._serialized_options = b'\202\323\344\223\002\"\022 /api/v1/example/server/websocket'
  _globals['_GREETER'].methods_by_name['SayHelloBody']._options = None
  _globals['_GREETER'].methods_by_name['SayHelloBody']._serialized_options = b'\202\323\344\223\002\026\"\024/api/v1/example/body'
  _globals['_GREETER'].methods_by_name['SayHelloError']._options = None
  _globals['_GREETER'].methods_by_name['SayHelloError']._serialized_options = b'\202\323\344\223\002\034\022\032/api/v1/example/error/test'
  _globals['_EXAMPLEENUM']._serialized_start=2779
  _globals['_EXAMPLEENUM']._serialized_end=2856
  _globals['_ENUMALLOW']._serialized_start=2858
  _globals['_ENUMALLOW']._serialized_end=2890
  _globals['_ERRORREQUEST']._serialized_start=220
  _globals['_ERRORREQUEST']._serialized_end=261
  _globals['_HELLOREQUEST']._serialized_start=263
  _globals['_HELLOREQUEST']._serialized_end=304
  _globals['_HELLOSUBREQUEST']._serialized_start=307
  _globals['_HELLOSUBREQUEST']._serialized_end=508
  _globals['_HELLOREQUESTWITHVALIDATOR']._serialized_start=511
  _globals['_HELLOREQUESTWITHVALIDATOR']._serialized_end=1872
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAPENTRY']._serialized_start=1603
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAPENTRY']._serialized_end=1677
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAP2ENTRY']._serialized_start=1679
  _globals['_HELLOREQUESTWITHVALIDATOR_SUBMAP2ENTRY']._serialized_end=1725
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAPENTRY']._serialized_start=1727
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAPENTRY']._serialized_end=1798
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAP2ENTRY']._serialized_start=1800
  _globals['_HELLOREQUESTWITHVALIDATOR_ENUMMAP2ENTRY']._serialized_end=1872
  _globals['_HELLOREPLY']._serialized_start=1874
  _globals['_HELLOREPLY']._serialized_end=1917
  _globals['_REPEATEDREPLY']._serialized_start=1919
  _globals['_REPEATEDREPLY']._serialized_end=1975
  _globals['_EXAMPLEMESSAGE']._serialized_start=1978
  _globals['_EXAMPLEMESSAGE']._serialized_end=2506
  _globals['_EXAMPLETABLE']._serialized_start=2509
  _globals['_EXAMPLETABLE']._serialized_end=2777
  _globals['_GREETER']._serialized_start=2893
  _globals['_GREETER']._serialized_end=3718
# @@protoc_insertion_point(module_scope)