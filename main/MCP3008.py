#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#This code  is for  DFR0553 and DFR0026
import sys
import time
import pandas
import datetime
import glob
sys.path.append('../')
from gpiozero import MCP3008
class ADC:
        def __init__(self):
                self.channel_port=0
                self.device=0
                self.timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        def Read_chanel(self,GPIO_port:int)->:
                return MCP3008(channel=self.channel,device=self.device,port=GPIO_port)
class DFR0026:
        def __init__(self):
                self.fname="sensor_data.csv"
                self.adc=ADC()  
                self.GPIO_port=9
        def Store_light_data_tc_csv(self):
                light_value=self.adc.Read_chanel(self.GPIO_port)
                data=[(light_vaule,self.adc.timestamp)]
                df = pd.DataFrame(data,columns=['Light(lux)','timestamp'])
                if glob.glob(self.fname):
                        df.to_csv(self.fname,mode='a' ,index=False,header=False)
                else:
                        df.to_csv(self.fname,mode='w' ,index=False)




