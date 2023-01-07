# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wordservice.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wordservice.proto',
  package='endpoints.word_service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11wordservice.proto\x12\x16\x65ndpoints.word_service\"\xb2\x01\n\x0eWordDefinition\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\ndefinition\x18\x02 \x01(\t\x12\x0b\n\x03pos\x18\x03 \x01(\t\x12\x10\n\x08\x65xamples\x18\x04 \x03(\t\x12\x11\n\tsyllables\x18\x05 \x03(\t\x12\x16\n\x0eprobablyExists\x18\x06 \x01(\x08\x12\x34\n\x07\x64\x61taset\x18\x07 \x01(\x0e\x32#.endpoints.word_service.DatasetType\"W\n\x11\x44\x65\x66ineWordRequest\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x34\n\x07\x64\x61taset\x18\x02 \x01(\x0e\x32#.endpoints.word_service.DatasetType\"J\n\x12\x44\x65\x66ineWordResponse\x12\x34\n\x04word\x18\x01 \x01(\x0b\x32&.endpoints.word_service.WordDefinition\"/\n\x19WordFromDefinitionRequest\x12\x12\n\ndefinition\x18\x01 \x01(\t\"R\n\x1aWordFromDefinitionResponse\x12\x34\n\x04word\x18\x01 \x01(\x0b\x32&.endpoints.word_service.WordDefinition\"\x15\n\x13GenerateWordRequest\"L\n\x14GenerateWordResponse\x12\x34\n\x04word\x18\x01 \x01(\x0b\x32&.endpoints.word_service.WordDefinition*:\n\x0b\x44\x61tasetType\x12\x07\n\x03OED\x10\x00\x12\x0f\n\x0bUD_FILTERED\x10\x01\x12\x11\n\rUD_UNFILTERED\x10\x02\x32\xe0\x02\n\x0bWordService\x12\x65\n\nDefineWord\x12).endpoints.word_service.DefineWordRequest\x1a*.endpoints.word_service.DefineWordResponse\"\x00\x12}\n\x12WordFromDefinition\x12\x31.endpoints.word_service.WordFromDefinitionRequest\x1a\x32.endpoints.word_service.WordFromDefinitionResponse\"\x00\x12k\n\x0cGenerateWord\x12+.endpoints.word_service.GenerateWordRequest\x1a,.endpoints.word_service.GenerateWordResponse\"\x00\x62\x06proto3')
)

_DATASETTYPE = _descriptor.EnumDescriptor(
  name='DatasetType',
  full_name='endpoints.word_service.DatasetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UD_FILTERED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UD_UNFILTERED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=625,
  serialized_end=683,
)
_sym_db.RegisterEnumDescriptor(_DATASETTYPE)

DatasetType = enum_type_wrapper.EnumTypeWrapper(_DATASETTYPE)
OED = 0
UD_FILTERED = 1
UD_UNFILTERED = 2



_WORDDEFINITION = _descriptor.Descriptor(
  name='WordDefinition',
  full_name='endpoints.word_service.WordDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.WordDefinition.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='definition', full_name='endpoints.word_service.WordDefinition.definition', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='endpoints.word_service.WordDefinition.pos', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examples', full_name='endpoints.word_service.WordDefinition.examples', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='syllables', full_name='endpoints.word_service.WordDefinition.syllables', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='probablyExists', full_name='endpoints.word_service.WordDefinition.probablyExists', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='endpoints.word_service.WordDefinition.dataset', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=224,
)


_DEFINEWORDREQUEST = _descriptor.Descriptor(
  name='DefineWordRequest',
  full_name='endpoints.word_service.DefineWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.DefineWordRequest.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='endpoints.word_service.DefineWordRequest.dataset', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=313,
)


_DEFINEWORDRESPONSE = _descriptor.Descriptor(
  name='DefineWordResponse',
  full_name='endpoints.word_service.DefineWordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.DefineWordResponse.word', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=389,
)


_WORDFROMDEFINITIONREQUEST = _descriptor.Descriptor(
  name='WordFromDefinitionRequest',
  full_name='endpoints.word_service.WordFromDefinitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='definition', full_name='endpoints.word_service.WordFromDefinitionRequest.definition', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=438,
)


_WORDFROMDEFINITIONRESPONSE = _descriptor.Descriptor(
  name='WordFromDefinitionResponse',
  full_name='endpoints.word_service.WordFromDefinitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.WordFromDefinitionResponse.word', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=440,
  serialized_end=522,
)


_GENERATEWORDREQUEST = _descriptor.Descriptor(
  name='GenerateWordRequest',
  full_name='endpoints.word_service.GenerateWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=545,
)


