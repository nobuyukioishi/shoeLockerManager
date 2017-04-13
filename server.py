# import socket
# from thread import *

# # 1.Gets the local ip/ip over LAN.
# HOST = ''

# print HOST

# # 2.Use port no. above 1800 so it does not interfere with ports already in use.
# PORT =input ("Enter the PORT number (1 - 10,000)") 

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# print "Socket Created"
# s.bind((HOST, PORT))
# print "Socket Bind Complete"
# s.listen(10)
# print "Socket now listening"
# while True:
#     connection, addr = s.accept()
#     print "Connection Established!"
#     connection.send("Welcome to the server. Type something and hit enter\n")
#     while True:
#         data = connection.recv(1024)
#         if not data:
#             break
#         connection.sendall(data)
#         print data
#         connection.close()
# s.close()

import socket               # Import socket module

s = socket.socket()         # Create a socket object
HOST = ''

# host =  # Get local machine name
port = 3334                 # Reserve a port for your service.
s.bind((HOST, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    f = open('torecv.png','wb')
    c, addr = s.accept()     # Establish connection with client.
    print( 'Got connection from', addr)
    print( "Receiving...")
    l = c.recv(1024)
    while (l):
        print( "Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print( "Done Receiving")
    # c.send('Thank you for connecting')
    c.close()                # Close the connection

# import socket
# import cv2
# import numpy

# def recvall(sock, count):
#     buf = b''
#     while count:
#         newbuf = sock.recv(count)
#         if not newbuf: return None
#         buf += newbuf
#         count -= len(newbuf)
#     return buf

# TCP_IP = 'localhost'
# TCP_PORT = 5001

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(True)
# conn, addr = s.accept()

# length = recvall(conn,16)
# stringData = recvall(conn, int(length))
# data = numpy.fromstring(stringData, dtype='uint8')
# s.close()

# decimg=cv2.imdecode(data,1)
# cv2.imshow('SERVER',decimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 
