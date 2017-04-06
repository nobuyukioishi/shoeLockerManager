import cv2
from functions import *
import datetime
import pymysql.cursors
from datetime import datetime

"""
verbs: 
big shoebox: bigShoeBox
small or one shoebox: smallShoeBox
"""


class ShoeLocker:
    def __init__(self, row, col, def_value=(False, "0000-00-00 00:00:00"), rowHeight=28, colWidth=56,
                 kernelSize=(56, 56)):
        """
        :param row: shoe locker's row
        :param col: shoe locker's column
        """
        self.locker = [[def_value for i in range(col)] for j in range(row)]
        self.row = row
        self.col = col
        self.rowHeight = rowHeight
        self.colWidth = colWidth
        self.kernelSize = (56, 56)

    def change_status_to(self, x, y, status):
        """
        :param x: row
        :param y: col
        :param status: (True/False, time)
        :return: None
        """
        if type(status) != tuple:
            print("status should be tuple object")
            return

        self.locker[x - 1][y - 1] = status
        return

    def print_status(self):
        for i in range(len(self.locker[0])):
            print("  |\t\t\t\t", i, "\t\t\t\t  ", end="")  # \t equals to 4 half-spaces.
        print()
        for i in range(len(self.locker)):
            print(i, "| ", end="")
            for j in range(len(self.locker[0])):
                print(self.locker[i][j], "\t|\t", end="")
            print()

    def get_big_picture(self):
        """
        :param NONE
        :return True, False
        Save picture of raspi-cam to temp/raspi_pic.jpg
        """

    def change_locker_edge_points_to(self, shoeBoxEdgePoints):
        """
        :param raspi_im: Name of picture to dissemble, this time raspi_im
        :set 4 edge point of 
        """
        self.x1x1, self.x1y2, self.x2y1, self.x2y2 = shoeBoxEdgePoints
        return

    def dissemble_bigShoeBox(self, raspi_im="temp/raspi_pic.jpg"):
        """
        :param raspi_im: Name of picture to dissemble, this time raspi_im
        :return count: number of dissembled picture
        Save dissembled pictures to temp/, names box%s.png %s is integer goes 0 to count-1
        """

        img = cv2.imread(raspi_im)
        if raspi_im is None:
            print("Cannot find image %s", raspi_im)
            return -1
        # affine transformation
        # points of target rectangle
        pts1 = np.float32([self.x1x1, self.x1y2, self.x2y1, self.x2y2])
        pts2 = np.float32([[0, 0], [self.col * self.colWidth, 0], [0, self.row * self.rowHeight],
                           [self.col * self.colWidth, self.row * self.rowHeight]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        warpedImg = cv2.warpPerspective(img, M, (self.col * self.colWidth, self.row * self.colWidth))

        # save image for shoeBox
        for i in range(0, self.row):
            for j in range(0, self.col):
                shoeBox = warpedImg[i * self.rowHeight: (i + 1) * self.rowHeight,
                          j * self.colWidth: (j + 1) * self.colWidth]
                # because current picture size is 28*56, to feed 56*56 kernel, we will resize it
                CubicImg = cv2.resize(shoeBox, self.kernelSize)
                cv2.imwrite('temp/box%s.png' % (i * self.col + j), CubicImg)

        return self.row * self.col

    def get_state(self, count=int):
        """
        :param count: number of a shoe locker's images
        :return: list of tuple (predict, time) for each shoe locker's state
        """

        if count != self.row * self.col:
            print("count!=row*col")

        # get shoe np array
        shoesArray = pic_to_np_array(count)
        # predict arrays
        predict_list = predictShoe(shoesArray)
        # for debug
        # return predict_list

        time_stamped_predict_list = []
        time = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        for index, predict in enumerate(predict_list):
            # index = i * self.col + j
            i = int(index / self.col)
            j = int(index - i * self.col)
            if predict > 0.8:
                time_stamped_predict_list.append((i, j, (True, time)))
            else:
                time_stamped_predict_list.append((i, j, (False, time)))
        return time_stamped_predict_list

    @staticmethod
    def push_status(box_no, last_in, last_out):
        """

        :param recordedTime:
        :param boxNo: index of shoe box
        :param lastIn:
        :param lastOut:
        :return:
        """

        connection = pymysql.connect(host='192.168.11.140',
                                     user='piyo',
                                     password='PassWord123@',
                                     db='shoeLockerManager',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            command = "insert into status (recordedTime,boxNo,lastIn,lastOut) values(now(),"+str(box_no)+",'"+str(last_in)+"','"+str(last_out)+"')"
            # print(command)
            cursor.execute(command)
            connection.commit()
        connection.close();

        return
