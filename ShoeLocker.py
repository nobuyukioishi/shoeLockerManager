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

    def __init__(self, row, col, 
                    def_value=(
                        {'recordedTime': "0000-00-00 00:00:00",
                         'boxNo': 0,
                         'status': 0,
                         'lastIn': "0000-00-00 00:00:00",
                         'lastOut': "0000-00-00 00:00:00"
                        }),
                    row_height=28, col_width=56, kernel_size=(56, 56)
                ):

        """
        :param row: shoe locker's row
        :param col: shoe locker's column
        """
        self.locker = [[def_value for i in range(col)] for j in range(row)]
        self.row = row
        self.col = col

        self.row_height = row_height
        self.col_width = col_width
        self.kernel_size = (56, 56)
        self.table_name = 'info'

    def set_database_info(self, host, user, password, db, charset="utf8", cursorclass=pymysql.cursors.DictCursor):
        self.db_info = dict(host=host, user=user, password=password, db=db, charset=charset, cursorclass=cursorclass)

    def change_status_to(self, kwargs):
        """
        :param x: row
        :param y: col
        :param status: {'recordedTime': ,
                        'boxNo': ,
                        'status':,
                        'lastIn':,
                        'lastOut': }
        :return: None
        """
        x = int(kwargs['boxNo'] / self.col)
        y = kwargs['boxNo'] % self.row

        # check if lastIn is setted
        if kwargs['lastIn'] == -1:
            # lastIn == 0
            if self.locker[x][y]==1 and kwargs['status']==0:
                # shoe has moved out, renew LastOut
                self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                     'boxNo': kwargs['boxNo'],
                                     'status': kwargs['status'],
                                     'lastIn': self.locker[x][y]['lastIn'],
                                     'lastOut': kwargs['recordedTime']
                                    }
            elif self.locker[x][y]==0 and kwargs['status']==1:
                # shoe has moved in, renew LastIn
                self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                     'boxNo': kwargs['boxNo'],
                                     'status': kwargs['status'],
                                     'lastIn': kwargs['recordedTime'],
                                     'lastOut': self.locker[x][y]['lastOut']
                                    }
            else:
                self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                     'boxNo': kwargs['boxNo'],
                                     'status': kwargs['status'],
                                     'lastIn': kwargs['recordedTime'],
                                     'lastOut': self.locker[x][y]['lastOut']
                                    }  
        else:
            self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                 'boxNo': kwargs['boxNo'],
                                 'status': kwargs['status'],
                                 'lastIn': kwargs['lastIn'],
                                 'lastOut': kwargs['lastOut']
                                }
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
        pts2 = np.float32([[0, 0], [self.col * self.col_width, 0], [0, self.row * self.row_height],
                           [self.col * self.col_width, self.row * self.row_height]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        warpedImg = cv2.warpPerspective(img, M, (self.col * self.col_width, self.row * self.col_width))

        # save image for shoeBox
        for i in range(0, self.row):
            for j in range(0, self.col):
                shoeBox = warpedImg[i * self.row_height: (i + 1) * self.row_height,
                          j * self.col_width: (j + 1) * self.col_width]
                # because current picture size is 28*56, to feed 56*56 kernel, we will resize it
                CubicImg = cv2.resize(shoeBox, self.kernel_size)
                cv2.imwrite('temp/box%s.png' % (i * self.col + j), CubicImg)

        return self.row * self.col

    def get_state(self, count=int):
        """
        :param count: number of a shoe locker's images
        :return: list of tuple (predict, time) for each shoe locker's state
        """

        if count != self.row * self.col:
            print("count != row * col")

        # get shoe np array
        shoesArray = pic_to_np_array(count)
        # predict arrays
        predict_list = predictShoe(shoesArray)
        # for debug
        # return predict_list

        time_stamped_predict_list = []
        time = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        for index, predict in enumerate(predict_list):

            if predict > 0.8:
                d = {'recordedTime': time,
                 'boxNo': index,
                 'status': True, 
                 'lastIn': -1,
                 'lastOut': -1   
                 }
                self.change_status_to(d)
                time_stamped_predict_list.append(d)

            else:
                d = {'recordedTime': time,
                 'boxNo': index,
                 'status': False, 
                 'lastIn': -1,
                 'lastOut': -1  
                 }
                self.change_status_to(d)
                time_stamped_predict_list.append(d)
        return time_stamped_predict_list


    def push_status(self, box_no, status, last_in, last_out):
        """

        :param recordedTime:
        :param boxNo: index of shoe box
        :param lastIn:
        :param lastOut:
        :return:
        """


        if self.db_info is None:
            print("ERROR! You should execute set_database_info() before use this method!")
            exit()

        connection = pymysql.connect(host=self.db_info['host'],
                                     user=self.db_info['user'],
                                     password=self.db_info['password'],
                                     db=self.db_info['db'],
                                     charset=self.db_info['charset'],
                                     cursorclass=self.db_info['cursorclass'])

        with connection.cursor() as cursor:
            command = "insert into "+self.table_name+" (recordedTime,boxNo,status,lastIn,lastOut) values(now()," \
                      + str(box_no)+","+status+",'"+str(last_in)+"','"+str(last_out)+"')"

            cursor.execute(command)
            connection.commit()
        connection.close()

        return


    def get_recent_data(self):
        connection = pymysql.connect(host=self.db_info['host'],
                                     user=self.db_info['user'],
                                     password=self.db_info['password'],
                                     db=self.db_info['db'],
                                     charset=self.db_info['charset'],
                                     cursorclass=self.db_info['cursorclass'])
        with connection.cursor() as cursor:
            sql = """select X.recordedTime, X.boxNo, X.status, X.lastIn, X.lastOut
                     from info as X, (select max(recordedTime) as max, boxNo from info group by boxNo) as Y
                     where X.recordedTime = Y.max AND X.boxNo = Y.boxNo;"""
            cursor.execute(sql)
            data = cursor.fetchall()
        connection.close()
        return data

