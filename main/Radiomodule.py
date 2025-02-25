#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/new_env/lib/python3.9
import time
import serial
import pandas as pd
import numpy as np
import threading
import base64
import asyncio
from memory_mangment import sensor_data
class Transciever:
	def __init__(self):
        self.timeout_limit=2
		self.transceive_ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=self.timeout_limit)

		self.message="Hello world!"
		self.byte_size=10
		self.txt_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Tests/transmited_text.txt"
		self.png_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Images_camera/camera_output_2024-05-19_13_25_18.png"
		self.csv_fname=sensor_data().fname
		
		self.recived=self.transceive_ser.in_waiting
		self.event=threading.Event()
	def serial_interrupt(self):
		if self.recived:
			self.event.set()
	def cal_bytes(self)-> int:
		return len([bytes(self.data[i],'utf-8').hex() for i in range(len(self.data))])

    async def receiver_logic(self,byte_limit:bool):
        # Handle receiver 
        async with asyncio.timeout(self.timeout_limit):
            if not byte_limit:
                data = await self.transceive_ser.readline()
            else:
                data = await self.transceive_ser.read(self.byte_size))
        # decode
        
	def transceive_test_message(self,transceive:bool):
		"""send /recive a hello world"""
		if transceive:
			# self.message
			#transmite
			self.transceive_ser.write(bytes(self.message,'utf-8'))
			time.sleep(0.2)
		if not transceive:
			while time.time()< self.reive_timelimit:
				self.transceive_ser.attachInterrupt(self.serial_interrupt)
				if self.event.is_set():
					data_read=self.transceive_ser.readline()
					data=data_read.decode("utf-8")
					print("message received:",data)
					self.event.clear()
	# Text file
	def transceive_test_txt_file(self,transceive:bool):
		"""send /revive a txt file"""
		if transceive:
			with open(self.txt_fname,'r') as f:
				data=f.read()

			self.transceive_ser.write(bytes(data,'utf-8'))
			time.sleep(0.2)
		if not transceive:
			while time.time()< self.timelimit:
                self.transceive_ser.attachInterrupt(self.serial_interrupt)
				if self.event.is_set():
					data_read=self.transceive_ser.readline()
					data=data_read.decode("utf-8")
					print("message received:",data)
					self.event.clear()
					return data
	#test csv file
	def transceive_test_csv(self,transceive:bool):
		if transceive:
			with open('/home/mistaherd/Documents/Github/meshnetwork_in_forest/main/sensor_data.csv','r') as f:
				data=f.readlines()
			data=''.join(data)
			lora.write(bytes(data,'utf-8'))
			time.sleep(0.2)
		if not transceive:
			while time.time() <self.timelimit:
				self.transceive_ser.attachInterrupt(self.serial_interrupt)
				if self.event.is_set():
					data=self.transceive_ser.readlines()
					output=[data[i].decode()[:-1].split(",") for i in range(len(data))]
					df=pd.DataFrame(output)
					self.event.clear()
					return df
	#test png,jpg

	#Test png,jpg
	def Transcevie_png_file(self,transceive:bool):
		"""Transmit a PNG file"""
		if transceive:
			with open(self.png_fname, 'rb') as f:
				self.data = f.read()
			if self.cal_bytes()>self.chunk_size:
				chunks=[data[i:i+self.chunk_size] for i in range(0,len(self.data),self.chunk_size)]
				for chunk in range(len(chunks)):
					encoded_chunk=base64.b64encode(chunk)
					self.transceive_ser.write(encoded_chunk)
			else:
				raise ValueError("Image file must be corrupted")
		if not transceive:
			output=[]
			self.transceive_ser.attachInterrupt(self.serial_interrupt)
			if self.event.is_set():
				while(self.transceive_ser.read() != b''):
					data_read = self.transceive_ser.read()
					print("bytes reviced %a"%data_read)
					output.append(base64.b64decode(data_read))
				output=b"".join(output)
				self.event.clear()
				return output
	def transive_choice(self,arugement):
		""" run this for demo"""
		if not self.event.is_set():
			#transmit something
			self.transmit=True
			choice ={
				1:lambda :self.transceive_test_message(self.transmit),
				2:lambda :self.transceive_test_txt_file(self.transmit),
				3:lambda :self.transceive_test_csv(self.transmit),
				4:lambda :self.Transcevie_png_file(self.transmit)}
			choice[arugement]()
		#revived somthing
		self.transmit=False
		choice[self.user_message]()
if __name__=='__main__':
	Transciever()
