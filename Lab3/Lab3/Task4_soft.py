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
    
    
soft_list = []

def proc():
    for i in range(1000):
        pi.gpio_trigger(TRIG,10,1)
        pi.callback(ECHO, pigpio.FALLING_EDGE, ownrise)
        pi.callback(ECHO, pigpio.RISING_EDGE, ownfall)
        tof = low-high
        distance = tof * 0.017150
        distance=round(distance, 3)
        soft_list.append(distance)
        time.sleep(0.01)
    return
proc()

file = open('hard_10cm.csv','w')
file.writelines(str(soft_list))
file.close()

pi.stop()
