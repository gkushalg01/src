#! /usr/bin/env python3

import rospy
from math import isinf, pi

from sensor_msgs.msg import LaserScan

def callback(msg):
    obstacle = False 
    nearest_distance = float('inf')
    size = len(msg.ranges)
    for i in range(size):
        if msg.ranges[i] < nearest_distance:
            nearest_distance = msg.ranges[i]
            nearest_angle = i
            obstacle = True

    print("---")
    if (obstacle):
        print("Obstacle Detected:")
        print(f"Range = {nearest_distance:.3f}")
        print(f"Bearing = {(msg.angle_max-msg.angle_min)*nearest_angle/size:.3f}")
    else:
        print("All Fine.")

rospy.init_node('scanner_node')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()