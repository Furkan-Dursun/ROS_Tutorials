#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import rospy
from test_pkg.srv import battery

def calculate(number):
    return number.battery_num*2

def server():

    rospy.init_node('srv_server') # dugumu tanimladik
    service = rospy.Service('calculate_time', battery, calculate) # servisi yayinladik
    print("Ready to calculate time")

    rospy.spin() 

if __name__ == "__main__":
    try:
        server()
    except rospy.ROSInterruptException:
        pass