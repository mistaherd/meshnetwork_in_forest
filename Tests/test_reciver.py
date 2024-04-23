#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#receiver
import serial
import time
import pandas as pd
import base64
lora = serial.Serial(port = '/dev/ttyS0' , baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
t_end=time.time()+6
ouputed_data=[]
while time.time()<t_end:
    if lora.in_waiting:
        data = lora.read()
        f=open('output.png','wb')
        f.write(base64.b64decode(data))
        lora.write(bytes("awk",'utf-8'))

