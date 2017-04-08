from ShoeLocker import ShoeLocker
import datetime

# stick this datetime format '{0:%Y-%m-%d %H:%M:%S}'

shoeLocker = ShoeLocker(8, 3, (True, '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())))
shoeLocker.change_status_to(2, 3, (False, "2015-11-11 11:11:11"))
# shoeLocker.print_status()

"""
x = ([804, 164], [1328, 165], [807, 815], [1293, 816])
shoeLocker.change_locker_edge_points_to(shoeBoxEdgePoints=x)
count = shoeLocker.dissemble_bigShoeBox(raspi_im="temp/raspi_pic.jpg")
print(count)
out = shoeLocker.get_state(count)
print(out)
"""

# ShoeLocker.push_status(10, 1,"2017-11-11 11:11:11", "2017-11-11 11:11:11")
shoeLocker.push_status(0, 0,"2017-11-11 11:00:11", "2017-11-11 11:00:11")
shoeLocker.push_status(1, 1,"2017-11-11 11:11:00", "2017-11-11 11:11:00")
shoeLocker.push_status(2, 0,"2016-11-11 00:11:11", "2017-11-11 00:11:11")
shoeLocker.push_status(3, 0,"2017-11-11 11:00:11", "2017-11-11 11:00:11")
shoeLocker.push_status(4, 1,"2017-11-11 11:11:00", "2017-11-11 11:11:00")
shoeLocker.push_status(5, 0,"2016-11-11 00:11:11", "2017-11-11 00:11:11")
shoeLocker.push_status(6, 0,"2017-11-11 11:00:11", "2017-11-11 11:00:11")
shoeLocker.push_status(7, 1,"2017-11-11 11:11:00", "2017-11-11 11:11:00")
shoeLocker.push_status(8, 0,"2016-11-11 00:11:11", "2017-11-11 00:11:11")

# command = "insert into status (recordedTime,boxNo,status,lastIn,lastOut) values(now(),"
# +str(box_no)+","+str(status)+",'"+str(last_in)+"','"+str(last_out)+"')"


# ShoeLocker.get_all_status()
