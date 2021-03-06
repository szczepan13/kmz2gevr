# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gevrplace.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gevrplace.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0fgevrplace.proto\"\xe3\x07\n\tGEVRPlace\x12#\n\x07summary\x18\x01 \x02(\x0b\x32\x12.GEVRPlace.Summary\x12!\n\x06places\x18\x02 \x02(\x0b\x32\x11.GEVRPlace.Places\x1av\n\x07Summary\x12\x10\n\x08location\x18\x01 \x03(\t\x12\x11\n\tcopyright\x18\x02 \x02(\t\x12\x10\n\x08unknown1\x18\x03 \x02(\x05\x12\x10\n\x08unknown2\x18\x04 \x02(\x05\x12\x10\n\x08unknown3\x18\x05 \x02(\x05\x12\x10\n\x08unknown4\x18\x06 \x02(\x05\x1a\x95\x06\n\x06Places\x12+\n\nsavedPlace\x18\x01 \x02(\x0b\x32\x17.GEVRPlace.Places.Place\x1a\xdd\x05\n\x05Place\x12\r\n\x05Title\x18\x01 \x02(\t\x12\x10\n\x08SubTitle\x18\x02 \x02(\t\x12\x32\n\x08location\x18\x03 \x02(\x0b\x32 .GEVRPlace.Places.Place.Location\x12/\n\x04time\x18\x04 \x02(\x0b\x32!.GEVRPlace.Places.Place.TimeStamp\x1a\xe8\x03\n\x08Location\x12\x38\n\x07latLong\x18\x01 \x02(\x0b\x32\'.GEVRPlace.Places.Place.Location.LatLon\x12=\n\tpicParams\x18\x02 \x02(\x0b\x32*.GEVRPlace.Places.Place.Location.PicParams\x12\x0f\n\x07heading\x18\x03 \x02(\x01\x12;\n\x08viewMode\x18\x04 \x02(\x0e\x32).GEVRPlace.Places.Place.Location.ViewMode\x12\x11\n\televation\x18\x05 \x02(\x01\x12;\n\x08unknown3\x18\x06 \x02(\x0e\x32).GEVRPlace.Places.Place.Location.ViewMode\x1a\x37\n\x06LatLon\x12\x0b\n\x03lat\x18\x01 \x02(\x01\x12\x0b\n\x03lon\x18\x02 \x02(\x01\x12\x13\n\x0b\x65\x61rthRadius\x18\x03 \x02(\x01\x1a?\n\tPicParams\x12\x0c\n\x04roll\x18\x01 \x02(\x01\x12\x15\n\rweirdAltitude\x18\x02 \x02(\x01\x12\r\n\x05pitch\x18\x03 \x02(\x01\"K\n\x08ViewMode\x12\x0c\n\x08UNKNOWN0\x10\x00\x12\x0c\n\x08UNKNOWN1\x10\x01\x12\x12\n\x0e\x45\x41RTH_IN_FRONT\x10\x02\x12\x0f\n\x0b\x45\x41RTH_BELOW\x10\x03\x1a\x63\n\tTimeStamp\x12\x0c\n\x04year\x18\x01 \x02(\x05\x12\r\n\x05month\x18\x02 \x02(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x02(\x05\x12\x0c\n\x04hour\x18\x04 \x02(\x05\x12\x0e\n\x06minute\x18\x05 \x02(\x05\x12\x0e\n\x06second\x18\x06 \x02(\x05')
)



_GEVRPLACE_PLACES_PLACE_LOCATION_VIEWMODE = _descriptor.EnumDescriptor(
  name='ViewMode',
  full_name='GEVRPlace.Places.Place.Location.ViewMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EARTH_IN_FRONT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EARTH_BELOW', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=839,
  serialized_end=914,
)
_sym_db.RegisterEnumDescriptor(_GEVRPLACE_PLACES_PLACE_LOCATION_VIEWMODE)


_GEVRPLACE_SUMMARY = _descriptor.Descriptor(
  name='Summary',
  full_name='GEVRPlace.Summary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='GEVRPlace.Summary.location', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='copyright', full_name='GEVRPlace.Summary.copyright', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='GEVRPlace.Summary.unknown1', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='GEVRPlace.Summary.unknown2', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unknown3', full_name='GEVRPlace.Summary.unknown3', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unknown4', full_name='GEVRPlace.Summary.unknown4', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=223,
)

