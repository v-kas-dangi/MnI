import pigpio
from time import sleep

pi = pigpio.pi()

#set GPIO pins
channel = 17

light_on = 10;        #seconds
frequency =  100000;    #seconds 

#Initialize the pin
pi.set_mode(gpio.BCM)
pi.set_PWM_dutycycle(50)

#Start the PWM signal by setting the frequency
pi.set_PWM_frequency(channel, frequency)
 
#Measure the frequency set on the pin
print(pi.get_PWM_frequency())

sleep(light_on)

#Switch channel off
pi.write(channel,0)

