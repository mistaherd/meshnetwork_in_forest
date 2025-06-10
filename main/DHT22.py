#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/.venv/lib/python3.11.9
import adafruit_dht

import board
import pandas as pd
class DHT22:
##Set DATA pin to pin 4
    def __init__(self):
        """this will setup the  data pin  for  DHT2"""
        # self.dhtDevice =adafruit_dht.DHT22(board.D4)
        self.dhtDevice =adafruit_dht.DHT11(board.D4)
        self.humidity=self.dhtDevice.humidity
        self.temperature=self.dhtDevice.temperature
    def Read_DHT22_data(self)-> tuple[float,float]|Tuple[NULL,NULL]:
        """This  will setup a DHT instance and  return the data from the sensor"""
        try:
            return self.temperature,self.humidity
        except RuntimeError as e:
            print(f"Error reading sensor: {e}")
            return Null,Null
if __name__ =="__main__":
    DHT22()
