# http://ros.org/doc/groovy/api/catkin/html/user_guide/supposed.html
cmake_minimum_required(VERSION 2.8.3)
project(media_player)

find_package(catkin REQUIRED COMPONENTS rospy message_generation)

catkin_python_setup()

add_message_files(
  FILES Control.msg ImageInfo.msg PlayList.msg Volume.msg
)

generate_messages()

catkin_package(
    DEPENDS rospy
    CATKIN-DEPENDS message_runtime
    INCLUDE_DIRS # TODO include
    LIBRARIES # TODO
)

