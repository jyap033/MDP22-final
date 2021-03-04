import socket
import time
import os
import tqdm
import threading
HEADER = 4096
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.22.5"
ADDR = (SERVER, PORT)
SEPARATOR = "<SEPARATOR>"


class Socket():
    def start(self):
        try:
            print("connecting to server...")
            self.movements = []
            self.client = socket.socket()
            self.client.connect(ADDR)
            print("connected to server")
        except:
            self.start()
        
            
    def send(self,msg):
        message = msg.encode(FORMAT)
        self.client.send(message)
        movement = self.client.recv(2048).decode(FORMAT)
        while movement != "done":
            self.movements.append(movement)
            movement = self.client.recv(2048).decode(FORMAT)
    def sendimage(self, filename):
         filesize=os.path.getsize(filename)
         self.client.send(f"{filename}{SEPARATOR}{filesize}".encode())
         progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
         with open(filename, "rb") as f:
            connection = True
            while connection:
                bytes_read=f.read(HEADER)
                if not bytes_read:
                    connection = False
                self.client.sendall(bytes_read)
                progress.update(len(bytes_read))

    def getmovements(self):
        return self.movements    
        

# s.("hi")
# s.send("there")
# s=Socket()
# s.start()
# s.sendimage("image0.jpg")




