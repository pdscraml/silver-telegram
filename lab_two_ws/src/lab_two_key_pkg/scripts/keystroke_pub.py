#!/usr/bin/env python
# BEGIN ALL
import sys, select, tty, termios
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    key_pub = rospy.Publisher('/lab_two_key', Twist, queue_size=1)
    rospy.init_node("keystroke_pub")
    # rate = rospy.Rate(100)
    # BEGIN TERMIOS
    old_attr = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    # END TERMIOS
    print "Publishing keystrokes. Press Ctrl-C to exit..."
    lin_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
    ang_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
    e = "Error"
    try:
        while not rospy.is_shutdown():
            # BEGIN SELECT
            key_pressed = getKey()
            if key_pressed == 'w' or key_pressed == 'W':
                lin_msg = Vector3(x=float(0.5), y=float(0.0), z=float(0.0))
                ang_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
            elif key_pressed == 's' or key_pressed == 'S':
                lin_msg = Vector3(x=float(-0.5), y=float(0.0), z=float(0.0))
                ang_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
            elif key_pressed == 'd' or key_pressed == 'D':
                lin_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
                ang_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.05))
            elif key_pressed == 'a' or key_pressed == 'A':
                lin_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
                ang_msg = Vector3(x=float(0.0), y=float(0.0), z=float(-0.05))
            else:
                lin_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
                ang_msg = Vector3(x=float(0.0), y=float(0.0), z=float(0.0))
            publish_msg = Twist(linear=lin_msg, angular=ang_msg)
            key_pub.publish(publish_msg)  # Publishing to topic

    except rospy.ROSInterruptException:
        pass

    finally:
        default_msg = Twist()
        default_msg.linear.x = 0
        default_msg.linear.y = 0
        default_msg.linear.z = 0
        default_msg.angular.x = 0
        default_msg.angular.y = 0
        default_msg.angular.z = 0
        key_pub.publish(default_msg)
# rate.sleep()
# END SELECT
# BEGIN TERMIOS_END
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)  # END TERMIOS_END  # END ALL
