#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import RPi.GPIO as GPIO
import time
import datetime
import pandas as pd
#pin 17
class AS312:
	def __init__(self,pin_number:int):
		self.pin_number=pin_number
		self.GPIO=GPIO
		self.GPIO.setmode(GPIO.BCM)
		self.GPIO.setup(self.pin_number,GPIO.IN)
		self.current_state=0
		self.timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	def read_state(self)->int:
		self.current_state =self.GPIO.input(self.pin_number)
		return self.current_state

	def append_data(self):
		data={
			"Motion Dectected": [self.current_state],
			"Timestamp": [self.timestamp]
		}
		df =pd.DataFrame(data)
		df.to_csv('sensor_data.csv',mode='a' ,index=False,header=False)

pir_sensor = AS312(17)

try:
	time.sleep(0.1)
	current_state =pir_sensor.read_state()
	timestamp=pir_sensor.timestamp
	print("GPIO pin %s is %s" % (pir_sensor.pin_number,current_state))
	if current_state == 1:
		print("Motion dectected")
	pir_sensor.append_data()
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
