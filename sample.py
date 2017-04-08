from ShoeLocker import ShoeLocker
import datetime

# stick this datetime format '{0:%Y-%m-%d %H:%M:%S}'

shoeLocker = ShoeLocker(8, 3, (True, '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())))
shoeLocker.change_status_to(2, 3, (False, "2015-11-11 11:11:11"))
# shoeLocker.print_status()

# x = ([804, 164], [1328, 165], [807, 815], [1293, 816])
# shoeLocker.change_locker_edge_points_to(shoeBoxEdgePoints=x)

# count = shoeLocker.dissemble_bigShoeBox(raspi_im="temp/raspi_pic.jpg")

# out = shoeLocker.get_state(count)

out = [(0, (True, '2017-04-08 17:34:14')), (1, (True, '2017-04-08 17:34:14')), (2, (True, '2017-04-08 17:34:14')), (3, (True, '2017-04-08 17:34:14')), (4, (True, '2017-04-08 17:34:14')), (5, (True, '2017-04-08 17:34:14')), (6, (True, '2017-04-08 17:34:14')), (7, (True, '2017-04-08 17:34:14')), (8, (True, '2017-04-08 17:34:14')), (9, (False, '2017-04-08 17:34:14')), (10, (True, '2017-04-08 17:34:14')), (11, (True, '2017-04-08 17:34:14')), (12, (True, '2017-04-08 17:34:14')), (13, (True, '2017-04-08 17:34:14')), (14, (True, '2017-04-08 17:34:14')), (15, (True, '2017-04-08 17:34:14')), (16, (True, '2017-04-08 17:34:14')), (17, (True, '2017-04-08 17:34:14')), (18, (True, '2017-04-08 17:34:14')), (19, (True, '2017-04-08 17:34:14')), (20, (True, '2017-04-08 17:34:14')), (21, (True, '2017-04-08 17:34:14')), (22, (True, '2017-04-08 17:34:14')), (23, (True, '2017-04-08 17:34:14'))]

push_many_status(time_stamped_predict_list=out)


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

# command = "insert into status (recordedTime,boxNo,status,lastIn,lastOut) values(now(),"
# +str(box_no)+","+str(status)+",'"+str(last_in)+"','"+str(last_out)+"')"


# ShoeLocker.get_all_status()
