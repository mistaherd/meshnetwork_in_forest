#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/new_env/lib/python3.9
import RPi.GPIO as GPIO
import time
#pin 17
class AS312:
	def __init__(self):
		"connect the AS312 to pin 17"
		self.pin_number=17
		self.GPIO=GPIO
		self.GPIO.setmode(GPIO.BCM)
		self.GPIO.setup(self.pin_number,GPIO.IN)
		self.current_state=0
	def read_state(self)->bool:
		time.sleep(0.1)
		self.current_state =bool(self.GPIO.input(self.pin_number))
		return self.current_state
if __name__=="__main__":
	AS312()
