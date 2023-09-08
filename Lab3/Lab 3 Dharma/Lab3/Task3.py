import pigpio
import time

pi = pigpio.pi()

TRIG = 4
ECHO = 17


def ownrise(gpio, level, tick):
    global low
    low = tick
    
def ownfall(gpio, level, tick):
    global high
    high = tick

pi.gpio_trigger(TRIG,10,1)

pi.callback(ECHO, pigpio.FALLING_EDGE, ownrise)
pi.callback(ECHO, pigpio.RISING_EDGE, ownfall)

if pi.wait_for_edge(ECHO, pigpio.FALLING_EDGE, 5):
    tof = low-high
    distance = tof * 0.017150
    distance=round(distance, 2)
    print("Distance: ", distance, " cm")
    print(tof)
else:
    print('Timeout')
    
    

pi.stop()