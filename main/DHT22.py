#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
#liberiers
#
import adafruit_dht 
import board
import time

##Set DATA pin to pin 4
dhtDevice =adafruit_dht.DHT22(board.D4)
Temperature_c=dhtDevice.temperature
Humidity=dhtDevice.humidity
#Print Temperature and Humidity on Shell window
print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(Temperature_c,humidity))
# while True:
#    #Read Temp and Hum from DHT22
#    h,t = dht.read_retry(dht.DHT22, DHT)
#    #Print Temperature and Humidity on Shell window
#    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))
#    sleep(5) #Wait 5 seconds and read again
# print("Hello world")
