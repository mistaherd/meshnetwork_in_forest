import socket
import threading
import datetime
import asyncio
import subprocess
import re
import os
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
        except Exception as e:
            print(f"Error with connection from {addr}: {e}")
            break
        finally:
            client_socket.close()


async def handle_request(request):
    request_dict={
            "Get message":await Message(),#just a hello world
            "Check_health":await Check_health(),
            "Check_camera":None,
            "Check_images":None,
            "Sensor_data":await Sensor_data(),
            "Help":await request_dict.keys().encode("utf-8")
            }
    return request_dict[request]

async def Message():
    return f"this sever is online at: {date_time_now}".encode("utf-8")

async def Check_health():
    command=["bash","../bash_scrpits/sys_diag.sh"]
    subprocess.run(command, check=True)
    with open('../data_storage/sys_dia.txt') as f:
        data=f.readlines()
        data=''.join(data)
        return bytes(data,'utf-8')

async def Check_camera():
    command=["bash","../bash_scrpits/camerea.sh"]
    subprocess.run(command, check=True)
    command=["bash","../bash_scrpits/Get_most_recent_pic.sh"]
    Imagefile=subprocess.run(command, capture_output=True, text=True).stdout.strip()
    with open (imagefile,'rb') as f:
        image_data=f.read()
        image_size=len(image_data)


async def Sensor_data():
    with open('../data_storage/sensor.csv','r') as f:
        data=f.readlines()
        data=''.join(data)
        return bytes(data,'utf-8')