_GENERATEWORDRESPONSE = _descriptor.Descriptor(
  name='GenerateWordResponse',
  full_name='endpoints.word_service.GenerateWordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='endpoints.word_service.GenerateWordResponse.word', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=623,
)

_WORDDEFINITION.fields_by_name['dataset'].enum_type = _DATASETTYPE
_DEFINEWORDREQUEST.fields_by_name['dataset'].enum_type = _DATASETTYPE
_DEFINEWORDRESPONSE.fields_by_name['word'].message_type = _WORDDEFINITION
_WORDFROMDEFINITIONRESPONSE.fields_by_name['word'].message_type = _WORDDEFINITION
_GENERATEWORDRESPONSE.fields_by_name['word'].message_type = _WORDDEFINITION
DESCRIPTOR.message_types_by_name['WordDefinition'] = _WORDDEFINITION
DESCRIPTOR.message_types_by_name['DefineWordRequest'] = _DEFINEWORDREQUEST
DESCRIPTOR.message_types_by_name['DefineWordResponse'] = _DEFINEWORDRESPONSE
DESCRIPTOR.message_types_by_name['WordFromDefinitionRequest'] = _WORDFROMDEFINITIONREQUEST
DESCRIPTOR.message_types_by_name['WordFromDefinitionResponse'] = _WORDFROMDEFINITIONRESPONSE
DESCRIPTOR.message_types_by_name['GenerateWordRequest'] = _GENERATEWORDREQUEST
DESCRIPTOR.message_types_by_name['GenerateWordResponse'] = _GENERATEWORDRESPONSE
DESCRIPTOR.enum_types_by_name['DatasetType'] = _DATASETTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WordDefinition = _reflection.GeneratedProtocolMessageType('WordDefinition', (_message.Message,), dict(
  DESCRIPTOR = _WORDDEFINITION,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.WordDefinition)
  ))
_sym_db.RegisterMessage(WordDefinition)

DefineWordRequest = _reflection.GeneratedProtocolMessageType('DefineWordRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEFINEWORDREQUEST,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.DefineWordRequest)
  ))
_sym_db.RegisterMessage(DefineWordRequest)

DefineWordResponse = _reflection.GeneratedProtocolMessageType('DefineWordResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEFINEWORDRESPONSE,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.DefineWordResponse)
  ))
_sym_db.RegisterMessage(DefineWordResponse)

WordFromDefinitionRequest = _reflection.GeneratedProtocolMessageType('WordFromDefinitionRequest', (_message.Message,), dict(
  DESCRIPTOR = _WORDFROMDEFINITIONREQUEST,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.WordFromDefinitionRequest)
  ))
_sym_db.RegisterMessage(WordFromDefinitionRequest)

WordFromDefinitionResponse = _reflection.GeneratedProtocolMessageType('WordFromDefinitionResponse', (_message.Message,), dict(
  DESCRIPTOR = _WORDFROMDEFINITIONRESPONSE,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.WordFromDefinitionResponse)
  ))
_sym_db.RegisterMessage(WordFromDefinitionResponse)

GenerateWordRequest = _reflection.GeneratedProtocolMessageType('GenerateWordRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERATEWORDREQUEST,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.GenerateWordRequest)
  ))
_sym_db.RegisterMessage(GenerateWordRequest)

GenerateWordResponse = _reflection.GeneratedProtocolMessageType('GenerateWordResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERATEWORDRESPONSE,
  __module__ = 'wordservice_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.word_service.GenerateWordResponse)
  ))
_sym_db.RegisterMessage(GenerateWordResponse)



_WORDSERVICE = _descriptor.ServiceDescriptor(
  name='WordService',
  full_name='endpoints.word_service.WordService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=686,
  serialized_end=1038,
  methods=[
  _descriptor.MethodDescriptor(
    name='DefineWord',
    full_name='endpoints.word_service.WordService.DefineWord',
    index=0,
    containing_service=None,
    input_type=_DEFINEWORDREQUEST,
    output_type=_DEFINEWORDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WordFromDefinition',
    full_name='endpoints.word_service.WordService.WordFromDefinition',
    index=1,
    containing_service=None,
    input_type=_WORDFROMDEFINITIONREQUEST,
    output_type=_WORDFROMDEFINITIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateWord',
    full_name='endpoints.word_service.WordService.GenerateWord',
    index=2,
    containing_service=None,
    input_type=_GENERATEWORDREQUEST,
    output_type=_GENERATEWORDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORDSERVICE)

DESCRIPTOR.services_by_name['WordService'] = _WORDSERVICE

# @@protoc_insertion_point(module_scope)
