#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import RPi.GPIO as GPIO
import time
import datetime
import pandas as pd
#pin 17
class AS312
def __init__(self):
	self.pir_sensor=17
	self.GPIO.setmode(GPIO.BCM)

pir_sensor =17


GPIO.setmode(GPIO.BCM)

GPIO.setup(pir_sensor, GPIO.IN)
current_state = 0
try:
	time.sleep(0.1)
	current_state =GPIO.input(pir_sensor)
	timestamp=datetime.datetime.now()
	timestamp=timestamp.strftime("%Y-%m-%d %H:%M:%S")
	if current_state == 1:
		print("GPIO pin %s is %s" % (pir_sensor,current_state))
	print("GPIO pin %s is %s" % (pir_sensor,current_state))
	data={
		"Motion detected":[current_state],
		"timestamp":[timestamp]
	}
	df =pd.DataFrame(data)
	df.to_csv('sensor_data.csv',mode='a' ,index=False,header=False)
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
