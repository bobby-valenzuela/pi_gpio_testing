#!/usr/bin/env python

from gpiozero import Button
from time import sleep

button = Button(24)
joystick_x = Button(18)
joystick_y = Button(23)

while True:
    
    if button.is_pressed:
        print("Btn Pressed")

    if joystick_x.is_pressed:
        print("Going X...")

    if joystick_y.is_pressed:
        print("Going Y...")
