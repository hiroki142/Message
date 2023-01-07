#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

ros2 topic pub --once /input log_msgs/msg/Log "{log: Hello World}" &
timeout 1 ros2 launch Message talk_listen.launch.py > /tmp/Message.log

cat /tmp/Message.log |
grep 'Hello World' 
