import tqdm
import os
SERVER_PORT = 5050
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
FORMAT = 'utf-8'
def saveimage(msg, client_socket):
    received = msg.encode().decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        reading = True
        while reading:
        
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    reading = False
                f.write(bytes_read)
                progress.update(len(bytes_read))
