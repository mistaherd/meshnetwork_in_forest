#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/.venv/lib/python3.11.9
import socket
from dotenv import load_dotenv

load_dotenv()
class Node:
	Link= {}
	Distance=0
	Node_number=0
	Node_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	def __init__(self):
		self.Node_socket.recv()
	
