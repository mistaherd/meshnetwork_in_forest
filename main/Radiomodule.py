#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import time
import serial
import pandas as pd
import numpy as np
import threading
import subprocess
from memory_mangment import sensor_data
class Transciever:
	def __init__(self,data):
		self.transceive=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.Parity_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
		self.message="Hello world!"
		self.data=data
		self.chunk_size=240
		self.mesh_fname="../bash_scrpits/mesh.sh"
		self.txt_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Tests/transmited_text.txt"
		self.csv_fname=sensor_data().fname
		self.timelimit=time.time()+6
		self.recived=self.transceive.in_waiting
		self.event=threading.Event()
	def serial_interrupt(self):
		if self.recived:
			self.event.set()
	def cal_bytes(self)-> int:
		return len([bytes(self.data[i],'utf-8').hex() for i in range(len(self.data))])

	# hello world
	def transceive_test_message(self,transceive:bool):
		"""send /recive a hello world"""
		if transceive:
			# self.message
			#transmite
			self.transceive.write(bytes(self.message,'utf-8'))
			time.sleep(0.2)
		if not transceive:
			while time.time()< self.reive_timelimit:
				self.transceive.attachInterrupt(self.serial_interrupt)
				if self.event.is_set():
					
					data_read=self.transceive.readline()
					data=data_read.decode("utf-8")
					print("message received:",data)
					self.event.clear()
	# Text file
	def transceive_test_txt_file(self,transceive:bool):
		"""send /revive a txt file"""
		if transceive:
			with open(self.txt_fname,'r') as f:
				data=f.read()
			
			self.transceive.write(bytes(data,'utf-8'))
			time.sleep(0.2)
		if not transceive:
			while time.time()< self.timelimit:
				self.transceive.attachInterrupt(self.serial_interrupt)
				if self.event.is_set():
					data_read=self.transceive.readline()
					data=data_read.decode("utf-8")
					print(data)
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
				self.transceive.attachInterrupt(self.serial_interrupt)
				if self.event.is_set():
					data=self.transceive.readlines()
					output=[data[i].decode()[:-1].split(",") for i in range(len(data))]
					df=pd.DataFrame(output)
					print(df)

	#Test png,jpg
	def Transcevie_png_file(self):
		"""Transmit a PNG file"""
		if transceive:
			with open(self.png_fname, 'rb') as f:
				data = f.read()
			for i in range(0,len(data),self.chunk_size):
				self.transceive.write(data[i:i+self.chunk_size])
		if not transceive:
			output=[]
			self.transceive.attachInterrupt(self.serial_interrupt)
			if self.event.is_set():
				while(self.transceive.read() != b''):
					data_read = self.transceive.read()
					output.append(data_read)	
	def transive_choice(self):
		""" run this for demo"""
		if not self.event.is_set():
			#transmit something
			self.user_message=int(input("enter what is transmited:\n\r 1:hello world \n\r 2:text file \n\r 3:csv file \n\r 4:PNG\n"))
			self.transmit=True
			choice ={
				1: lambda :self.transceive_test_message(self.transmit),
				2:lambda :self.transceive_test_txt_file(self.transmite),
				3: lambda :transceive_test_csv(self.transmit),
				4:lambda :Transcevie_png_file(self.transmit),
			}
			choice[self.user_message]()
		#revived somthing
		self.transmit=False
		choice[self.user_message]()
if __name__=='__main__':
	Transciever()


