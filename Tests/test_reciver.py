#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#receiver
import serial
import time
import pandas as pd
import base64
import re
import threading
lora = serial.Serial(port = '/dev/ttyS0' , baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
t_end=time.time()+6
stored_data=[]
end_of_file=b"\n EOF \n"
def read_image(data):
    while True:
        if re.match(end_of_file,data):
            break
        stored_data.append(data)
while time.time()<t_end:
    # print(time.time(),t_end)
    if lora.in_waiting:
        data = lora.read()
        if re.match(data,b"PNG")
        thread=threading.Thread(target=read_image,args=(data,))
        thread.start()
        
        output=b"".join(stored_data)
        f=open('output.png','wb')
        f.write(base64.b64decode(output))
