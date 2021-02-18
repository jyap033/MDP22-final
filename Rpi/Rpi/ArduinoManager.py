import serial
ser =  serial.Serial('/dev/ttyACM0',9600)

class Arduino:

    #read from Arduino
    #input= ser.read()
    #print ("Read input" + input.decode("utf-8") + " from Aduino")

    #write to Arduino
    def send(self,movement):
        
        ser.write(movement.encode())
   
