import ctypes
import os

file = open('data.csv','w')

#Import driver for sensor reading ------------------------------
wd = os.getcwd()                      #Get working directory
driver_file ="/driver_D6F_PH0505.so"  #Define driver filename
driver_filepath = wd+driver_file      #Create full path name 
sensor = ctypes.CDLL(driver_filepath) #Load driver functions
#---------------------------------------------------------------

data = []

#Read and print one data point with the pressue sensor
for i in range(500):
    sensor_data_point = sensor.main()
    data.append(sensor_data_point)

file.writelines(str(data))
print(sensor_data_point)

file.close()
