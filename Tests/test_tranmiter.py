#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#Transmitter
import time
import serial

lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
while input("send messages")=='y':
    with open('/home/mistaherd/Documents/Github/meshnetwork_in_forest/main/sensor_data.csv', 'r') as f:
        data=f.readlines()
    data=''.join(data)

    lora.write(bytes(data,'utf-8'))
    time.sleep(0.2)