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
    def __init__(self, row, col, def_value=(
                    {'recordedTime': "2017-04-08 20:56:30",
                     'boxNo': 0,
                     'status': True,
                     'lastIn': "2017-04-08 20:56:30",
                     'lastOut': "2017-04-08 20:56:30"}),
                 row_height=28, col_width=56, kernel_size=(56, 56)
                 ):

        """
        :param row: shoe locker's row
        :param col: shoe locker's column
        """
        # TODO: i, j not used?
        self.locker = [[def_value for i in range(col)] for j in range(row)]
        self.row = row
        self.col = col

        self.row_height = row_height
        self.col_width = col_width
        self.kernel_size = kernel_size
        self.table_name = 'info'
        self.db_info = None

        self.x1x1 = None
        self.x1y2 = None
        self.x2y1 = None
        self.x2y2 = None

    def set_database_info(self, host, user, password, db, charset="utf8", cursorclass=pymysql.cursors.DictCursor):
        self.db_info = dict(host=host, user=user, password=password, db=db, charset=charset, cursorclass=cursorclass)

    def set_status_from_database(self):
        """
        set shoe locker initialization from MySQL database's most latest record
        """

        data = self.get_recent_data()
        for tmp in data:
            self.change_status_to(tmp)

    def change_status_to(self, kwargs):
        """
        Substitute local locker variable to kwargs.
        :param kwargs: {'recordedTime': ,
                        'boxNo': ,
                        'status':,
                        'lastIn':,
                        'lastOut': }
        :return: None
        """
        x = int(kwargs['boxNo'] / self.col)
        y = kwargs['boxNo'] % self.row
        print("kwargs['status']")
        print(kwargs['status'])
        print("self.lockeri[{0}][{1}]".format(x,y))
        print(self.locker[x][y]['status'])
        # check if lastIn has set
        if kwargs['lastIn'] == -1:
            # lastIn, lastOut is not initialized yet
            if self.locker[x][y]['status'] is True and kwargs['status'] is False:
                # shoe has moved out, renew LastOut
                self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                               'boxNo': kwargs['boxNo'],
                                               'status': kwargs['status'],
                                               'lastIn': self.locker[x][y]['lastIn'],
                                               'lastOut': kwargs['recordedTime']
                                               }
                print("shoes have been moved out")
                print(kwargs['boxNo'])
                print(kwargs)
            elif self.locker[x][y]['status'] is False and kwargs['status'] is True:
                # shoe has moved in, renew LastIn
                self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                     'boxNo': kwargs['boxNo'],
                                     'status': kwargs['status'],
                                     'lastIn': kwargs['recordedTime'],
                                     'lastOut': self.locker[x][y]['lastOut']
                                     }
                print("shoes have moved in")
                print(kwargs['boxNo'])
                print(kwargs)
            else:
                # status hasn't changed, no change on last in, last out value
                self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                     'boxNo': kwargs['boxNo'],
                                     'status': kwargs['status'],
                                     'lastIn': self.locker[x][y]['lastIn'],
                                     'lastOut': self.locker[x][y]['lastOut']
                                     }
                print("status have not changed")
                print(kwargs['boxNo'])
                print(kwargs)
        else:
            # lastIn, lastOut is already initialized. Substitute directly from data.
            self.locker[x][y] = {'recordedTime': kwargs['recordedTime'],
                                 'boxNo': kwargs['boxNo'],
                                 'status': kwargs['status'],
                                 'lastIn': kwargs['lastIn'],
                                 'lastOut': kwargs['lastOut']
                                 }
            print("else was called")
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

    def change_locker_edge_points_to(self, shoe_box_edge_points):
        """
        set 4 edge point of shoe locker
        :param : Edge points of shoe locker
        """
        self.x1x1, self.x1y2, self.x2y1, self.x2y2 = shoe_box_edge_points
        return

    def divide_big_shoe_box(self, latest_pic):
        """
        :param latest_pic: Name of picture to dissemble, this time latest_pic
        Save dissembled pictures to temp/, names box%s.png %s is integer goes 0 to row * col
        """
        img = cv2.imread(latest_pic)
        if latest_pic is None:
            print("Cannot find image %s", latest_pic)
            return -1
        # affine transformation
        # points of target rectangle
        pts1 = np.float32([self.x1x1, self.x1y2, self.x2y1, self.x2y2])
        pts2 = np.float32([[0, 0], [self.col * self.col_width, 0], [0, self.row * self.row_height],
                           [self.col * self.col_width, self.row * self.row_height]])
        m = cv2.getPerspectiveTransform(pts1, pts2)
        warped_img = cv2.warpPerspective(img, m, (self.col * self.col_width, self.row * self.col_width))

        # save image for shoeBox
        for i in range(0, self.row):
            for j in range(0, self.col):
                shoe_box = warped_img[i * self.row_height: (i + 1) * self.row_height,
                                      j * self.col_width: (j + 1) * self.col_width
                                      ]
                # because current picture size is 28*56, to feed 56*56 kernel, we will resize it
                cubic_img = cv2.resize(shoe_box, self.kernel_size)
                cv2.imwrite('temp/box%s.png' % (i * self.col + j), cubic_img)

    def get_state(self):
        """
        Saves object
        :return: list of tuple (predict, time) for each shoe locker's state
        """

        # get shoe np array
        shoes_arrays = pic_to_np_array(self.row * self.col)
        # predict arrays
        predict_list = predict_shoe(shoes_arrays)

        # set state of each box by using change_status_to
        time_stamped_predict_list = []
        # TODO: fix date time ?
        time = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        for index, predict in enumerate(predict_list):

            print("indexNo= ", index, "Accuracy= ", predict)

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
        :param box_no: box number
        :param status: status True or False
        :param last_in: Last shoe moved in time
        :param last_out: Last shoe move out time
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

    def push_many_status(self):
        """
        Push locker variables to Database
        """

        if self.db_info is None:
            print("ERROR! You should execute set_database_info() before use this method!")
            exit()

        connection = pymysql.connect(host=self.db_info['host'],
                                     user=self.db_info['user'],
                                     password=self.db_info['password'],
                                     db=self.db_info['db'],
                                     charset=self.db_info['charset'],
                                     cursorclass=self.db_info['cursorclass']
                                     )

        # TODO: make new records by loop
        with connection.cursor() as cursor:
            # make new record
            big_command = ()
            # append
            for index in range(self.row * self.col):
                x = int(index / self.col)
                y = int(index % self.row)
                # print("yeah oh yea")
                # print(self.locker[x][y])
                current_box = (str(self.locker[x][y]['recordedTime']), self.locker[x][y]['boxNo'],
                               self.locker[x][y]['status'], str(self.locker[x][y]['lastIn']),
                               str(self.locker[x][y]['lastOut'])
                               )
                big_command = big_command + (current_box,)
            stmt_insert = "INSERT INTO "+self.table_name+" (recordedTime,boxNo,status,lastIn,lastOut) " \
                                                         "VALUES (%s, %s, %s, %s, %s)"
            print(big_command)
            cursor.executemany(stmt_insert, big_command)
            connection.commit()
        return

    def get_recent_data(self):
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
            sql = """select X.recordedTime, X.boxNo, X.status, X.lastIn, X.lastOut
                     from info as X, (select max(recordedTime) as max, boxNo from info group by boxNo) as Y
                     where X.recordedTime = Y.max AND X.boxNo = Y.boxNo;"""
            cursor.execute(sql)
            data = cursor.fetchall()
        connection.close()
        return data

    @staticmethod
    def save_to_folder(image):
        save_to_folder_func(image)


    @staticmethod
    def is_image_good(image):
        if check_image(image):
            return True
        else:
            return False

