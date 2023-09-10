import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=4
ECHO=17
print("Distance Measurement in progress ")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, GPIO.HIGH)
time.sleep(10E-3)
GPIO.output(TRIG, GPIO.LOW)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
flight_time = pulse_end - pulse_start

distance = flight_time * 17150
distance=round(distance, 2)
print("Distance: ", distance, " cm")
flight_time = round(flight_time*1000000, 2)
print('Time Elapsed', flight_time, ' us')

soft_list = []

for i in range(1000):
    
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(10E-3)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    flight_time = pulse_end - pulse_start
    distance = flight_time * 17150
    distance=round(distance, 3)
    soft_list.append(distance)
    
file = open('soft_10cm.csv','w')
file.writelines(str(soft_list))
file.close()
print('done')


GPIO.cleanup()
