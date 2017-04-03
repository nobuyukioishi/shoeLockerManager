from ShoeLocker import ShoeLocker
import datetime

shoeLocker = ShoeLocker(5, 5, (True, '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())))
shoeLocker.change_status_to(2, 3, (True, "2015-11-11 11:11:11"))
shoeLocker.print_status()