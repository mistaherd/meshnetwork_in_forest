#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
from DFRobot_ADS1115 import ADS1115
import time
class DFR0026():
    def __init__(self):
        self.ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
        self.ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
        self.ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
        self.ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
        self.ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
        self.ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
        self.ads1115 = ADS1115()
        self.ads1115.set_addr_ADS1115(0x48)
        self.ads1115.set_gain(self.ADS1115_REG_CONFIG_PGA_6_144V)
        self.adc_channel=0
    def read_voltage(self):
        return self.ads1115.read_voltage(self.adc_channel)
        #time.sleep(0.2) after read it
if __name__=="__main__":
    DFR0026()