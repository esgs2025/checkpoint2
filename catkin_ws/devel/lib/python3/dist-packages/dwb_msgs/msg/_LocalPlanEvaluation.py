# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from dwb_msgs/LocalPlanEvaluation.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import dwb_msgs.msg
import genpy
import geometry_msgs.msg
import nav_2d_msgs.msg
import std_msgs.msg

class LocalPlanEvaluation(genpy.Message):
  _md5sum = "d360642012ea44ee598913c70498aa4b"
  _type = "dwb_msgs/LocalPlanEvaluation"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# Full Scoring for running the local planner

# Header, used for timestamp
Header header
# All the trajectories evaluated and their scores
TrajectoryScore[] twists
# Convenience index of the best (lowest) score in the twists array
uint16 best_index
# Convenience index of the worst (highest) score in the twists array. Useful for scaling.
uint16 worst_index

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
string frame_id

================================================================================
MSG: dwb_msgs/TrajectoryScore
# Complete scoring for a given twist.

# The trajectory being scored
Trajectory2D traj
# The Scores for each of the critics employed
CriticScore[] scores
# Convenience member that totals the critic scores
float32 total

================================================================================
MSG: dwb_msgs/Trajectory2D
# For a given velocity command, the poses that the robot will go to in the allotted time.

# Input Velocity
nav_2d_msgs/Twist2D velocity

# Poses the robot will go to, given our kinematic model
geometry_msgs/Pose2D[] poses

# Time difference between the current pose and the poses in the trajectory.
# Parallel array to poses. Length should be the same.
duration[] time_offsets

================================================================================
MSG: nav_2d_msgs/Twist2D
float64 x
float64 y
float64 theta

================================================================================
MSG: geometry_msgs/Pose2D
# Deprecated
# Please use the full 3D pose.

# In general our recommendation is to use a full 3D representation of everything and for 2D specific applications make the appropriate projections into the plane for their calculations but optimally will preserve the 3D information during processing.

# If we have parallel copies of 2D datatypes every UI and other pipeline will end up needing to have dual interfaces to plot everything. And you will end up with not being able to use 3D tools for 2D use cases even if they're completely valid, as you'd have to reimplement it with different inputs and outputs. It's not particularly hard to plot the 2D pose or compute the yaw error for the Pose message and there are already tools and libraries that can do this for you.


# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta

================================================================================
MSG: dwb_msgs/CriticScore
# The result from one critic scoring a Twist.
# Name of the critic
string name
# Score for the critic, not multiplied by the scale
float32 raw_score
# Scale for the critic, multiplied by the raw_score and added to the total score
float32 scale
"""
  __slots__ = ['header','twists','best_index','worst_index']
  _slot_types = ['std_msgs/Header','dwb_msgs/TrajectoryScore[]','uint16','uint16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,twists,best_index,worst_index

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LocalPlanEvaluation, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.twists is None:
        self.twists = []
      if self.best_index is None:
        self.best_index = 0
      if self.worst_index is None:
        self.worst_index = 0
    else:
      self.header = std_msgs.msg.Header()
      self.twists = []
      self.best_index = 0
      self.worst_index = 0

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
      length = len(self.twists)
      buff.write(_struct_I.pack(length))
      for val1 in self.twists:
        _v1 = val1.traj
        _v2 = _v1.velocity
        _x = _v2
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.theta))
        length = len(_v1.poses)
        buff.write(_struct_I.pack(length))
        for val3 in _v1.poses:
          _x = val3
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.theta))
        length = len(_v1.time_offsets)
        buff.write(_struct_I.pack(length))
        for val3 in _v1.time_offsets:
          _x = val3
          buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
        length = len(val1.scores)
        buff.write(_struct_I.pack(length))
        for val2 in val1.scores:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2
          buff.write(_get_struct_2f().pack(_x.raw_score, _x.scale))
        _x = val1.total
        buff.write(_get_struct_f().pack(_x))
      _x = self
      buff.write(_get_struct_2H().pack(_x.best_index, _x.worst_index))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.twists is None:
        self.twists = None
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.twists = []
      for i in range(0, length):
        val1 = dwb_msgs.msg.TrajectoryScore()
        _v3 = val1.traj
        _v4 = _v3.velocity
        _x = _v4
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v3.poses = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Pose2D()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.theta,) = _get_struct_3d().unpack(str[start:end])
          _v3.poses.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v3.time_offsets = []
        for i in range(0, length):
          val3 = genpy.Duration()
          _x = val3
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
          _v3.time_offsets.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.scores = []
        for i in range(0, length):
          val2 = dwb_msgs.msg.CriticScore()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.name = str[start:end]
          _x = val2
          start = end
          end += 8
          (_x.raw_score, _x.scale,) = _get_struct_2f().unpack(str[start:end])
          val1.scores.append(val2)
        start = end
        end += 4
        (val1.total,) = _get_struct_f().unpack(str[start:end])
        self.twists.append(val1)
      _x = self
      start = end
      end += 4
      (_x.best_index, _x.worst_index,) = _get_struct_2H().unpack(str[start:end])
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
      length = len(self.twists)
      buff.write(_struct_I.pack(length))
      for val1 in self.twists:
        _v5 = val1.traj
        _v6 = _v5.velocity
        _x = _v6
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.theta))
        length = len(_v5.poses)
        buff.write(_struct_I.pack(length))
        for val3 in _v5.poses:
          _x = val3
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.theta))
        length = len(_v5.time_offsets)
        buff.write(_struct_I.pack(length))
        for val3 in _v5.time_offsets:
          _x = val3
          buff.write(_get_struct_2i().pack(_x.secs, _x.nsecs))
        length = len(val1.scores)
        buff.write(_struct_I.pack(length))
        for val2 in val1.scores:
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2
          buff.write(_get_struct_2f().pack(_x.raw_score, _x.scale))
        _x = val1.total
        buff.write(_get_struct_f().pack(_x))
      _x = self
      buff.write(_get_struct_2H().pack(_x.best_index, _x.worst_index))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.twists is None:
        self.twists = None
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.twists = []
      for i in range(0, length):
        val1 = dwb_msgs.msg.TrajectoryScore()
        _v7 = val1.traj
        _v8 = _v7.velocity
        _x = _v8
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v7.poses = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Pose2D()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.theta,) = _get_struct_3d().unpack(str[start:end])
          _v7.poses.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v7.time_offsets = []
        for i in range(0, length):
          val3 = genpy.Duration()
          _x = val3
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2i().unpack(str[start:end])
          _v7.time_offsets.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.scores = []
        for i in range(0, length):
          val2 = dwb_msgs.msg.CriticScore()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.name = str[start:end]
          _x = val2
          start = end
          end += 8
          (_x.raw_score, _x.scale,) = _get_struct_2f().unpack(str[start:end])
          val1.scores.append(val2)
        start = end
        end += 4
        (val1.total,) = _get_struct_f().unpack(str[start:end])
        self.twists.append(val1)
      _x = self
      start = end
      end += 4
      (_x.best_index, _x.worst_index,) = _get_struct_2H().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2H = None
def _get_struct_2H():
    global _struct_2H
    if _struct_2H is None:
        _struct_2H = struct.Struct("<2H")
    return _struct_2H
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f