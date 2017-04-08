from ShoeLocker import ShoeLocker
import datetime
import pymysql.cursors


# stick this datetime format '{0:%Y-%m-%d %H:%M:%S}'

shoeLocker = ShoeLocker(3, 3)
shoeLocker.print_status()

"""
x = ([804, 164], [1328, 165], [807, 815], [1293, 816])
shoeLocker.change_locker_edge_points_to(shoeBoxEdgePoints=x)
count = shoeLocker.dissemble_bigShoeBox(raspi_im="temp/raspi_pic.jpg")
print(count)
out = shoeLocker.get_state(count)
print(out)
"""

"""

shoeLocker.set_database_info(host='192.168.11.140',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


shoeLocker.push_status(11, "2017-11-11 11:11:11", "2017-11-11 11:11:11")

"""