#!/usr/bin/env python

#import RPi.GPIO as GPIO

import time
import rospy
from std_msgs.msg import String
import ledpy


#GPIO.setmode(GPIO.BCM)
#GPIO.output

def led_callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "COMMAND DATA is %s", msg.data)

    if msg.data == 'a' :
        ledpy.SetLedLeftTurn()
    elif msg.data == 's':
        ledpy.SetLedRightTurn()
    elif msg.data == 'd':
        ledpy.SetLedLeftShiftOn()
    elif msg.data == 'f':
        ledpy.SetLedRightShiftOn()
    elif msg.data == 'c':
        ledpy.SetLedLeftShiftOff()
    elif msg.data == 'v':
        ledpy.SetLedRightShiftOff()
    elif msg.data == 'g':
        ledpy.SetLedOn()
    elif msg.data == 'b':
        ledpy.SetLedOff()
    elif msg.data == 'q':
        ledpy.SetForced_Shutdown()
    elif msg.data == 'w':
        ledpy.SetForced_BootUp()


def led_ctrl():
    led = [2, 3, 4, 17, 27]
    ledpy.Init_Led_Port(led)
    ledpy.SetForced_BootUp()

    rospy.init_node('led_ctrl', anonymous=True)
    rospy.Subscriber("ctrl", String, led_callback)
    rospy.loginfo('I am Ready!')

    rospy.spin()
if __name__ == '__main__':
    led_ctrl()
