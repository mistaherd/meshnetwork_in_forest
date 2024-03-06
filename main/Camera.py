#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
from picamera import PiCamera
from time import sleep
from datetime import datetime
class Raspberry_Pi_VR_220:
    def __init__(self):
        """setup an instan  for the  camera"""
        self.timestamp=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.fname ='/home/mistaherd/Documents/Github/meshnetwork_in_forest/{}.png'.format(self.timestamp)
        self.camera=PiCamera()
        self.timeamount=2
    def take_pic(self)-> str:
        """this will take  a picture from camera"""
        self.camera.start_preview()
        sleep(self.timeamount)
        self.camera.capture(self.fname)
        self.stop_preview()
        return self.fname
camera=Raspberry_Pi_VR_220()
picture=camera.take_pic()