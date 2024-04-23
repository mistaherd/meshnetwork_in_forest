#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#Transmitter
import time
import serial
import base64
lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
t_end=time.time()+3
length=240
with open('/home/mistaherd/Documents/Github/meshnetwork_in_forest/Images_camera/camera_output_2024-03-21_21-43-16.png', 'rb') as f:
        data=f.read()+b"\n EOF \n"
        data=[data[i:i+length] for i in range(0,len(data),length)]

while time.time()< t_end:

    lora.write(data[0])
    # time.sleep(0.2)
    if lora.in_waiting:
        if lora.readline().decode("utf-8") =="awk":
            break