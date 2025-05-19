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

async def handle_client(client_socket,addr):
    assert isinstance(client_socket,socket.socket),"the function handle client the arguements need to be of type socket.socket"
    assert isinstance(addr,tuple),"the function handle client the arguements need to be of type socket.socket"
    
    try:
        while True:

            request=client_socket.recv(byte_limit).decode("utf-8")

            if request.lower()=="close":
                client_socket.send("closed").encode("utf-8")
                break
             
            response=await handle_request(request,client_socket)
            if response!=None:
                client_socket.send(response)
            
    except Exception as e:
        print(f"Error with connection from {addr}: {e}")
        #break
    finally:
        client_socket.close()


async def handle_request(request,client_socket):
    print(f"{request=}")
    match request:
        case "Message":
            return await Message()  # Just a hello world
        case "Check_health":
            return await Check_health()
        case "Check_camera":
            return await Check_camera(client_socket)
        case "Sensor_data":
            return await Sensor_data()
        case "Help":
            help_message = "Available commands: Message, Check_health, Check_camera, Sensor_data, Help"
            return help_message.encode("utf-8")
        case _:  # Default case if no match is found
            return None  #  

async def Message():
    return f"this sever is online at: {date_time_now}".encode("utf-8")

async def Check_health():
    command=["bash","../bash_scrpits/sys_diag.sh"]
    subprocess.run(command, check=True)
    with open('../data_storage/sys_dia.txt') as f:
        data=f.readlines()
        data=''.join(data)
        return bytes(data,'utf-8')

async def Check_camera(client_socket):
    command=["bash","../bash_scrpits/camerea.sh"]
    subprocess.run(command, check=True)
    command=["bash","../bash_scrpits/Get_most_recent_pic.sh"]
    Imagefile=subprocess.run(command, capture_output=True, text=True).stdout.strip()
    with open (imagefile,'rb') as f:
        image_data=f.read()
        image_size=len(image_data)
    client_socket.sendall(image_size.to_bytes(4,'big'))
    client_socket.sendall(image_data)
    return None

async def Sensor_data():
    with open('../data_storage/sensor.csv','r') as f:
        data=f.readlines()
        data=''.join(data)
        return bytes(data,'utf-8')
async def run_server():
    hostname=socket.gethostname()

    server_ip="0.0.0.0"
    port=12345
    server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((server_ip,port))
        server.listen(5)
        print(f"Server listening on {server_ip}:{port}")

        
        client_socket,client_address=server.accept()
        print(f"Accepted connection from {client_address[0]} : {client_address[1]}")
        await handle_client(client_socket,client_address)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()
if __name__=="__main__":
    asyncio.run(run_server())
