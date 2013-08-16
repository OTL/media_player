#! /usr/bin/env python

import rospy
import subprocess

from media_player.msg import ImageInfo
from media_player.msg import Control


class ImageDisplay:
    def __init__(self):
        self._sub = rospy.Subscriber("/image/display",
                                    ImageInfo,
                                    self.display_by_msg)
        self._control_sub = rospy.Subscriber("/image/control",
                                            Control,
                                            self.control_by_msg)
        self._process = None

    def display(self, path, fullscreen=True):
        args = ["eog"]
        if fullscreen:
            args.append("-f")
        args.append("-w") # single window mode
        args.append(path)
        process = subprocess.Popen(args)
        if not self._process:
            self._process = process

    def display_by_msg(self, msg):
        self.display(msg.path)

    def quit(self):
        if self._process:
            self._process.kill()
            self._process = None

    def control_by_msg(self, msg):
        if msg.type == Control.QUIT:
            self.quit()

if __name__ == '__main__':
    rospy.init_node('image_display')
    node = ImageDisplay()
    rospy.spin()
