import socket
import tqdm
import os
import time

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host="192.168.22.5"
port=5050



s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected")

def send(filename):
    filesize=os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
  
#     progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
#     with open(filename, "rb") as f:
#         while True:
#             bytes_read=f.read(BUFFER_SIZE)
#     #         fr=f.read()
#     #         bytes_read=bytearray(fr)
#             if not bytes_read:
#                 break
#             s.sendall(bytes_read)
#             progress.update(len(bytes_read))
send("image0.jpg")
send("image.jpg")
send("image1.jpg")
send("image2.jpg")




# import socket
# 
# s=socket.socket()
# host = socket.gethostname()
# port = 12345
# 
# s.connect((host, port))
# s.send("Hello server!")
# f= open('image.jpg')
# print ("sending...")
# l = f.read(1024)
# while True:
#     print ('Sending')
#     s.send(l)
#     l=f.read(1024)
# f.close()
# print ('Done sending')
# print (s.recv(1024))
# s.close()
# 