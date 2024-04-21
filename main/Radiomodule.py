#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import time
import serial
import pandas as pd
import numpy as np
import threading
from memory_mangment import sensor_data
class Transciever:
	def __init__(self,data):
		self.transceive=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.Parity_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
		self.message="Hello world!"
		self.data=data
		self.chunk_size=240
		self.txt_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Tests/transmited_text.txt"
		self.csv_fname=sensor_data().fname
		self.reive_timelimit=time.time()+6
		self.recived=self.transceive.in_waiting()
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

			self.data=self.message
			for i in range(8):
				self.transceive.write(bytes(self.data,'utf-8'))
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
	def Transmit_test_text_file(self):
		"""Transmit a text file"""
		with open(self.txt_fname,'r') as f:
			self.data=list(f.read())
			self.data=[bytes(self.data[i],'utf-8').hex().encode() for i in range(len(self.data))]
		
		length=self.cal_bytes()
		index_right=[((x+1)*(self.chunk_size))for x in range(len)]
    	index_left=[x*(chunk_size) for x in range(number_of_loop)]
		for x in range(length,self.chunk_size):
			self.data[(x*self.chunk_size)+1:x*self.chunk_size]
	
		# data=",".join([bytes(data[i],'utf-8').hex().encode() for i in range(len(data))])
		# self.transceive.write(self.data.encode())
	def Received_test_text_file(self):
		"""receive a text file"""
		self.transceive.attachInterrupt(self.serial_interrupt)
		while self.event.is_set():
			data_read=self.transceive.read()
			if not data_read:
				break
		output="".join(chr(int(data_read.decode().split(',')[x],16)) for x in range(len(data_read.decode().split(','))))	
		print("message received:",output)
		
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
if __name__=='__main__':
	Transciever()


