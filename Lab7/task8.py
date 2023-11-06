import ctypes
import os
import time

file = open('data_task8_2.csv','w')

#Import driver for sensor reading ------------------------------
wd = os.getcwd()                      #Get working directory
driver_file ="/driver_D6F_PH0505.so"  #Define driver filename
driver_filepath = wd+driver_file      #Create full path name 
sensor = ctypes.CDLL(driver_filepath) #Load driver functions
#---------------------------------------------------------------

data = []
file.writelines('output, calc\n')


tic = time.perf_counter()

#Read and print one data point with the pressue sensor
while ((time.perf_counter()-tic)<2):
    sensor_data_point = sensor.main()
    data.append(sensor_data_point)
    file.writelines(f'{sensor_data_point}, {(((sensor_data_point-1024)/60000)*100)-50}\n')

d = 0
for i in data:
    d += i**2
d = (d/len(data))**0.5

print(d)

file.close()






