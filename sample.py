from ShoeLocker import ShoeLocker
import datetime
import pymysql.cursors


# stick this datetime format '{0:%Y-%m-%d %H:%M:%S}'

# shoeLocker = ShoeLocker(row=3, col=3, (True, '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())))
shoeLocker = ShoeLocker(row=3, col=3)
# shoeLocker.change_status_to(2, 3, (False, "2015-11-11 11:11:11"))
shoeLocker.print_status()

# x = ([804, 164], [1328, 165], [807, 815], [1293, 816])
# shoeLocker.change_locker_edge_points_to(shoeBoxEdgePoints=x)

# count = shoeLocker.dissemble_bigShoeBox(raspi_im="temp/raspi_pic.jpg")

# out = shoeLocker.get_state(count)

kwargs ={'recordedTime': datetime.datetime.now(),
                                 'boxNo': 1,
                                 'status': 0,
                                 'lastIn': datetime.datetime.now(),
                                 'lastOut': datetime.datetime.now()
                                }
shoeLocker.change_status_to(kwargs)
shoeLocker.print_status()

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

