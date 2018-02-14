import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

import grovepi
from grovepi import *
import socket 

# use TCP
def Main():
	# Change the host and port as needed. For ports, use a number in the 9000 
	# range. 
	host = '192.168.1.249'
	port = 8000

	s = socket.socket()
	s.bind((host,port))

	s.listen(1)
	c, addr = s.accept()

	print("Connected to: " + str(addr))

	LED = 3

	pinMode(LED,"OUTPUT")

	message = "LED waiting for command..."
	while True:
		data = c.recv(1024).decode('utf-8')
		if not data:
			break
		data = str(data)
		print(data + data)
		if data == "LED_ON":
			digitalWrite(LED,1)
			message = "LED ON"
		if data == "LED_OFF":
			digitalWrite(LED,0)
			message = "LED OFF"
		else:
			message = "command not recognized"
		c.send(message.encode('utf-8'))
	c.close()

if __name__ == '__main__':
	Main()