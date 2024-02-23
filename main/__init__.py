#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import unittest
# from protest import Read_DHT22,Read_MCP3008,Read_AS312,Read_Raspberry_PiVR220,Read_Memory_module
from DHT22 import DHT22
import board
dht22_instance=DHT22()
hum,temp,ts=dht22_instance.Read_DHT22_data()
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
    # def test_DFR0026_MCP3008_out_type(self):
    #     self.assertIsInstance(Read_MCP3008,float)
    # def test_DFR0026_MCP3008_out_range(self):
    #     self.assertLessEqual(Read_MCP3008(2,34),5)
    #     self.assertGreaterEqual(Read_MCP3008(2,34),0)
     #AS312
     def test_AS312_out_type(self):
         self.assertIsInstance(Read_AS312,bool)
     # Raspberry Pi VR 220 Camera
     def test_Raspberry_Pi_VR220_out_shape(self):
         self.assertEqual(Read_Raspberry_PiVR220.shape,(1920,1080,3))
     # battery 
    
    # # memory module
    
    # def Test_memory_module_turbo_1GB_size(self):
    #     #testing  turbo 1GB
    #     self.assertLessEqual(Read_Memory_module,1e9)
    #     self.assertGreaterEqual(Read_Memory_module,0)
    # def Test_memory_silicon_power_32GB(self):
    #     self.assertLessEqual(Read_Memory_module,32e9)
    #     self.assertGreaterEqual(Read_Memory_module,0)
    # radio module
if __name__ == '__main__':
    unittest.main()


