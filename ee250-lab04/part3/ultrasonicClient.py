import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

from grovepi import *
import socket

#use UDP
def Main():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '192.168.1.249'
    port = 5000

    server_addr = '192.168.1.189'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host,port))

    # UDP is connectionless, so a client does not formally connect to a server
    dst_port = 8000

    while TRUE:
	    try:
	        # Read distance value from Ultrasonic
	        dist = grovepi.ultrasonicRead(ultrasonic_ranger)

	    except TypeError:
	        data = "TypeError"
	    except IOError:
	        data = "IOError"

        #tuples are immutable so we need to overwrite the last tuple
        server = (server_addr, int(dst_port))

        # for UDP, sendto() and recvfrom() are used instead
        s.sendto(dist.encode('utf-8'), server) 
    s.close()

if __name__ == '__main__':
    Main()