#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#Transmitter
import time
import serial

lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

while time.time() <time.time()+6:
    with open('transmited_text.txt', 'r') as f:
        data=f.read()
        
    lora.write(bytes(data,'utf-8'))
    time.sleep(0.2)