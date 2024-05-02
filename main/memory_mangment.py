#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import pandas as pd
from DHT22 import DHT22
from AS312 import AS312
from DFR0026 import DFR0026
import glob
import datetime
import re 
import subprocess
class sensor_data:
	def __init__(self):
		self.dht22 = DHT22()
		self.humidity,self.temperature=self.dht22.Read_DHT22_data()
		self.humidity,self.temperature = 0,0
		self.AS312=AS312()
		self.timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		self.motion_detected =AS312.read_state(self.AS312)
		self.DF0026 =DFR0026()
		self.light_value=self.DF0026.read_voltage()
		self.fname="sensor_data.csv"

	def write_append_csv(self):
		data = { "Timestamp" : self.timestamp,
			"Temperature(oc)" : self.temperature,
			"Humidity(%)" : self.humidity,
			"Light(lux)" :self.light_value,
			"Motion Detected": self.motion_detected
			}
		print("this csv contains the following data:%s"%data)
		df = pd.DataFrame(data)
		if glob.glob(self.fname):	
			df.to_csv(self.fname,mode='a' ,index=False,header=False)
		else:
			df.to_csv(self.fname,mode='w' ,index=False)
class Memory_tester():
	def __init__(self):
		self.units={"K":10e3,"M": 10e6,"G":10e9}
		self.regex ="\d{4}\.\[0-9]{1,3}[K,M,G]"
		self.fname="../bash_scrpits/memorytest.sh" 
		self.output_bash=subprocess.check_output(["bash",self.fname],universal_newlines=True)
	
	def check_memory(self):
		try:
			if re.search(self.regex,self.output_bash):
				value,unit=match.group(0).split()
				try:
					return float(value)*self.units[unit]
				except KeyError:
					raise ValueError(f"unknown unit: {unit}")
			
		except subprocess.CalledProcessError as e:
			raise ValueError(f"Error running script:{e.output}")
	
	def error_check(self):
		mem=self.check_memory()
		max=32*10e9
		if mem >= 0.2* max:
			raise MemoryError("memory on pi is about to  used up")

if __name__=="__main__":
	sensor_data()
	Memory_tester()