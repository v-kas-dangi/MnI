#Distance measurement using HC-SR04 using software triggered pulses.

import RPi.GPIO as GPIO
import time


#Preparing the RPi------------------------------------------- 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
TRIG = ??
ECHO = ?? 
 
#set GPIO direction (IN / OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


#Create single trigger pulse with 10 ms on the TRIG pin
#Send trigger signal
GPIO.output(TRIG, GPIO.HIGH)
time.sleep(10E-6)
GPIO.output(TRIG, GPIO.LOW)
#------------------------------------------------------------


# save StartTime
while GPIO.input(ECHO) == 0:
    StartTime = time.time()

# save time of arrival
while GPIO.input(ECHO) == 1:
    StopTime = time.time()


TimeElapsed = (StopTime - StartTime)
print(TimeElapsed)


GPIO.cleanup()



