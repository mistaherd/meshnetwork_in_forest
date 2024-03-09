#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import adafruit_dht 
import board
import datetime
import pandas as pd
import glob
class DHT22:
##Set DATA pin to pin 4
    def __init__(self):
        """this will setup the  data pin  for  DHT2"""
        # self.dhtDevice =adafruit_dht.DHT22(board.D4)
        self.dhtDevice =adafruit_dht.DHT11(board.D4)
        self.timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.humidity=self.dhtDevice.humidity
        self.temperature=elf.dhtDevice.temperature
    def Read_DHT22_data(self)-> tuple[float,float,str]:
        """This  will setup a DHT instance and  return the data from the sensor"""
        try:
            return self.temperature,self.humidity,self.timestamp
        except RuntimeError as e:
            print(f"Error reading sensor: {e}")
            return None, None
dht_sensor = DHT22()
