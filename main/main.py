#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
# from memory_mangment import sensor_data,Memory_tester
# from Camera_alt import camera
# sen_data=sensor_data()
# camera=camera()
# sen_data.write_append_csv()
from Radiomodule import Transciever as tr
tr.transceive_test_message(False)
