import socket               # Import socket module
import pymysql.cursors
import sys, os
sys.path.append(os.pardir)
from ShoeLocker import ShoeLocker

shoeLocker = ShoeLocker(3, 3)
shoeLocker.set_database_info(host='192.168.88.14',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
x = ([124, 96], [415, 91], [115, 356], [409, 366])
shoeLocker.change_locker_edge_points_to(shoe_box_edge_points=x)
shoeLocker.set_status_from_database()

s = socket.socket()         # Create a socket object
host = ''                   # Get local machine name
port = 55000                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    # get latest_pic.jpg using socket connection
    c, address = s.accept()     # Establish connection with client.
    f = open('latest_pic.jpg', 'wb')
    print('Got connection from', address)
    l = c.recv(1024)
    while l:
        f.write(l)
        l = c.recv(1024)
    f.close()
    c.close()                # Close the connection

    # check if latest_pic is OK
    if shoeLocker.is_image_good(image="latest_pic.jpg"):
        # push status to shoe locker
        shoeLocker.divide_big_shoe_box(latest_pic="latest_pic.jpg")
        shoeLocker.get_state()
        try:
            shoeLocker.push_many_status()
        except:
            print("failed push_many_status")
        try: 
            shoeLocker.save_to_folder(image="latest_pic.jpg")
        except:
            print("failed on save to folder")
    else:
        print("Returned false from is_pic_good, ignoring this loop . . .")
