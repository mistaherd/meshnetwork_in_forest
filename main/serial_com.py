#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/new_env/lib/python3.9
import time
import serial
import pandas as pd
import re
import numpy as np
import threading
import base64
import asyncio
from memory_mangment import sensor_data
class Transciever:
	def __init__(self):
        self.timeout_limit=2
		self.transceive_ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=self.timeout_limit)
        # 868MHz/433MHz fc =434 to 216 
        self.byte_limit=300
        self.ack_pattern=r"ack\d+"
	    self.tx/rx=false
        self.message="Hello world!"
		self.byte_size=10
    
		self.txt_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Tests/transmited_text.txt"
		self.png_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Images_camera/camera_output_2024-05-19_13_25_18.png"
		self.csv_fname=sensor_data().fname
		
		self.serial_wait=self.transceive_ser.in_waiting
		self.event=threading.Event()
	def serial_interrupt(self):
		if self.recived:
			self.event.set(
	def cal_bytes(self)-> int:
		return len([bytes(self.data[i],'utf-8').hex() for i in range(len(self.data))])
    def packet_endswith_reciver(self,data):
        if not isinstance(data, bytes):
            raise TypeError("Input data must be a byte string.")
        matches="".join(re.findall(self.ack_pattern,data, re.IGNORECASE))
        # last digit is if  the data has been recivered or not
        # the first what packet is are we currently onand second to be how many packet there is
        lookat=matches[3:]
        lookat[0]==f"{int(lookat[0])+1}"

    async def receiver_logic(self,byte_limit:bool):
        # Handle receiver 
        async with asyncio.timeout(self.timeout_limit):
            if not byte_limit:
                data = await self.transceive_ser.readline()
            else:
                data = await self.transceive_ser.read(self.byte_size)
        # decode
        
