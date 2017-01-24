#!/usr/bin/env python

#!/usr/bin/env python

# Node Description: Random Publisher Node publishes random linear and angular  
# messages of  sthe messagte type geometry_msgs to the topic 'lab_two_random'
# The rate at which the publisher publishes is also random for the
# random publisher node

# Intro to Robotics - EE5900 - Spring 2017
#          Assignment #2

#       Project Group #1
#	Phillip Scramlin (Team Lead)
#	Derek Chopp 
#	Roger Gomes

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Vector3 
import random

def randomPublisher():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)#Intialize the publisher and topic to which the node publishes
    rospy.init_node('random_pub', anonymous=True)#Intialize the node
    rate = rospy.Rate(1/(0.1 * random.uniform(5,50)))#Define a random rate of publishing the message	
    while not rospy.is_shutdown():
	#Define the linear and angular messages - First was change in linear orientation
    	linear_msg = Vector3(x=random.uniform(-3,3), y=float(0.0), z=float(0.0))
    	angular_msg = Vector3(x=float(0.0), y=float(0.0), z=random.uniform(0,0))
    	#Intialize the twist messgae to be sent for change in linear orientation
    	publish_msg = Twist(linear=linear_msg, angular=angular_msg)
    	#Log the published Linear and angular velocity messages
    	rospy.loginfo('Linear Velocity Msg: %.2f'%linear_msg.x)
    	rospy.loginfo('Angular Velocity Msg: %.2f'%angular_msg.z)
	#Publish change in linear orientation
	pub.publish(publish_msg)
	#Sleep for random time
	rate.sleep()

	#Define the linear and angular messages - Change in angular orientation
    	linear_msg = Vector3(x=random.uniform(0,0), y=float(0.0), z=float(0.0))
    	angular_msg = Vector3(x=float(0.0), y=float(0.0), z=random.uniform(-3,3))
    	#ntialize the twist messgae to be sent for change in angular orientation
    	publish_msg = Twist(linear=linear_msg, angular=angular_msg)
    	#Log the published Linear and angular velocity messages
    	rospy.loginfo('Linear Velocity Msg: %.2f'%linear_msg.x)
    	rospy.loginfo('Angular Velocity Msg: %.2f'%angular_msg.z)
	#Publish change in angular orientation
	pub.publish(publish_msg)
	#Sleep for random time
    	rate.sleep()

if __name__ == '__main__':
    try:
        randomPublisher()
    except rospy.ROSInterruptException:
        pass
