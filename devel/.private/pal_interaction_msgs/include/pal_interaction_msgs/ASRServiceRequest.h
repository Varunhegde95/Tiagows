// Generated by gencpp from file pal_interaction_msgs/ASRServiceRequest.msg
// DO NOT EDIT!


#ifndef PAL_INTERACTION_MSGS_MESSAGE_ASRSERVICEREQUEST_H
#define PAL_INTERACTION_MSGS_MESSAGE_ASRSERVICEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <pal_interaction_msgs/ASRSrvRequest.h>

namespace pal_interaction_msgs
{
template <class ContainerAllocator>
struct ASRServiceRequest_
{
  typedef ASRServiceRequest_<ContainerAllocator> Type;

  ASRServiceRequest_()
    : request()  {
    }
  ASRServiceRequest_(const ContainerAllocator& _alloc)
    : request(_alloc)  {
  (void)_alloc;
    }



   typedef  ::pal_interaction_msgs::ASRSrvRequest_<ContainerAllocator>  _request_type;
  _request_type request;





  typedef boost::shared_ptr< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ASRServiceRequest_

typedef ::pal_interaction_msgs::ASRServiceRequest_<std::allocator<void> > ASRServiceRequest;

typedef boost::shared_ptr< ::pal_interaction_msgs::ASRServiceRequest > ASRServiceRequestPtr;
typedef boost::shared_ptr< ::pal_interaction_msgs::ASRServiceRequest const> ASRServiceRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator1> & lhs, const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator2> & rhs)
{
  return lhs.request == rhs.request;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator1> & lhs, const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pal_interaction_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bf3afdb7a9717c398d58f3a78181472c";
  }

  static const char* value(const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbf3afdb7a9717c39ULL;
  static const uint64_t static_value2 = 0x8d58f3a78181472cULL;
};

template<class ContainerAllocator>
struct DataType< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_interaction_msgs/ASRServiceRequest";
  }

  static const char* value(const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_interaction_msgs/ASRSrvRequest request\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/ASRSrvRequest\n"
"# Request messages for the recognizer service.\n"
"# It is possible to request and activate task, \n"
"# a grammar management task and language change or just\n"
"# request the current status.\n"
"\n"
"# Type of request list\n"
"int8 ACTIVATION = 1\n"
"int8 GRAMMAR = 2\n"
"int8 LANGUAGE = 3\n"
"int8 STATUS = 4\n"
"int8 KWSPOTTING = 5\n"
"\n"
"# Message variables\n"
"# list of requests types (several requests can be send in one single message)\n"
"int8[] requests\n"
"\n"
"# Information related to each possible request\n"
"# except for status that does not need any additional info.\n"
"ASRActivation activation\n"
"ASRLangModelMngmt model\n"
"ASRLanguage lang\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/ASRActivation\n"
"# Message that can be used to send activation commands to the speech recognizer.\n"
"# It is possible to activate/deactivate or pause/resume the recognizer with these commands.\n"
"# action list\n"
"int8 ACTIVATE = 1\n"
"int8 DEACTIVATE = 2\n"
"int8 PAUSE = 3\n"
"int8 RESUME = 4\n"
"int8 CALIBRATE = 5\n"
"\n"
"# Message variables\n"
"int8 action\n"
"\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/ASRLangModelMngmt\n"
"# This message is to be used in the ASR service to manage the grammars\n"
"# makes possible to enable/disable, load/unload grammars.\n"
"\n"
"\n"
"# Types of action\n"
"int8 ENABLE = 1\n"
"int8 DISABLE = 2\n"
"int8 LOAD = 3\n"
"int8 UNLOAD = 4\n"
"\n"
"# Message variables\n"
"# Type of action requested\n"
"int8 action\n"
"\n"
"# Name of the grammar to actuate on.\n"
"string modelName\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/ASRLanguage\n"
"# This message is to indicate the language\n"
"# that has to be set in the speech recognizer\n"
"string language\n"
;
  }

  static const char* value(const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.request);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ASRServiceRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pal_interaction_msgs::ASRServiceRequest_<ContainerAllocator>& v)
  {
    s << indent << "request: ";
    s << std::endl;
    Printer< ::pal_interaction_msgs::ASRSrvRequest_<ContainerAllocator> >::stream(s, indent + "  ", v.request);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAL_INTERACTION_MSGS_MESSAGE_ASRSERVICEREQUEST_H
