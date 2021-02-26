import socket 
import threading
import time
from AlgorithmManager import AlgorithmManager
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server)
print(ADDR)
server.bind(ADDR)




def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            print ("#"+msg_length)
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            if msg == "start":
                print("calibrating")
                a=AlgorithmManager()
                waypoint=[2,3]
                hex="0700000000000001C00002000400080010202040408001000200040000380000000020004200"

                movs=a.compute(hex,waypoint)   
                for row in movs:
                    conn.send(row.encode(FORMAT))
                    print(row)
                    time.sleep(0.001)

                print("done")
            #conn.send("Msg received".encode(FORMAT))
           
            conn.send("done".encode(FORMAT))

   
    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()