#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3 
import random

def randomPublisher():
  pub = rospy.Publisher('lab_two_random', Twist, queue_size=10)
  rospy.init_node('random_pub', anonymous=True)
  rate = rospy.Rate(5)
  while not rospy.is_shutdown():
    rate = rospy.Rate(1/(0.1 * random.uniform(1,10)))
    linear_velocity = Vector3(x=random.uniform(-2,2), y=float(0.0), z=float(0.0))
    angular_velocity = Vector3(x=float(0.0), y=float(0.0), z=random.uniform(-3,3))
    publish_msg = Twist(linear=linear_velocity, angular=angular_velocity)
    rospy.loginfo('Linear Velocity: %.2f'%linear_velocity.x)
    rospy.loginfo('Angular Velocity: %.2f'%angular_velocity.z)
    pub.publish(publish_msg)
    rate.sleep()

if __name__ == '__main__':
    try:
        randomPublisher()
    except rospy.ROSInterruptException:
        pass
