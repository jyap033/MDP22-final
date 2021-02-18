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

ar.send("L")
while True:
    r = an.recv()
    tempMsg = str(r).split("'")
    if(tempMsg[1].strip() == ''):
        # send message
        sendMsg = input("Type here : ")
        an.send(sendMsg)

#Connect to Server
#s = Socket()
#s.start()
#s.send("start")

#Read from Server
#ard = ArduinoManager
#for movement in s.getmovements():
#    ard.send(movement)
#    print(movement)
#    time.sleep(300)
    