from SocketClient import Socket
from AndroidManager import Android
from ArduinoManager import Arduino
import ArduinoManager
import time


#Connect to Arduino
ar = Arduino()

#'Connect to Server
s = Socket()

#Connect to Android
an = Android()
an.connect()


while True:
    an.send("Ard|And|fwd|")
    r = an.recv()
    tempMsg = str(r).split("'")[1].strip()
    
    #Left Turn
    if(tempMsg == "And|Ard|a|"):
        ar.send("L1")
    #Right Turn
    if(tempMsg == "And|Ard|d|"):
        ar.send("R1")
    #Go Straight
    if(tempMsg == "And|Ard|w|"):
        ar.send("F1")
    #Go Backwards
    if(tempMsg == "And|Ard|b|"):
        ar.send("B1")
    #Calibrate
    if(tempMsg == "And|Alg|C|"):
        s.start()
        s.send("start")
        ar.send("C")
    #Start
    if(tempMsg == "And|Alg|FP_START|"):
        for movement in s.getmovements():
            ar.send(movement)
            ar.read()
    
    #Read from Arduino
    while True:
        ar.read()     
        
    if(tempMsg == ''):
        # send message
        sendMsg = input("Type here : ")
        
        
        
        



    