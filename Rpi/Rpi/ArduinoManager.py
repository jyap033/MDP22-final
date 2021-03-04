import threading
import serial

class Arduino:
    def __init__(self):
        self.ser =  serial.Serial('/dev/ttyACM0',115200)
        #self.connected = False
        
    #write to Arduino
    def send(self,movement):
        self.ser.write(movement.encode())
    
    #def handle_data(self,data):
        #print(data)
        
    #read from Arduino
    def read(self):
        #while not connected:
            #connected = True
            
            #while True:
                #print("test")
        msg= self.ser.readline().decode()
        print(msg)
                #handle_data(msg)
        #print ("Read input " + msg.decode("utf-8") + " from Arduino")
    

#thread = threading.Thread(target=read, args=(
# ar=Arduino()
# while True:
#     ar.read()