import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)
channel = 17

gpio.setup(channel, gpio.OUT)
gpio.output(channel,gpio.LOW)
for t in [0.1, 0.01, 0.001, 0.0001]:
    for i in range(5):
        gpio.output(channel,gpio.HIGH)
        sleep(0.1)
        gpio.output(channel, gpio.LOW)
        sleep(0.1)
gpio.cleanup()