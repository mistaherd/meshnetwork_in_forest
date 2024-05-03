#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
from memory_mangment import sensor_data,Memory_tester
from Camera_alt import camera
from Radiomodule import Transciever
import sys
sen_data=sensor_data()
camera_obj=camera()
mem_obj=Memory_tester()
transive_obj=Transciever()

sen_data.write_append_csv()
#camera_obj.run
mem_obj.error_check()
#Then we transmit th
transive_obj.transive_choice()
