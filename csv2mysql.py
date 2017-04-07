import csv
import pymysql.cursors

with open('testCSVFile/sampleData.csv') as csv_file:
    reader = csv.reader(csv_file)

    connection = pymysql.connect(host='192.168.11.140',
                                 user='hoge',
                                 password='PassWord123@',
                                 db='shoeLockerManager',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    for row in reader:
        # print(row)

        with connection.cursor() as cursor:
            command = "insert into status (recordedTime,boxNo,status, lastIn,lastOut) values('"+row[0]+"'," \
                      + row[1] + "," + row[2] + ",'" + row[3] + "','" + row[4] + "')"
            print(command)
            cursor.execute(command)
            connection.commit()

connection.close()