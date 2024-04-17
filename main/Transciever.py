#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import time
import serial
import pandas as pd
import numpy as np
import threading
from memory_mangment import sensor_data
class Transciever:
	def __init__(self,data):
		self.transceive=serial.Serial(port='/dev/tty50',
								baudrate=9600,
								parity=serial.Parity_NONE,
								stopbits=serial.STOPBITS_ONE,
								bytesize=serial.EIGHTBITS,
								timeout=1)
		self.message="Hello world! "
		self.data=data
		self.txt_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Tests/transmited_text.txt"
		self.csv_fname=sensor_data().fname
		self.recived=self.transceive.in_waiting
		self.event=threading.Event()
	def serial_interrupt(self):
		if self.recived:
			self.event.set()
	# hello world
	def Transmit_test_message(self):
		"""send a simple hello world"""
		self.message=list(self.message)
		self.message=[bytes(self.message[i],'utf-8').hex() for i in range(len(self.message))]
		self.transceive.write(",".join(self.message).encode())
		time.sleep(0.2)
		
	def Receive_test_message(self):
		"""receive a simple message"""
		self.transceive.attachInterrupt(self.serial_interrupt)
		if self.event.is_set():
			data_read=self.transceive.readline()
			
			

	# Text file
	def Tranmist_test_text_file(self):
		"""Transmit a text file"""
		with open(self.txt_fname,'r') as f:
			data=f.read()
		self.transceive.writeline(data.encode())
	def Recevive_test_text_file(self):
		"""receive a text file"""
		self.transceive.attachInterrupt(self.serial_interrupt)
		while self.event.is_set():
			data_read=self.transceive.read()
			if not data_read:
				break
			s=data_read.decode("ascii")
			print("message received:",s)
	
	#test csv file
	def Tranmist_test_csv_file(self):
		"""Transmit a csv file"""
		with open(self.csv_fname,'rb') as f:
			data= f.read()
		self.transceive.write(data)
	def Recevive_test_csv_file(self):
		"""receive a csv file"""
		self.transceive.attachInterrupt(self.serial_interrupt)
		if self.event.is_set():
			data=self.transceive.readlines()
			output=[data[i].decode()[:-2] for i in range(len(data))]
			header=output[0]
			df=pd.DataFrame(output[output!=output[0]:],columns=[header])

	#Test png,jpg
	def Transmit_test_png_file(self):
		"""Transmit a PNG file"""
		with open(self.png_fname, 'rb') as f:
			data = f.read()
		self.transceive.write(data)
	def Receive_test_png_file(self):
		"""Receive a PNG file"""
		self.transceive.attachInterrupt(self.serial_interrupt)
		if self.event.is_set():
			data_read = self.transceive.readlines()
			
			



