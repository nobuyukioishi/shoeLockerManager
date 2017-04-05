from ShoeLocker import ShoeLocker
import datetime

# stick this datetime format '{0:%Y-%m-%d %H:%M:%S}'
shoeLocker = ShoeLocker(8, 3, (True, '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())))
shoeLocker.change_status_to(2, 3, (False, "2015-11-11 11:11:11"))
shoeLocker.print_status()

edge_points = (
	[804, 164], [1328, 165], 
	[807, 815], [1293, 816]
	)
shoeLocker.change_locker_edge_points_to(shoe_box_edge_points=edge_points)
count = shoeLocker.dissemble_big_shoe_box(raspi_im="temp/raspi_pic.jpg")
print(count)
out = shoeLocker.get_state(count)
print(out)

