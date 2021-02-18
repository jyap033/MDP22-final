from SocketClient import Socket
from AndroidManager import Android
from ArduinoManager import Arduino
import ArduinoManager
import time

#Connect to Android
an = Android()
an.connect()

#Connect to Arduino
ar = Arduino()

#Connect to Server
s = Socket()



while True:
    an.send("Ard|And|fwd|")
    r = an.recv()
    tempMsg = str(r).split("'")[1].strip()
    #Left Turn
    if(tempMsg == "And|Ard|a|"):
        ar.send("L")
    #Right Turn
    if(tempMsg == "And|Ard|d|"):
        ar.send("R")
    #Go Straight
    if(tempMsg == "And|Ard|w|"):
        ar.send("S")
    #Go Backwards
    if(tempMsg == "And|Ard|b|"):
        ar.send("B")
    #Calibrate
    if(tempMsg == "And|Alg|C|"):
        s.start()
        s.send("start")
        ar.send("C")
    #Start
    if(tempMsg == "And|Alg|FP_START|"):
        for movement in s.getmovements():
            ar.send(movement)
            
        
    if(tempMsg == ''):
        # send message
        sendMsg = input("Type here : ")
        



    