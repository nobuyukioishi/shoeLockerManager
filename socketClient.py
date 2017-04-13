# CentOS 
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "192.168.11.213" # Raspi ip
port = 3336               # Reserve a port for your service.

s.connect((host, port))
# s.send("Hello server!")

f = open('to_recv.jpg','wb')

print( "Receiving...")
l = s.recv(1024)
count = 0
while (l):
    print( "Receiving...")
    print(count)
    count = count+1
    f.write(l)
    l = s.recv(1024)
    print(count)
print( "Done Receiving")

# s.send("Hello server!")

f.close()
s.close()