_GEVRPLACE_PLACES_PLACE_LOCATION_LATLON = _descriptor.Descriptor(
  name='LatLon',
  full_name='GEVRPlace.Places.Place.Location.LatLon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='GEVRPlace.Places.Place.Location.LatLon.lat', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lon', full_name='GEVRPlace.Places.Place.Location.LatLon.lon', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='earthRadius', full_name='GEVRPlace.Places.Place.Location.LatLon.earthRadius', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=717,
  serialized_end=772,
)

_GEVRPLACE_PLACES_PLACE_LOCATION_PICPARAMS = _descriptor.Descriptor(
  name='PicParams',
  full_name='GEVRPlace.Places.Place.Location.PicParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roll', full_name='GEVRPlace.Places.Place.Location.PicParams.roll', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weirdAltitude', full_name='GEVRPlace.Places.Place.Location.PicParams.weirdAltitude', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='GEVRPlace.Places.Place.Location.PicParams.pitch', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=837,
)

_GEVRPLACE_PLACES_PLACE_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='GEVRPlace.Places.Place.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latLong', full_name='GEVRPlace.Places.Place.Location.latLong', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='picParams', full_name='GEVRPlace.Places.Place.Location.picParams', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='GEVRPlace.Places.Place.Location.heading', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='viewMode', full_name='GEVRPlace.Places.Place.Location.viewMode', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='GEVRPlace.Places.Place.Location.elevation', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unknown3', full_name='GEVRPlace.Places.Place.Location.unknown3', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GEVRPLACE_PLACES_PLACE_LOCATION_LATLON, _GEVRPLACE_PLACES_PLACE_LOCATION_PICPARAMS, ],
  enum_types=[
    _GEVRPLACE_PLACES_PLACE_LOCATION_VIEWMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=914,
)

_GEVRPLACE_PLACES_PLACE_TIMESTAMP = _descriptor.Descriptor(
  name='TimeStamp',
  full_name='GEVRPlace.Places.Place.TimeStamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='GEVRPlace.Places.Place.TimeStamp.year', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='GEVRPlace.Places.Place.TimeStamp.month', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day', full_name='GEVRPlace.Places.Place.TimeStamp.day', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='GEVRPlace.Places.Place.TimeStamp.hour', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minute', full_name='GEVRPlace.Places.Place.TimeStamp.minute', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second', full_name='GEVRPlace.Places.Place.TimeStamp.second', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=916,
  serialized_end=1015,
)

_GEVRPLACE_PLACES_PLACE = _descriptor.Descriptor(
  name='Place',
  full_name='GEVRPlace.Places.Place',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Title', full_name='GEVRPlace.Places.Place.Title', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SubTitle', full_name='GEVRPlace.Places.Place.SubTitle', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='GEVRPlace.Places.Place.location', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='GEVRPlace.Places.Place.time', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GEVRPLACE_PLACES_PLACE_LOCATION, _GEVRPLACE_PLACES_PLACE_TIMESTAMP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=1015,
)

_GEVRPLACE_PLACES = _descriptor.Descriptor(
  name='Places',
  full_name='GEVRPlace.Places',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='savedPlace', full_name='GEVRPlace.Places.savedPlace', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GEVRPLACE_PLACES_PLACE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=1015,
)

_GEVRPLACE = _descriptor.Descriptor(
  name='GEVRPlace',
  full_name='GEVRPlace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='GEVRPlace.summary', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='places', full_name='GEVRPlace.places', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GEVRPLACE_SUMMARY, _GEVRPLACE_PLACES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=1015,
)

