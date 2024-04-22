#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#receiver
import serial
import time
import io
lora = serial.Serial(port = '/dev/ttyS0' , baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)

while True:
    data = lora.readlines()#read data from other lora
    # data =[data[i][:-2].split(",") for i in range(len(data))]
    print(data)
