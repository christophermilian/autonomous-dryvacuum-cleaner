# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sensor_msgs/MultiEchoLaserScan.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import std_msgs.msg

class MultiEchoLaserScan(genpy.Message):
  _md5sum = "6fefb0c6da89d7c8abe4b339f5c2f8fb"
  _type = "sensor_msgs/MultiEchoLaserScan"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# Single scan from a multi-echo planar laser range-finder
#
# If you have another ranging device with different behavior (e.g. a sonar
# array), please find or create a different message, since applications
# will make fairly laser-specific assumptions about this data

Header header            # timestamp in the header is the acquisition time of 
                         # the first ray in the scan.
                         #
                         # in frame frame_id, angles are measured around 
                         # the positive Z axis (counterclockwise, if Z is up)
                         # with zero angle being forward along the x axis
                         
float32 angle_min        # start angle of the scan [rad]
float32 angle_max        # end angle of the scan [rad]
float32 angle_increment  # angular distance between measurements [rad]

float32 time_increment   # time between measurements [seconds] - if your scanner
                         # is moving, this will be used in interpolating position
                         # of 3d points
float32 scan_time        # time between scans [seconds]

float32 range_min        # minimum range value [m]
float32 range_max        # maximum range value [m]

LaserEcho[] ranges       # range data [m] (Note: NaNs, values < range_min or > range_max should be discarded)
                         # +Inf measurements are out of range
                         # -Inf measurements are too close to determine exact distance.
LaserEcho[] intensities  # intensity data [device-specific units].  If your
                         # device does not provide intensities, please leave
                         # the array empty.
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/LaserEcho
# This message is a submessage of MultiEchoLaserScan and is not intended
# to be used separately.

float32[] echoes  # Multiple values of ranges or intensities.
                  # Each array represents data from the same angle increment."""
  __slots__ = ['header','angle_min','angle_max','angle_increment','time_increment','scan_time','range_min','range_max','ranges','intensities']
  _slot_types = ['std_msgs/Header','float32','float32','float32','float32','float32','float32','float32','sensor_msgs/LaserEcho[]','sensor_msgs/LaserEcho[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,angle_min,angle_max,angle_increment,time_increment,scan_time,range_min,range_max,ranges,intensities

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MultiEchoLaserScan, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.angle_min is None:
        self.angle_min = 0.
      if self.angle_max is None:
        self.angle_max = 0.
      if self.angle_increment is None:
        self.angle_increment = 0.
      if self.time_increment is None:
        self.time_increment = 0.
      if self.scan_time is None:
        self.scan_time = 0.
      if self.range_min is None:
        self.range_min = 0.
      if self.range_max is None:
        self.range_max = 0.
      if self.ranges is None:
        self.ranges = []
      if self.intensities is None:
        self.intensities = []
    else:
      self.header = std_msgs.msg.Header()
      self.angle_min = 0.
      self.angle_max = 0.
      self.angle_increment = 0.
      self.time_increment = 0.
      self.scan_time = 0.
      self.range_min = 0.
      self.range_max = 0.
      self.ranges = []
      self.intensities = []

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7f().pack(_x.angle_min, _x.angle_max, _x.angle_increment, _x.time_increment, _x.scan_time, _x.range_min, _x.range_max))
      length = len(self.ranges)
      buff.write(_struct_I.pack(length))
      for val1 in self.ranges:
        length = len(val1.echoes)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.echoes))
      length = len(self.intensities)
      buff.write(_struct_I.pack(length))
      for val1 in self.intensities:
        length = len(val1.echoes)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.Struct(pattern).pack(*val1.echoes))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.ranges is None:
        self.ranges = None
      if self.intensities is None:
        self.intensities = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.angle_min, _x.angle_max, _x.angle_increment, _x.time_increment, _x.scan_time, _x.range_min, _x.range_max,) = _get_struct_7f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ranges = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.LaserEcho()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.echoes = s.unpack(str[start:end])
        self.ranges.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.intensities = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.LaserEcho()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.echoes = s.unpack(str[start:end])
        self.intensities.append(val1)
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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7f().pack(_x.angle_min, _x.angle_max, _x.angle_increment, _x.time_increment, _x.scan_time, _x.range_min, _x.range_max))
      length = len(self.ranges)
      buff.write(_struct_I.pack(length))
      for val1 in self.ranges:
        length = len(val1.echoes)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.echoes.tostring())
      length = len(self.intensities)
      buff.write(_struct_I.pack(length))
      for val1 in self.intensities:
        length = len(val1.echoes)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.echoes.tostring())
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.ranges is None:
        self.ranges = None
      if self.intensities is None:
        self.intensities = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.angle_min, _x.angle_max, _x.angle_increment, _x.time_increment, _x.scan_time, _x.range_min, _x.range_max,) = _get_struct_7f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ranges = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.LaserEcho()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.echoes = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.ranges.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.intensities = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.LaserEcho()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.echoes = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.intensities.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7f = None
def _get_struct_7f():
    global _struct_7f
    if _struct_7f is None:
        _struct_7f = struct.Struct("<7f")
    return _struct_7f
