import socket
import threading
import datetime
import asyncio
nodes=2
byte_limit=0x3FF
time_limit=5
date_time_now=datetime.datetime.now()

async def handle_client(client_soc,addr):
    assert isinstance(client_soc,socket.socket),"the function handle client the arguements need to be of type socket.socket"
    assert isinstance(addr,socket.socket),"the function handle client the arguements need to be of type socket.socket"
    while True:
        try:
            while True:

                request=client_socket.recv(byte_limit).decode("utf-8")

                 
                response=await handle_request(request)
                client_socket.send(response)
                 if request.lower()=="close":
                     client_socket.send("closed").encode("utf-8")
                     break
        execept Exception as e:
            print(f"Error with connection from {addr}: {e}")
            break
        finally:
            client_socket.close()
async def handle_request(request):
    request_dict={
            "Get message":await Message(),#just a hello world
            "Check_health":None,
            "Check_camera":None,
            "Check_images":None,
            "Sensor_data":await Sensor_data(),
            "Help":await request_dict.keys().encode("utf-8")
            }
    return request_dict[request]
async def Message():
    return f"this sever is online at: {date_time_now}".encode("utf-8")
async def Sensor_data():
    with open('../data_storage/sensor.csv','r') as f:
        data=f.readlines()
        data=''.join(data)
        return bytes(data,'utf-8')
    
