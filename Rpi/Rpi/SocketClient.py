import socket
import time
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.10.102"
ADDR = (SERVER, PORT)

movements = []
class Socket():
    
    def start(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)

    def send(self,msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        movement = self.client.recv(2048).decode(FORMAT)
        while movement != "done":
            movements.append(movement)
            movement = self.client.recv(2048).decode(FORMAT)
            
    def getmovements(self):
        return movements
