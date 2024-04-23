#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#receiver
import serial
import time
import pandas as pd
lora = serial.Serial(port = '/dev/ttyS0' , baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
t_end=time.time()+6
ouputed_data=[]
while time.time()<t_end:
    if lora.in_waiting:
        lora.write(bytes("awk",'utf-8'))
        data = lora.readlines()#read data from other lora
        
        
        
        output=[data[i].decode().split(",") for i in range(len(data))]
        header=output[0]
        df=pd.DataFrame(output[output!=output[0]:],columns=[header])
        df.style
        print(data,output)

