import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '' # Get local machine name
port = 55000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    f = open('latest_pic.jpg','wb')
    print('Got connection from', addr)
    l = c.recv(1024)
    while (l):
        f.write(l)
        l = c.recv(1024)
    f.close()
    c.close()                # Close the connection
s.close()