_GEVRPLACE_SUMMARY.containing_type = _GEVRPLACE
_GEVRPLACE_PLACES_PLACE_LOCATION_LATLON.containing_type = _GEVRPLACE_PLACES_PLACE_LOCATION
_GEVRPLACE_PLACES_PLACE_LOCATION_PICPARAMS.containing_type = _GEVRPLACE_PLACES_PLACE_LOCATION
_GEVRPLACE_PLACES_PLACE_LOCATION.fields_by_name['latLong'].message_type = _GEVRPLACE_PLACES_PLACE_LOCATION_LATLON
_GEVRPLACE_PLACES_PLACE_LOCATION.fields_by_name['picParams'].message_type = _GEVRPLACE_PLACES_PLACE_LOCATION_PICPARAMS
_GEVRPLACE_PLACES_PLACE_LOCATION.fields_by_name['viewMode'].enum_type = _GEVRPLACE_PLACES_PLACE_LOCATION_VIEWMODE
_GEVRPLACE_PLACES_PLACE_LOCATION.fields_by_name['unknown3'].enum_type = _GEVRPLACE_PLACES_PLACE_LOCATION_VIEWMODE
_GEVRPLACE_PLACES_PLACE_LOCATION.containing_type = _GEVRPLACE_PLACES_PLACE
_GEVRPLACE_PLACES_PLACE_LOCATION_VIEWMODE.containing_type = _GEVRPLACE_PLACES_PLACE_LOCATION
_GEVRPLACE_PLACES_PLACE_TIMESTAMP.containing_type = _GEVRPLACE_PLACES_PLACE
_GEVRPLACE_PLACES_PLACE.fields_by_name['location'].message_type = _GEVRPLACE_PLACES_PLACE_LOCATION
_GEVRPLACE_PLACES_PLACE.fields_by_name['time'].message_type = _GEVRPLACE_PLACES_PLACE_TIMESTAMP
_GEVRPLACE_PLACES_PLACE.containing_type = _GEVRPLACE_PLACES
_GEVRPLACE_PLACES.fields_by_name['savedPlace'].message_type = _GEVRPLACE_PLACES_PLACE
_GEVRPLACE_PLACES.containing_type = _GEVRPLACE
_GEVRPLACE.fields_by_name['summary'].message_type = _GEVRPLACE_SUMMARY
_GEVRPLACE.fields_by_name['places'].message_type = _GEVRPLACE_PLACES
DESCRIPTOR.message_types_by_name['GEVRPlace'] = _GEVRPLACE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GEVRPlace = _reflection.GeneratedProtocolMessageType('GEVRPlace', (_message.Message,), dict(

  Summary = _reflection.GeneratedProtocolMessageType('Summary', (_message.Message,), dict(
    DESCRIPTOR = _GEVRPLACE_SUMMARY,
    __module__ = 'gevrplace_pb2'
    # @@protoc_insertion_point(class_scope:GEVRPlace.Summary)
    ))
  ,

  Places = _reflection.GeneratedProtocolMessageType('Places', (_message.Message,), dict(

    Place = _reflection.GeneratedProtocolMessageType('Place', (_message.Message,), dict(

      Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(

        LatLon = _reflection.GeneratedProtocolMessageType('LatLon', (_message.Message,), dict(
          DESCRIPTOR = _GEVRPLACE_PLACES_PLACE_LOCATION_LATLON,
          __module__ = 'gevrplace_pb2'
          # @@protoc_insertion_point(class_scope:GEVRPlace.Places.Place.Location.LatLon)
          ))
        ,

        PicParams = _reflection.GeneratedProtocolMessageType('PicParams', (_message.Message,), dict(
          DESCRIPTOR = _GEVRPLACE_PLACES_PLACE_LOCATION_PICPARAMS,
          __module__ = 'gevrplace_pb2'
          # @@protoc_insertion_point(class_scope:GEVRPlace.Places.Place.Location.PicParams)
          ))
        ,
        DESCRIPTOR = _GEVRPLACE_PLACES_PLACE_LOCATION,
        __module__ = 'gevrplace_pb2'
        # @@protoc_insertion_point(class_scope:GEVRPlace.Places.Place.Location)
        ))
      ,

      TimeStamp = _reflection.GeneratedProtocolMessageType('TimeStamp', (_message.Message,), dict(
        DESCRIPTOR = _GEVRPLACE_PLACES_PLACE_TIMESTAMP,
        __module__ = 'gevrplace_pb2'
        # @@protoc_insertion_point(class_scope:GEVRPlace.Places.Place.TimeStamp)
        ))
      ,
      DESCRIPTOR = _GEVRPLACE_PLACES_PLACE,
      __module__ = 'gevrplace_pb2'
      # @@protoc_insertion_point(class_scope:GEVRPlace.Places.Place)
      ))
    ,
    DESCRIPTOR = _GEVRPLACE_PLACES,
    __module__ = 'gevrplace_pb2'
    # @@protoc_insertion_point(class_scope:GEVRPlace.Places)
    ))
  ,
  DESCRIPTOR = _GEVRPLACE,
  __module__ = 'gevrplace_pb2'
  # @@protoc_insertion_point(class_scope:GEVRPlace)
  ))
_sym_db.RegisterMessage(GEVRPlace)
_sym_db.RegisterMessage(GEVRPlace.Summary)
_sym_db.RegisterMessage(GEVRPlace.Places)
_sym_db.RegisterMessage(GEVRPlace.Places.Place)
_sym_db.RegisterMessage(GEVRPlace.Places.Place.Location)
_sym_db.RegisterMessage(GEVRPlace.Places.Place.Location.LatLon)
_sym_db.RegisterMessage(GEVRPlace.Places.Place.Location.PicParams)
_sym_db.RegisterMessage(GEVRPlace.Places.Place.TimeStamp)


# @@protoc_insertion_point(module_scope)
