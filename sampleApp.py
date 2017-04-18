from flask import Flask, render_template
import datetime
import pymysql.cursors
import sys, os
sys.path.append(os.pardir)
from ShoeLocker import ShoeLocker

shoeLocker = ShoeLocker(3, 3)

shoeLocker.set_database_info(host='192.168.11.184',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def home():
    # we are getting picture by socket automatically
    # shoeLocker.save_raspi_pic()

    x = ([99, 30], [425, 39], [108, 349], [406, 350])
    shoeLocker.change_locker_edge_points_to(shoeBoxEdgePoints=x)
    shoeLocker.divide_big_shoe_box(latest_pic="latest_pic.jpg")
    shoeLocker.get_state()
    shoeLocker.push_many_status()

    data = shoeLocker.get_recent_data()
    for tmp in data:
        shoeLocker.change_status_to(tmp)

    return render_template('index.html',
                           now='{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()),
                           data=sorted(data, key = lambda x:x['boxNo']),
                           col=shoeLocker.col,
                           row=shoeLocker.row)

app.run(port=9999, debug=True)
