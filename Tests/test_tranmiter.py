#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#Transmitter
import time
import serial
import base64
import threading
lora = serial.Serial(port='/dev/ttyS0',baudrate = 9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
t_end=time.time()+3
length=250
  

def read_image():
    with open('/home/mistaherd/Documents/Github/meshnetwork_in_forest/Images_camera/camera_output_2024-03-21_21-43-16.png', 'rb') as f:
        data=f.read()
    a=open("imagefile.txt","wb")
    a.write(data)
    with open("/home/mistaherd/Documents/Github/meshnetwork_in_forest/Tests/imagefile.txt",'rb') as d:
        data=d.read()
        lora.write(data)
read_image()
print("Tranmitting file will take a while")