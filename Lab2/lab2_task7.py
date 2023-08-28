import pigpio
import RPi.GPIO as gpiodev
from time import sleep

#Define the channels for trigger and measurement
TRIG = 17
MEAS = 4


#Set Trigger and measurement pins
pi = pigpio.pi()
pi.set_mode(TRIG,pigpio.OUTPUT)
pi.set_mode(MEAS,pigpio.INPUT)

#Define background functions to watch events 
def ownrise(gpio,level,tick):
    global riseedge
    riseedge = tick
    
def ownfall(gpio,level,tick):
    global falledge
    falledge = tick

#Initialise callback functions to run in the background
#Whenever an event is happening a timestamp is measure    
pi.callback(MEAS,pigpio.RISING_EDGE,ownrise)
pi.callback(MEAS,pigpio.FALLING_EDGE,ownfall)

#Create a trigger 
pi.gpio_trigger()  

#Wait for 1  s to compute and print the duration of trigger time
sleep(1)
pulse_duration = falledge - riseedge
print("Pulse duration:", pulse_duration,"us")



    