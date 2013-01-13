#! /usr/bin/env python

import rospy
import roslib
roslib.load_manifest("movie_player")

import subprocess

from movie_player.msg import PlayList
from movie_player.msg import Control

class MoviePlayer:
    def __init__(self):
        self.sub = rospy.Subscriber("/movie/play",
                                    PlayList,
                                    self.play_by_msg)
        self.control_sub = rospy.Subscriber("/movie/control",
                                            Control,
                                            self.control_by_msg)

    def play(self, paths, fullscreen=True):
        args = ["totem"]
        if fullscreen:
            args.append("--fullscreen")
        totem = subprocess.call(args + paths)

    def play_by_msg(self, msg):
        print msg.paths
        self.play(msg.paths)

    def control_by_msg(self, msg):
        if msg.type == Control.PLAY:
            p = subprocess.call(["totem", "--play"])
        elif msg.type == Control.PAUSE:
            p = subprocess.call(["totem", "--pause"])
        elif msg.type == Control.QUIT:
            p = subprocess.call(["totem", "--quit"])
        elif msg.type == Control.NEXT:
            p = subprocess.call(["totem", "--next"])
        elif msg.type == Control.PREVIOUS:
            p = subprocess.call(["totem", "--previous"])


if __name__ == '__main__':
    rospy.init_node('movie_player')
    node = MoviePlayer()
    rospy.spin()
