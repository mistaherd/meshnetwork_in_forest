#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#receiver
import serial
import time
import pandas as pd
import base64
import re
import asyncio
async def reciver_png():
    lora = serial.Serial(port = '/dev/ttyS0' , baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)
    
    stored_data=[]
    end_of_file=b"\n EOF \n"
    while True:
        data = await lora.read(1)
        if not data:
            break
        if re.match(end_of_file,data):
            break
        stored_data.append(data)
    output=b"".join(stored_data)
    f=open('output.png','wb')
    f.write(base64.b64decode(output))
    f.close()
async def main():
    await reciver_png()
async.run(main())
