#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import adafruit_dht 
import board
import datetime

class DHT22:
##Set DATA pin to pin 4
    def __init__(self,boardmethod):
        # self.dhtDevice =adafruit_dht.DHT22(board.D4)
        self.dhtDevice =adafruit_dht.DHT11(boardmethod)
    def Read_data(self)-> tuple[float,float,datetime.datetime]:
        try:
            Humidity=self.dhtDevice.humidity
            Temperature=self.dhtDevice.temperature
            timestamp =datetime.datetime.now()
            return Temperature,Humidity,timestamp
        except RuntimeError as e:
            print(f"Error reading sensor: {e}")
            return None, None
if __name__ =="__main__":
    dhobj=DHT22(board.D4)
    dhobj.Read_data()
