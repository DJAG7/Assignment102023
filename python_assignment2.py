#Importing library required for psutil.cpu_percent() functions 
import psutil

#for an indefinite while loop
n=0

#predefined percentage
threshold= int(input("Monitoring CPU program \n \n Enter the threshold to recieve alerts if CPU usage percentage goes "))

#Monitoring CPU usage
while (n==0):
    cpu_usage=psutil.cpu_percent(interval=2)
    #Testing Threshold
    if(cpu_usage<threshold):
        print("Monitoring CPU usage:" , cpu_usage, "%")
    if (cpu_usage>=threshold):
        print("Alert, CPU usage exceeds threshold.", cpu_usage, "%")
