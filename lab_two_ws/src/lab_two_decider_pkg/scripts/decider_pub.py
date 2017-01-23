#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist, Vector3

timeout = 15

# Create a "safe" message to send in absence of valid input
zeroLin = Vector3(x=0, y=0, z=0)
zeroAng = Vector3(x=0, y=0, z=0)
zeroMsg = Twist(linear=zeroLin, angular=zeroAng)

# Initialize variables for rx'd message to a safe message
keyMsg = zeroMsg
randMsg = zeroMsg

# Initialize variables for rx'd time to an expired time
keyTime = time.time() - (timeout + 1)
randTime = time.time() - (timeout + 1)

# Initialize variables for new rx'd message
newKey = 0
newRand = 0

# Callback for a key message
def key_callback(data):
  global keyTime, keyMsg, newKey
  keyTime = time.time()
  keyMsg = data
  rospy.loginfo("I heard key [%.2f,%.2f,%.2f] [%.2f,%.2f,%.2f], at %d", data.linear.x, data.linear.y, data.linear.z, data.angular.x, data.angular.y, data.angular.z, keyTime)
  newKey = 1;

# Callback for a random message
def random_callback(data):
  global randTime, randMsg, newRand
  randTime = time.time()
  randMsg = data
  rospy.loginfo("I heard random [%.2f,%.2f,%.2f] [%.2f,%.2f,%.2f], at %d", data.linear.x, data.linear.y, data.linear.z, data.angular.x, data.angular.y, data.angular.z, randTime)
  newRand = 1;

# Main Loop for node
if __name__ == '__main__':
  try:
    # Setup the publisher, subscribers
    pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber("lab_two_key", Twist, key_callback)
    rospy.Subscriber("lab_two_random", Twist, random_callback)
    
    # Initialize ros node
    rospy.init_node('decider', anonymous=True)
    rate = rospy.Rate(50)
  
    while not rospy.is_shutdown():
      currentTime = time.time()
      
      # Select what message should be sent
      if(((keyTime + timeout) > currentTime)):
        if(newKey == 1):
          newKey = 0
          pub.publish(keyMsg)
          rospy.loginfo("Send Key Message")
      elif(((randTime + timeout) > currentTime)):
        if(newRand == 1):
          newRand = 0
          pub.publish(randMsg)
          rospy.loginfo("Send Random Message")
      else:
        pub.publish(zeroMsg) 
        rospy.loginfo("Send Zero Message")
      
      rate.sleep()
  except rospy.ROSInterruptException:
    pass

