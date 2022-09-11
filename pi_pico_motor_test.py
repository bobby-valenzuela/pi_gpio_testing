from machine import Pin, PWM
import utime

MID= 150000
MIN = 1000000
MAX = 2000000

led = Pin("LED",Pin.OUT)
pwm = PWM(Pin(1))
pwm.freq(50)
pwm.duty_ns(MID)


while True:
    led.on()
    print("running...")
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1)
    pwm.duty_ns(MAX)
    utime.sleep(1)
    led.off()
    utime.sleep(1)
