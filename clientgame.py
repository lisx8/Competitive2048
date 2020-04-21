'''from socket import *
import sys
import time

#serverName = "127.0.0.1"
#serverPort = 12000

SERVER_IP = '192.168.2.15'
PORT_NUMBER = 8888

mySocket = socket( AF_INET, SOCK_DGRAM)
mySocket.connect((SERVER_IP,PORT_NUMBER))

while True:
        mySocket.send('cool')
        time.sleep(.5)
from socket import *
import sys

PORT_NUMBER = 8888
SIZE = 102'''


import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', 8888))
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()
    print(message)
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)