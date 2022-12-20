import socket
import sys
import json

class UDPServer:

    def __init__(self):
        self.server_ip     = "127.0.0.1"
        self.server_port   = 20001
        self.MAX_BUFFER_SIZE  = 1024
    

    def init_server(self):
        try:
            print("[UDP SERVER] Starting the UDP Server")
            self.udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self.udp_server_socket.bind((self.server_ip, self.server_port))

        except Exception as e:
            print("[UDP SERVER] Error creating a UDP client")
            print(e)
            sys.exit(0)# to get out of system 
    
    def start_server(self):
        print("UDP server up and listening")
        print('waiting for messages ...')
        self.message, self.address = self.udp_server_socket.recvfrom(self.MAX_BUFFER_SIZE)
        self.message = self.message.decode("utf-8")
        self.message=json.loads(self.message)
        return self.message ,self.address

    def send(self,msg_from_server=""):
        bytes_to_send= str.encode(msg_from_server)
        self.udp_server_socket.sendto(bytes_to_send, self.address)

            



