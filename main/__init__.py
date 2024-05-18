#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import unittest
from memory_mangment import sensor_data,Memory_tester
from DHT22 import DHT22
from AS312 import AS312
from DFR0026 import DFR0026
sensor_data_object=sensor_data()
dht22_instance=DHT22()
AS312_instance=AS312()
temp=sensor_data_object.temperature()
hum=sensor_data_object.humidity()
memorytest_obj=Memory_tester

class test_project_code(unittest.TestCase):
    # DHT22
    def test_DHT22_output_type(self):
       
        self.assertIsInstance(dht22_instance.Read_DHT22_data, tuple)

    def test_DHT_22_temp_output_type(self):
        self.assertIsInstance(temp, (int,float) )

    def test_DHT22_temp_range(self):
        self.assertGreaterEqual(temp,-30.3)
        self.assertLessEqual(temp,80.3)

    def test_DHT22_hum_output_type(self):
        self.assertIsInstance(hum,(int,float))

    def test_DHT22_hum_range(self):
        self.assertGreaterEqual(hum,0.0)
        self.assertLessEqual(hum,100.0)
     # DFR0026 
    def test_DFR0026_out_type(self):
        self.assertIsInstance(DFR0026().read_voltage(),float)
    def test_DFR0026_out_range(self):
        self.assertLessEqual(DFR0026().read_voltage(),5)
        self.assertGreaterEqual(DFR0026().read_voltage(),0)
     #AS312
    def test_AS312_out_type(self):
         self.assertIsInstance(AS312_instance.read_state,bool)
     # Raspberry Pi VR 220 Camera
    def test_Raspberry_Pi_VR220_out_shape(self):
         self.assertEqual(Read_Raspberry_PiVR220.shape,(1920,1080,3))
    
    
    # memory module
    def Test_memory_silicon_power_32GB(self):
        self.assertLessEqual(memorytest_obj.check_memory,32e9)
        self.assertGreaterEqual(memorytest_obj.check_memory,0)
    # radio module
if __name__ == '__main__':
    unittest.main()


