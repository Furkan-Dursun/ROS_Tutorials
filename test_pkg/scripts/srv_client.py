#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import rospy
from test_pkg.srv import battery
import sys

def client():
    
    rospy.init_node('srv_client') # dugumu tanimladik
    rospy.wait_for_service('calculate_time') # calculate_time adli erver erisilebilir olana kadar bekle

    response = rospy.ServiceProxy('calculate_time', battery) # servisi cagirmak icin

    battery_num = int(sys.argv[1]) # terminalden veri girmek icin
    print(battery_num)
    res = response(battery_num)

    print("Remain time: ",res.remain_time )

if __name__ == "__main__":
    try:
        client()
    except rospy.ROSInterruptException:
        pass