import bluetooth as bt
from config import UUID

class Android:
    def __init__(self):
        self.server_sock = None
        self.client_sock = None
        
        self.server_sock = bt.BluetoothSocket(bt.RFCOMM)
        currentPort = bt.PORT_ANY
        self.server_sock.bind(("", currentPort)) #port 1        
        self.server_sock.listen(currentPort)
        print(currentPort)
        
        bt.advertise_service(
            self.server_sock,
            'MDPGrp22',
            service_id=UUID,
            service_classes=[UUID, bt.SERIAL_PORT_CLASS],
            profiles=[bt.SERIAL_PORT_PROFILE]
        )
        print('server socket:', str(self.server_sock))
        print('client socket:', str(self.client_sock))
        
    def connect(self):
        while True:
            retry = False;
            
            try:
                print('Establishing connection with Android Galaxy Tablet...')
                
                if self.client_sock is None:
                    self.client_sock, address = self.server_sock.accept()
                    print('Accepted connection from Android at: ' + str(address))
                    retry = False
                
#                 elif self.client_sock is not None:
#                     self.client_sock, address = self.server_sock.accept()
#                     print('Accepted connection from Android at: ' + str(address))
#                     retry = False
        
                    
            except Exception as e:
                print("Connection with Android failed: " + str(e))
                
                if self.client_sock is not None:
                    self.client_sock.close()
                    self.client_sock = None
                
                retry = True
                
            if not retry:
                break
            
            print("Attempting Reconnection with Android...")
                
    def disconnect(self):
        try:
            if self.client_sock is not None:
               self.client_sock.close()
               self.client_sock = None
            print("Android disconnected")
            
        except Exception as e:
            print("Android disconnect failed: " + str(e))
            
    def recv(self):
        try:
            msg = self.client_sock.recv(1024)
            print ("received: [%s]" %(msg))
            
            if msg is None:
                return None
            
            if len(msg) > 0:
                return msg
            
            return None
        
        except Exception as e:
            print("Failed to receive from Android: " + str(e))
            raise e
        
    def send(self, msg):
        try:
            self.client_sock.send(msg)
            print ("send: [%s]" %(msg)) 
            
        except Exception as e:
            print("Failed to send to Android: " + str(e))
            raise e
            
# an = Android()
# an.connect()