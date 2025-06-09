import socket
from dotenv import load_dotenv
import asyncio
import os

byte_limit=0x3FF
load_dotenv()

def handle_request(request,client):
    
    client.send(request.encode("utf-8"))
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
            handle_request(request,client)

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
