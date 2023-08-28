import RPi.GPIO as gpio
from time import sleep

//Complete the code to specify the board numbering format
gpio.setmode(????)

//Specify the GPIO pin number you will use
channel = ??????

//Initialize the pin as an input or an output
gpio.setup(???)

//Code pushes the output of the pin to low level. 
gpio.output(channel,gpio.LOW)

//See what the following code does. Modify this code to complete the Lab 1 tasks
gpio.output(channel,gpio.HIGH)
sleep(5)
gpio.output(channel, gpio.LOW)
sleep(5)

//Frees up the GPIO pin. 
gpio.cleanup()