# import numpy as np
# import cv2
# def get_bigShoeBox_array(x, y, height, width, raspi_im="temp/raspi_pic.jpg"):
#     """
#     :param raspi_im
#     :return : big shoe box position
#     """

#     image = cv2.imread(raspi_im)
#     if image is None:
#         print("Cannot find image %s", raspi_im)
#         return
#     cv2.imshow("cropped", image)
#     cv2.waitKey(0)
#     #turn crop image to np array
#     npImage = np.asarray(crop_img)

#     return npImage

# if __name__ == '__main__':
#     get_bigShoeBox_array(x=10, y=10, height=800, width=800)

from datetime import datetime
import pymysql.cursors


connection = pymysql.connect(host='192.168.11.140',
                             user='piyo',
                             password='PassWord123@',
                             db='shoeLockerManager',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "SELECT max(recordedTime), boxNo from info group by boxNo"
    cursor.execute(sql)
    results = cursor.fetchall()
    for r in results:
        #dictionary of r
        print(r)
        print(r['boxNo'])
        print(r['max(recordedTime)'])
        # print("b=%s" % b)
        # print("a=%s" % a)

