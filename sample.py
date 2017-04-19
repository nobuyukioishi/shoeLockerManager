from ShoeLocker import ShoeLocker
import datetime
import pymysql.cursors
import time


# stick this datetime format '{0:%Y-%m-%d %H:%M:%S}'

shoeLocker = ShoeLocker(row=3, col=3)
shoeLocker.set_database_info(host='192.168.11.184',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

# shoeLocker.print_status()
# kwargs ={'recordedTime': datetime.datetime.now(),
#                                  'boxNo': 1,
#                                  'status': 0,
#                                  'lastIn': datetime.datetime.now(),
#                                  'lastOut': datetime.datetime.now()
#                                 }

shoeLocker.save_raspi_pic()
# shoebox edge points
# x = ([99, 30], [425, 39], [108, 349], [406, 350]) 
# shoe centered points
x = ([124, 96], [415, 91], [115, 356], [409, 366]) 
shoeLocker.change_locker_edge_points_to(shoe_box_edge_points=x)
count = shoeLocker.divide_big_shoe_box(latest_pic="recent.jpg")
shoeLocker.get_state(count)
#shoeLocker.push_many_status()

# shoeLocker.change_status_to(kwargs)
# shoeLocker.print_status()


# ShoeLocker.push_status(10, 1,"2017-11-11 11:11:11", "2017-11-11 11:11:11")
# shoeLocker.push_status(0, 0,"2017-11-11 11:00:11", "2017-11-11 11:00:11")
# shoeLocker.push_status(1, 1,"2017-11-11 11:11:00", "2017-11-11 11:11:00")
# shoeLocker.push_status(2, 0,"2016-11-11 00:11:11", "2017-11-11 00:11:11")
# shoeLocker.push_status(3, 0,"2017-11-11 11:00:11", "2017-11-11 11:00:11")
# shoeLocker.push_status(4, 1,"2017-11-11 11:11:00", "2017-11-11 11:11:00")
# shoeLocker.push_status(5, 0,"2016-11-11 00:11:11", "2017-11-11 00:11:11")
# shoeLocker.push_status(6, 0,"2017-11-11 11:00:11", "2017-11-11 11:00:11")
# shoeLocker.push_status(7, 1,"2017-11-11 11:11:00", "2017-11-11 11:11:00")
# shoeLocker.push_status(8, 0,"2016-11-11 00:11:11", "2017-11-11 00:11:11")

"""

shoeLocker.set_database_info(host='192.168.11.140',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


shoeLocker.push_status(11, "2017-11-11 11:11:11", "2017-11-11 11:11:11")

"""

