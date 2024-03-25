#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
from picamera2 import Picamera2,Preview
from time import sleep
from datetime import datetime
class Raspberry_Pi_VR_220:
    def __init__(self):
        """setup an instan  for the  camera"""
        self.timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.fname ='/home/mistaherd/Documents/Github/meshnetwork_in_forest/Images_camera/{}.png'.format(self.timestamp)
        self.camera=PiCamera()
        self.camera_config=self.camera.create_preview_configuration()
        self.timeamount=2
    def take_pic(self)-> str:
        """this will take  a picture from camera"""
        self.camera.configure(self.camera_config)
        self.camera.start_preview(Preview.QTGL)
        self.camera.start()
        sleep(self.timeamount)
        self.camera.capture_file(self.fname)
        return self.fname
if __name__=="__main__":
    Raspberry_Pi_VR_220()
