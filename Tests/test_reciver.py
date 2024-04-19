#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#receiver
import serial
import time

lora = serial.Serial(port = '/dev/tty10' , baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
t_end= time.time()+6
while time.time()<t_end:
    data_read = lora.readline()#read data from other lora
    data = data_read.decode("utf-8")#convert byte into string
    print(data)