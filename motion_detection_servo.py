from utime import sleep
from machine import Pin, PWM

# IR Sensor
prox_sensor = Pin(0, Pin.IN)

# Servo motor
servo_01 = PWM(Pin(1))
servo_01.freq(50)

# Servo Config
MIN = 1000000
MAX = 2000000

# Onboard led
led = Pin("LED",Pin.OUT)

def detected_obj():
    return 1 if prox_sensor.value() == 0 else 0

def move_servo(dir):

    if dir == 'l':
        servo_01.duty_ns(MAX)
    else:
        servo_01.duty_ns(MIN)

# Initiate servo left
move_servo('l')

while True:

    print(detected_obj())

    if detected_obj() == 0 :
        move_servo('l')
    else:
        move_servo('r')

    sleep(0.15)
