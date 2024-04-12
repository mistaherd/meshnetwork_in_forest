#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import time
import serial
import threading
class Transciever:
	def __init__(self,data):
		self.transceive=serial.Serial(port='/dev/tty50',baudrate=9600,parity=serial.Parity_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
		self.message="Hello world! "
		self.data=data
		self.txt_fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/Tests/transmited_text.txt"
		self.recived=self.transceive.in_waiting
		self.event=threading.Event()
	def serial_interrupt(self):
		if self.recived:
			self.event.set()
	# hello world 
	def Transmit_test_message(self):
		"""send a simple hello world"""
		self.transceive.write(bytes(self.message,'utf-8'))
		time.sleep(0.2)
	def Recive_test_message(self):
		"""recive a simple message"""
		self.transceive.attachInterrupt(serial_interrupt)
		if self.event.is_set():
			data_read=self.transceive.readline()
			s=data_read.decode("utf-8")
			print("message recived:",s)
	# Text file
	def Tranmist_test_text_file(self):
		"""Transmit a text file"""
		with open(self.txt_fname,'r') as f:
			data=f.read()
		self.transceive.writeline(data.encode())
	def Recevive_test_text_file(self):
		"""Transmit a text file"""
		self.transceive.attachInterrupt(serial_interrupt)
                if self.event.is_set():
			data_read=self.transceive.readline()
                        s=data_read.decode("utf-8")
                        print("message recived:",s)
	#test csv file
	
	#Test png,jpg
