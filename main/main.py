#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/new_env/lib/python3.9
from memory_mangment import sensor_data,Memory_tester
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
#Then we transmit th
transive_obj.transive_choice(sys.argv[1])
if len(sys.argv) ==1:
	print("enter what is transmited:\n\r1:hello world \n\r2:text file \n\r3:csv file\n\r4:PNG\n\r>")
else:
	sen_data=sensor_data()
	camera_obj=camera()
	mem_obj=Memory_tester()
	transive_obj=Transciever()
	sen_data.write_append_csv()
	camera_obj.run
	mem_obj.error_check()
	#Then we transmit th
	transive_obj.transive_choice(sys.argv[1])
