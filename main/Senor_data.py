#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/.venv/lib/python3.11.9
import pandas as pd
from DHT22 import DHT22
from AS312 import AS312
from DFR0026 import DFR0026
import glob
import datetime

class Sensor_data:
	def __init__(self):
		self.dht22 = DHT22()
		self.humidity,self.temperature=self.dht22.Read_DHT22_data()
		self.AS312=AS312()
		self.timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		self.motion_detected =AS312.read_state(self.AS312)
		self.DF0026 =DFR0026()
		self.light_value=self.DF0026.read_voltage()
		self.fname="/home/mistaherd/Documents/Github/meshnetwork_in_forest/data_storage/sensor_data.csv"

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
if __name__=="__main__":
	Sensor_data()
