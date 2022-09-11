#!/usr/bin/env python

print("Running...")

from gpiozero import AngularServo, Device
from time import sleep
from bluedot import BlueDot
from signal import pause

# Prevent jitter by changing pin factory
from gpiozero.pins.pigpio import PiGPIOFactory
Device.pin_factory = PiGPIOFactory()

# pause()


# Initialize Servo Instance
# servo = Servo(13)
servo = AngularServo(13, min_angle=44, max_angle=-42)
servo.angle = 0.0

bd = BlueDot()

def dpad(pos):
    
    if pos.top:
        print("up")
        left_right(0.3)

    elif pos.bottom:
        print("down")
        left_right(0.2,4)

    elif pos.left:
        print("left")
        servo.angle = -42

    elif pos.right:
        print("right")
        servo.angle = 44

    elif pos.middle:
        print("middle")
        servo.angle = 0.0

def left_right(naptime, step = 1):
    
    for deg in range(-42,44, step):
        
        if deg > 44:
            break

        servo.angle = deg
        sleep(naptime)


bd.when_pressed = dpad

pause()
