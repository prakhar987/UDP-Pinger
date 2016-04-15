import time
from socket import * 
from datetime import datetime

for i in range(1,11):  

    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server

    addr = ("127.0.0.1", 12000)

    #Send ping
    start = time.time()
    message = 'Ping '+str(i)+' '+str(datetime.now())
    clientSocket.sendto(message, addr)
 
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print data , "Packet Num:" , i , "Time Elapsed", elapsed        
 
    except timeout:
        print 'REQUEST TIMED OUT for packet :',i
