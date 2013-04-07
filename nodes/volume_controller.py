#! /usr/bin/env python

import rospy
import roslib
roslib.load_manifest("movie_player")

import subprocess

from movie_player.msg import Volume


def set_volume_by_amixer(volume, card_id=0, control='Master', device=None):
    # example command line: amixer -c1 sset PCM 500
    if device:
        args = ["amixer", "-D"+device, "sset", control, str(volume)]
    else:
        args = ["amixer", "-c%d"%card_id, "sset", control, str(volume)]
    result = subprocess.call(args)
    if result == 0:
        return True
    else:
        return False


class VolumeController:
    def __init__(self):
        self.max_value = rospy.get_param('~max_value', 255)
        if rospy.has_param('~device'):
            self.use_device = rospy.get_param('~device')
        else:
            self.use_device = None
        self.card_id = rospy.get_param('~card_id', 0)
        self.control = rospy.get_param('~control', 'PCM')
        self.sub = rospy.Subscriber("/audio_volume",
                                    Volume,
                                    self.change_volume_by_msg)

    def percentage_to_value(self, percent):
        value = percent * 0.01 * self.max_value
        if value > self.max_value:
            value = self.max_value
            rospy.logwarn("volume percent should be less than 100 (you set %d)"% percent)
        elif value < 0:
            value = 0
            rospy.logwarn("volume percent should be less than 100 (you set %d)"%percent)
        return value

    def change_volume_by_msg(self, msg):
        value = self.percentage_to_value(msg.percentage)
        if not set_volume_by_amixer(value, card_id=self.card_id, control=self.control, device=self.use_device):
            rospy.logerr('set volume by amixer failed')

if __name__ == '__main__':
    rospy.init_node('volume_controller')
    node = VolumeController()
    rospy.spin()
