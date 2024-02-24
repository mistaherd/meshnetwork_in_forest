#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
from picamera import PiCamera
from time import sleep
from datetime import datetime

timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

camera=PiCamera()
camera.start_preview()
sleep(2)
