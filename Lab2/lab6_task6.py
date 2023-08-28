import RPi.GPIO as gpio
import time

#Set the board numbering and input and output pins
gpio.setmode(gpio.BCM)
TRIG = 17
MEAS = 4

gpio.setup(TRIG ,gpio.OUT) #setting output channel
gpio.setup(MEAS ,gpio.IN)  #setting input channle
gpio.output(TRIG,gpio.LOW) #Set output to 0

#Acquire the zero reference time 
zero_time = time.time()

#Set the trigger to a high value for a certain time
gpio.output(TRIG,gpio.HIGH)
time.sleep(100E-3)

#Measure the duration of high value with an error timeout of 1 second
while gpio.input(MEAS) == 1:
    stop_time = time.time()
    if stop_time - zero_time > 1:
        break

#Set the trigger value to low
gpio.output(TRIG,gpio.LOW)

#Calculate the trigger time
pulse_duration = stop_time - zero_time

print("Pulse duration:", pulse_duration,"s")

gpio.cleanup()