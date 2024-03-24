#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
from memory_mangment import sensor_data,Memory_tester
from Camera import Raspberry_Pi_VR_220
camera=Raspberry_Pi_VR_220()
camera.take_pic()
sen_data=sensor_data()
sen_data.write_append_csv()
