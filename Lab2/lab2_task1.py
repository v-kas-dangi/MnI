import RPi.GPIO as gpio
import time

channel  = 21
light_on = 2
freq_list=[10, 400, 1000, 5000, 10000, 100000]

gpio.setmode(gpio.BCM)
gpio.setup(channel, gpio.OUT)

def proc(x):
    time_period=1/freq_list[x]
    time_stamp=time.perf_counter()
    while True:
        if(time.perf_counter-time_stamp)<light_on:
            gpio.output(channel, gpio.HIGH)
            time.sleep(time_period/2)
            gpio.output(channel, gpio.LOW)
            time.sleep(time_period/2)
        else:
            break
for x in freq_list:
    proc(x)

gpio.cleanup()