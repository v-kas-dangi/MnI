import RPi.GPIO as gpio
import time

channel  = 21
light_on = 2
freq_list=[100]
DutyCycle=[0]
# DutyCycle=[0, 25, 50, 75, 100]

gpio.setmode(gpio.BCM)
gpio.setup(channel, gpio.OUT)

def proc(x):
    time_period=1/freq_list[0]
    time_stamp=time.perf_counter()
    while True:
        if(time.perf_counter-time_stamp)<light_on:
            gpio_pwm=gpio.PWM(channel, freq_list[0])
            gpio_pwm.start(x)
        else:
            break
        
for x in DutyCycle:
    proc(x)

gpio.cleanup()