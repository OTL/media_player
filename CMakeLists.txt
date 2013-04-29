# http://ros.org/doc/groovy/api/catkin/html/user_guide/supposed.html
cmake_minimum_required(VERSION 2.8.3)
project(media_player)

find_package(catkin REQUIRED COMPONENTS message_generation)

#catkin_python_setup()

add_message_files(
  FILES Control.msg ImageInfo.msg PlayList.msg Volume.msg
)

generate_messages()

catkin_package(
    CATKIN-DEPENDS rospy message_runtime
)

install(PROGRAMS nodes/image_display.py
  nodes/movie_player.py
  nodes/volume_controller.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
