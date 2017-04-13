import socket               # Import socket module
# same as raspi file
# raspi folder direction : ~/Desktop/socketServer.py
s = socket.socket()         # Create a socket object
HOST = ''       # set ip address visible to network

# host =  # Get local machine name
port = 3336                 # Reserve a port for your service.
s.bind((HOST, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print( 'Got connection from', addr)
    f = open('image01.jpg','rb')
    print('Sending...')
    l = f.read(1024)
    while (l):
    #    print('Sending...')
        c.send(l)
        l = f.read(1024)
    f.close()
    print("Done Sending")

    # c.send('Thank you for connecting')




