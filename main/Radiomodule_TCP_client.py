import socket
from dotenv import load_dotenv
import asyncio
import os

byte_limit=0x3FF
load_dotenv()

async def handle_request(request,client):
    request_dict={
        "Message":client.send(request.encode("utf-8")),# a way to test a simple send /recive
        "Check_health":client.send(request.encode("utf-8")),# a way to test a simple send /recivetbd",# tell me about how much mem ,temp of semptem
        "Check_camera":client.send(request.encode("utf-8")),# a way to test a simple send /recivebd",#selection of tranport vid
        # a way to test a simple send /recivetbd",
        "Sensor_data":client.send(request.encode("utf-8")),# a way to test a simple send /recive
        "Help":client.send(request.encode("utf-8")),
        "close":client.send(request.encode("utf-8"))
    }
async def run_client():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_ip=os.getenv("SERVER_IP_ADDRESS")
    server_port=12345
    try:
        client.connect((server_ip,server_port))
    
        while True:
            request=input("\nEnter command: ")
            if request=="close":
                
                break
            await handle_request(request,client)

            response=client.recv(byte_limit)
            if response.lower()=="closed":
                break
            response=response.decode("utf-8")
            print(f"Response from server: {response}")

    except ConnectionRefusedError:
        print("the connection was refused")
        return 
    finally:
        client.close()
if __name__=="__main__":
    asyncio.run(run_client())
