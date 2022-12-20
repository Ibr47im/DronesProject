import socket
class UDPClient:  

    def __init__(self) -> None:
        self.server_address_port= ("127.0.0.1", 20001)
        self.MAX_BUFFER_SIZE= 1024

    def init_client(self):
        self.udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def connect(self):
        self.init_client()

    def send(self,msg_from_client):
        # Send to server using created UDP socket
        bytes_to_send = str.encode(msg_from_client)
        self.udp_client_socket.sendto(bytes_to_send, self.server_address_port)

    def receive(self):
        msg_from_server, address = self.udp_client_socket.recvfrom(self.MAX_BUFFER_SIZE)
        msg_from_server = msg_from_server.decode("utf-8")
        
        return msg_from_server
        
   
    

    

