#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import rospy
from test_pkg.msg import vehicle

def callback(data):

    rospy.loginfo(rospy.get_caller_id() + ' data received (%s, %d, %s, %d)', data.name,
    data.speed, data.camera, data.battery_remaining)

def listener():

    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('vehicle_topic', vehicle, callback) # dugumun abone oldugunu yayinlar

    rospy.spin() # dugum durana kadar python'un cikmasini engeller

if __name__ == '__main__':
    listener()