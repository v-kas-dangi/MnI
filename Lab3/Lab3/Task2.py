import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=4
ECHO=17
print("Distance Measurement in progress ")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)
GPIO.output(TRIG, True)
time.sleep(0.01)
GPIO.output(TRIG, False)
while GPIO.input(ECHO)==0:
    pulse_start = time.time()
while GPIO.input (ECHO)==1:
    pulse_end = time.time()
flight_time = pulse_end - pulse_start
distance = flight_time * 17150
distance=round(distance, 2)
print("Distance: ", distance, " cm")
flight_time = round(flight_time*1000000, 2)
print('Time Elapsed', flight_time, ' us')
GPIO.cleanup()