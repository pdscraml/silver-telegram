#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist, Vector3


timeout = 15

zeroLin = Vector3(x=0, y=0, z=0)
zeroAng = Vector3(x=0, y=0, z=0)
zeroMsg = Twist(linear=zeroLin, angular=zeroAng)

keyMsg = zeroMsg
randMsg = zeroMsg

keyTime = time.time() - timeout
randTime = time.time() - timeout

# Callback for a key message
def key_callback(data):
  global keyTime, keyMsg
  keyTime = time.time()
  keyMsg = data
  rospy.loginfo("I heard key %s, at %d", data.linear.x, keyTime)

# Callback for a random message
def random_callback(data):
  global randTime, randMsg
  randTime = time.time()
  randMsg = data
  rospy.loginfo("I heard rand %s, at %d", data.linear.x, randTime)


# Main Loop for node
if __name__ == '__main__':
  try:
    # Setup the publisher, subscribers
    pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("lab_two_key", Twist, key_callback)
    rospy.Subscriber("lab_two_random", Twist, random_callback)
    
    # Initialize ros node
    rospy.init_node('decider', anonymous=True)
    rate = rospy.Rate(10) # 10hz
  
    while not rospy.is_shutdown():
      currentTime = time.time()
      
      if((keyTime + timeout) > currentTime):
        pub.publish(keyMsg)
        rospy.loginfo("Send Key Message")
      elif((randTime + timeout) > currentTime):
        pub.publish(randMsg)
        rospy.loginfo("Send Random Message")
      else:
        pub.publish(zeroMsg) 
        rospy.loginfo("Send Zero Message")
      
      rate.sleep()
  except rospy.ROSInterruptException:
    pass

