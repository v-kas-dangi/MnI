import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
channel = 17
gpio.setup(channel, gpio.OUT)
gpio.output(channel,gpio.LOW)
gpio.output(channel,gpio.HIGH)
sleep(0.1)
gpio.output(channel, gpio.LOW)
sleep(0.1)
gpio.cleanup()