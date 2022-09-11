from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

led.off()

for i in range(0,5):
    print(i)
    led.toggle()
    sleep(0.03)
    led.toggle()
    sleep(0.03)
