import serial


class Arduino:

    #read from Arduino
    #input= ser.read()
    #print ("Read input" + input.decode("utf-8") + " from Aduino")
    def __init__(self):
        self.ser =  serial.Serial('/dev/ttyACM0',115200)
    #write to Arduino
    def send(self,movement):
        
        self.ser.write(movement.encode())
   
