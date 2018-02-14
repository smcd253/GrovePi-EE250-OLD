import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `from grovepi import *`
sys.path.append('../../Software/Python/')

import socket 

# use TCP
def Process1():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '10.0.2.15'
    port = 9000

    s = socket.socket()
    s.bind((host,port))
    
    s.listen(1)
    c, addr = s.accept()

    print("Connected to: " + str(addr))

    command = input("command->")
    while True:
        c.send(command.encode('utf-8'))
        data = c.recv(1024).decode('utf-8')
        print("LED status: " + data)
        command = input("command->")
    c.close()

if __name__ == '__main__':
    Process1()