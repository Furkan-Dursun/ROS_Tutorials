#!/usr/bin/env python
# license removed for brevity
import rospy
from test_pkg.msg import uav
    

pub = rospy.Publisher('chatter', uav, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
    uav_info = uav()
    uav.name = "uav_1"
    uav.speed = 15
    uav.camera = "Active"
    uav.remaining_battery = 76

    rospy.loginfo(uav_info) # bilgileri ekrana basmamiz icin
    pub.publish(uav_info) # yayini yaptik
    rate.sleep()
 
