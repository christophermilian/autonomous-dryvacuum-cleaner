// Generated by gencpp from file sensor_msgs/Imu.msg
// DO NOT EDIT!


#ifndef SENSOR_MSGS_MESSAGE_IMU_H
#define SENSOR_MSGS_MESSAGE_IMU_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Quaternion.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Vector3.h>

namespace sensor_msgs
{
template <class ContainerAllocator>
struct Imu_
{
  typedef Imu_<ContainerAllocator> Type;

  Imu_()
    : header()
    , orientation()
    , orientation_covariance()
    , angular_velocity()
    , angular_velocity_covariance()
    , linear_acceleration()
    , linear_acceleration_covariance()  {
      orientation_covariance.assign(0.0);

      angular_velocity_covariance.assign(0.0);

      linear_acceleration_covariance.assign(0.0);
  }
  Imu_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , orientation(_alloc)
    , orientation_covariance()
    , angular_velocity(_alloc)
    , angular_velocity_covariance()
    , linear_acceleration(_alloc)
    , linear_acceleration_covariance()  {
  (void)_alloc;
      orientation_covariance.assign(0.0);

      angular_velocity_covariance.assign(0.0);

      linear_acceleration_covariance.assign(0.0);
  }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::geometry_msgs::Quaternion_<ContainerAllocator>  _orientation_type;
  _orientation_type orientation;

   typedef boost::array<double, 9>  _orientation_covariance_type;
  _orientation_covariance_type orientation_covariance;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _angular_velocity_type;
  _angular_velocity_type angular_velocity;

   typedef boost::array<double, 9>  _angular_velocity_covariance_type;
  _angular_velocity_covariance_type angular_velocity_covariance;

   typedef  ::geometry_msgs::Vector3_<ContainerAllocator>  _linear_acceleration_type;
  _linear_acceleration_type linear_acceleration;

   typedef boost::array<double, 9>  _linear_acceleration_covariance_type;
  _linear_acceleration_covariance_type linear_acceleration_covariance;





  typedef boost::shared_ptr< ::sensor_msgs::Imu_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sensor_msgs::Imu_<ContainerAllocator> const> ConstPtr;

}; // struct Imu_

typedef ::sensor_msgs::Imu_<std::allocator<void> > Imu;

typedef boost::shared_ptr< ::sensor_msgs::Imu > ImuPtr;
typedef boost::shared_ptr< ::sensor_msgs::Imu const> ImuConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sensor_msgs::Imu_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sensor_msgs::Imu_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace sensor_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'sensor_msgs': ['/home/ubuntu/catkin_ws/src/sensor_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs::Imu_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs::Imu_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs::Imu_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs::Imu_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs::Imu_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs::Imu_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sensor_msgs::Imu_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6a62c6daae103f4ff57a132d6f95cec2";
  }

  static const char* value(const ::sensor_msgs::Imu_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6a62c6daae103f4fULL;
  static const uint64_t static_value2 = 0xf57a132d6f95cec2ULL;
};

template<class ContainerAllocator>
struct DataType< ::sensor_msgs::Imu_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sensor_msgs/Imu";
  }

  static const char* value(const ::sensor_msgs::Imu_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sensor_msgs::Imu_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This is a message to hold data from an IMU (Inertial Measurement Unit)\n\
#\n\
# Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec\n\
#\n\
# If the covariance of the measurement is known, it should be filled in (if all you know is the \n\
# variance of each measurement, e.g. from the datasheet, just put those along the diagonal)\n\
# A covariance matrix of all zeros will be interpreted as \"covariance unknown\", and to use the\n\
# data a covariance will have to be assumed or gotten from some other source\n\
#\n\
# If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an orientation \n\
# estimate), please set element 0 of the associated covariance matrix to -1\n\
# If you are interpreting this message, please check for a value of -1 in the first element of each \n\
# covariance matrix, and disregard the associated estimate.\n\
\n\
Header header\n\
\n\
geometry_msgs/Quaternion orientation\n\
float64[9] orientation_covariance # Row major about x, y, z axes\n\
\n\
geometry_msgs/Vector3 angular_velocity\n\
float64[9] angular_velocity_covariance # Row major about x, y, z axes\n\
\n\
geometry_msgs/Vector3 linear_acceleration\n\
float64[9] linear_acceleration_covariance # Row major x, y z \n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::sensor_msgs::Imu_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sensor_msgs::Imu_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.orientation);
      stream.next(m.orientation_covariance);
      stream.next(m.angular_velocity);
      stream.next(m.angular_velocity_covariance);
      stream.next(m.linear_acceleration);
      stream.next(m.linear_acceleration_covariance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Imu_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sensor_msgs::Imu_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sensor_msgs::Imu_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "orientation: ";
    s << std::endl;
    Printer< ::geometry_msgs::Quaternion_<ContainerAllocator> >::stream(s, indent + "  ", v.orientation);
    s << indent << "orientation_covariance[]" << std::endl;
    for (size_t i = 0; i < v.orientation_covariance.size(); ++i)
    {
      s << indent << "  orientation_covariance[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.orientation_covariance[i]);
    }
    s << indent << "angular_velocity: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.angular_velocity);
    s << indent << "angular_velocity_covariance[]" << std::endl;
    for (size_t i = 0; i < v.angular_velocity_covariance.size(); ++i)
    {
      s << indent << "  angular_velocity_covariance[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.angular_velocity_covariance[i]);
    }
    s << indent << "linear_acceleration: ";
    s << std::endl;
    Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "  ", v.linear_acceleration);
    s << indent << "linear_acceleration_covariance[]" << std::endl;
    for (size_t i = 0; i < v.linear_acceleration_covariance.size(); ++i)
    {
      s << indent << "  linear_acceleration_covariance[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.linear_acceleration_covariance[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SENSOR_MSGS_MESSAGE_IMU_H
