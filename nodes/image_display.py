#! /usr/bin/env python

import rospy
import roslib
roslib.load_manifest("movie_player")

import subprocess

from movie_player.msg import ImageInfo
from movie_player.msg import Control

class ImageDisplay:
    def __init__(self):
        self.sub = rospy.Subscriber("/image/display",
                                    ImageInfo,
                                    self.display_by_msg)
        self.control_sub = rospy.Subscriber("/image/control",
                                            Control,
                                            self.control_by_msg)
        self.process = None

    def display(self, path, fullscreen=True):
        args = ["eog"]
        if fullscreen:
            args.append("-f")
        args.append(path)
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen(args)

    def display_by_msg(self, msg):
        self.display(msg.path)

    def control_by_msg(self, msg):
        if msg.type == Control.QUIT:
            if self.process:
                self.process.kill()

if __name__ == '__main__':
    rospy.init_node('image_display')
    node = ImageDisplay()
    rospy.spin()
