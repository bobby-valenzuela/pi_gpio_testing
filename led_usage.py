# Important snippets
#  https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf

from machine import Pin

from machine import Pin
led = Pin(28, Pin.OUT)
led.toggle()
# or...
led.value(0)
led.value(1)
# or define the led start state...
# led = machine.Pin(28, machine.Pin.OUT, value=1)
