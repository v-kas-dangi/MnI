import ctypes
import os

file = open('data_task3.csv','w')

#Import driver for sensor reading ------------------------------
wd = os.getcwd()                      #Get working directory
driver_file ="/driver_D6F_PH0505.so"  #Define driver filename
driver_filepath = wd+driver_file      #Create full path name 
sensor = ctypes.CDLL(driver_filepath) #Load driver functions
#---------------------------------------------------------------

data = []
file.writelines('output, calc\n')


#Read and print one data point with the pressue sensor
for i in range(500):
    sensor_data_point = sensor.main()
    data.append(sensor_data_point)
    file.writelines(f'{sensor_data_point}, {(((sensor_data_point-1024)/60000)*100)-50}\n')



print(sensor_data_point)

file.close()

