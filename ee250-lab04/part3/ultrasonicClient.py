import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

import grovepi
from grovepi import *
import socket

#use UDP
def Main():
	print("enter main")

	# Change the host and port as needed. For ports, use a number in the 9000 
	# range. 
	host = '192.168.1.100'
	port = 5000

	server_addr = '192.168.1.189'

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print("socket created")

	s.bind((host,port))
	print("socket bound")

	# UDP is connectionless, so a client does not formally connect to a server
	dst_port = 8000

	ultrasonic_ranger = 4

	while True:

		try:
			# Read distance value from Ultrasonic
			dist = grovepi.ultrasonicRead(ultrasonic_ranger)
			data = int(dist)

		except TypeError:
			data = "TypeError"
		except IOError:
			data = "IOError"

		#tuples are immutable so we need to overwrite the last tuple
		server = (server_addr, int(dst_port))
		print(data)
		# for UDP, sendto() and recvfrom() are used instead
		s.sendto(data.encode('utf-8'), server) 
	
	s.close()

	print("connection closed")

if __name__ == '__main__':
		Main()