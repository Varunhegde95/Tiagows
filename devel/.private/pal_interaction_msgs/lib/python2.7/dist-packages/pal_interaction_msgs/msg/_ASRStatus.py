# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pal_interaction_msgs/ASRStatus.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import pal_interaction_msgs.msg

class ASRStatus(genpy.Message):
  _md5sum = "b05e32d6465a052804ec3f6d853dbe61"
  _type = "pal_interaction_msgs/ASRStatus"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# The status of the ASR
# if it is active then active=true
bool active

# the current language 
string language

# the current enabled grammar
string enabled_grammar

# the current acoustic models
string acoustic_env

# A description of the audio device the 
# recognizer is taking audio from.
AudioDeviceDescription device

================================================================================
MSG: pal_interaction_msgs/AudioDeviceDescription
# Description of an audio device.

int8 SIGNED = 0
int8 UNSIGNED = 1


# name of the device (usually a portaudio name)
string device_name

# sample rate of the acquired audio signal
uint32 sample_rate

# sample size in bits
int8 sample_size

# format can be SIGNED or UNSIGNED
int8 format

# buffer size used to acquire data.
uint16 buffer_size

# number of recorded channels
int8 number_of_channels"""
  __slots__ = ['active','language','enabled_grammar','acoustic_env','device']
  _slot_types = ['bool','string','string','string','pal_interaction_msgs/AudioDeviceDescription']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       active,language,enabled_grammar,acoustic_env,device

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ASRStatus, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.active is None:
        self.active = False
      if self.language is None:
        self.language = ''
      if self.enabled_grammar is None:
        self.enabled_grammar = ''
      if self.acoustic_env is None:
        self.acoustic_env = ''
      if self.device is None:
        self.device = pal_interaction_msgs.msg.AudioDeviceDescription()
    else:
      self.active = False
      self.language = ''
      self.enabled_grammar = ''
      self.acoustic_env = ''
      self.device = pal_interaction_msgs.msg.AudioDeviceDescription()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.active
      buff.write(_get_struct_B().pack(_x))
      _x = self.language
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.enabled_grammar
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.acoustic_env
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.device.device_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I2bHb().pack(_x.device.sample_rate, _x.device.sample_size, _x.device.format, _x.device.buffer_size, _x.device.number_of_channels))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.device is None:
        self.device = pal_interaction_msgs.msg.AudioDeviceDescription()
      end = 0
      start = end
      end += 1
      (self.active,) = _get_struct_B().unpack(str[start:end])
      self.active = bool(self.active)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.language = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.language = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.enabled_grammar = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.enabled_grammar = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.acoustic_env = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.acoustic_env = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.device.device_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.device.device_name = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.device.sample_rate, _x.device.sample_size, _x.device.format, _x.device.buffer_size, _x.device.number_of_channels,) = _get_struct_I2bHb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.active
      buff.write(_get_struct_B().pack(_x))
      _x = self.language
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.enabled_grammar
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.acoustic_env
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.device.device_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I2bHb().pack(_x.device.sample_rate, _x.device.sample_size, _x.device.format, _x.device.buffer_size, _x.device.number_of_channels))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.device is None:
        self.device = pal_interaction_msgs.msg.AudioDeviceDescription()
      end = 0
      start = end
      end += 1
      (self.active,) = _get_struct_B().unpack(str[start:end])
      self.active = bool(self.active)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.language = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.language = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.enabled_grammar = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.enabled_grammar = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.acoustic_env = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.acoustic_env = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.device.device_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.device.device_name = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.device.sample_rate, _x.device.sample_size, _x.device.format, _x.device.buffer_size, _x.device.number_of_channels,) = _get_struct_I2bHb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_I2bHb = None
def _get_struct_I2bHb():
    global _struct_I2bHb
    if _struct_I2bHb is None:
        _struct_I2bHb = struct.Struct("<I2bHb")
    return _struct_I2bHb
