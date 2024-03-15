#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import pandas as pd
# from DHT22 import DHT22

# from AS312 import AS312
# from MCP3008 import DF0026
import pandas as pd
import glob
import re 
import subprocess
class sensor_data:
	def __init__(self):
		self.dht22 = DHT22()
		self.humidity,self.temperature,self.timestamp=self.dht22.Read_DHT22_data()
		self.AS312=AS312(17)
		self.motion_dected =AS312.read_state()
		self.DF0026 =DF0026()
		self.light_value=self.DF0026.Read_data()
		self.fname="sensor_data.csv"
	def write_append_csv(self):
		data = { "Timestamp" : self.timestamp,
			"Temperature(oc)" : self.Temperature,
			"Humidity(%)" : self.humidity,
			"Light(lux)" :self.light_value,
			"Motion Dected": self.motion_dected
			}
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
