import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

import grovepi
from grovepi import *
import socket

#use tcp
def Main():
	host = '192.168.1.249'
	port = 8000

	s = socket.socket()
	print("socket created")

	s.connect((host,port))
	print("socket connected")

	command = input("command->")
    while True:
        c.send(command.encode('utf-8'))
        data = c.recv(1024).decode('utf-8')
        print("LED status: " + data)
        command = input("command->")
	s.close()

if __name__ == '__main__':
	Main()
