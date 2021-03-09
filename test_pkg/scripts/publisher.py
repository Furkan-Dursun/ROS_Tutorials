#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import rospy
from test_pkg.msg import vehicle

def publisher():

    pub = rospy.Publisher('vehicle_topic', vehicle, queue_size=10) # dugumu tanimladik ve yayinlanacagini bildirdik
    rospy.init_node('publisher', anonymous=True) # dugumu baslatmak icin

    rate = rospy.Rate(10) # 10hz , calisma hizimiz

    while(not rospy.is_shutdown()): 

        vehicle_info = vehicle()
        vehicle_info.name = "vehicle_1"
        vehicle_info.speed = 15
        vehicle_info.camera = "Active"
        vehicle_info.battery_remaining = 76

        rospy.loginfo(vehicle_info) # bilgileri ekrana basmamiz icin
        pub.publish(vehicle_info) # yayini yaptik

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass