#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/.venv/lib/python3.11.9
from Senor_data import Sensor_data
from Camera_alt import camera
from Radiomodule import Transciever
import sys
sen_data=sensor_data()
camera_obj=camera()
mem_obj=Memory_tester()
transive_obj=Transciever()
sen_data.write_append_csv()
camera_obj.run
mem_obj.error_check()

#initialize nodes
