import socket               # Import socket module

shoeLocker = ShoeLocker(3, 3)
shoeLocker.set_database_info(host='192.168.88.14',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
x = ([124, 96], [415, 91], [115, 356], [409, 366])
shoeLocker.change_locker_edge_points_to(shoeBoxEdgePoints=x)

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
    shoeLocker.divide_big_shoe_box(latest_pic="latest_pic.jpg")
	shoeLocker.get_state()
	shoeLocker.push_many_status()
s.close()



