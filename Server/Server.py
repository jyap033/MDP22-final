import socket 
import threading
import time
from AlgorithmManager import AlgorithmManager
import ImageManager
HEADER = 4096
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SEPARATOR = "<SEPARATOR>"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server)
print(ADDR)

server.bind(ADDR)


#def image_receive(conn, addr):

def rpi_handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
       # msg_length = conn.recv(HEADER).decode(FORMAT)
       # if msg_length:
           
            #msg_length = int(msg_length)
            #msg = conn.recv(msg_length).decode(FORMAT)
            msg = conn.recv(HEADER).decode(FORMAT)
            if ".jpg" in msg:
                ImageManager.saveimage(msg,conn) 
                connected = False
            if msg == DISCONNECT_MESSAGE:
                connected = False

            if msg == "start":
                print("calibrating")
                a=AlgorithmManager()
                waypoint=[4,7]
                hex="0700000000000001C00002000400080010202040408001000200040000380000000020004200"

                movs=a.compute(hex,waypoint)   
                print(movs)
                for row in movs:
                    conn.send(row.encode(FORMAT))
                    print(row)
                    time.sleep(0.001)

                print("done")
            #conn.send("Msg received".encode(FORMAT))
           
            conn.send("done".encode(FORMAT))

   
    conn.close()
    #sys.exit()
def saveimage(client_socket):
    received = client_socket.recv(HEADER).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(HEADER)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))   

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        rpi_thread = threading.Thread(target=rpi_handle_client, args=(conn, addr))
        rpi_thread.start()


        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    

print("[STARTING] server is starting...")
start()
