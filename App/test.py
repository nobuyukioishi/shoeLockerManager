from flask import Flask, render_template
from datetime import datetime
import pymysql.cursors
import sys, os
sys.path.append(os.pardir)
from ShoeLocker import ShoeLocker

shoeLocker = ShoeLocker(3, 3)

connection = pymysql.connect(host='192.168.11.140',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

# get recent data
with connection.cursor() as cursor:
    sql = """select X.recordedTime, X.boxNo, X.status, X.lastIn, X.lastOut
             from info as X, (select max(recordedTime) as max, boxNo from info group by boxNo) as Y
             where X.recordedTime = Y.max AND X.boxNo = Y.boxNo;"""
    cursor.execute(sql)
    recentData = cursor.fetchall()
connection.close()

for data in recentData:
    shoeLocker.change_status_to(data)

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    shoeLockerInfo = '<div></div>'
    return render_template('index.html', data=recentData)


app.run(port=9999, debug=True)
