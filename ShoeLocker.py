import cv2
from functions import *
import datetime

"""
verbs: 
big shoebox: bigShoeBox
small or one shoebox: smallShoeBox
"""

class ShoeLocker:
    def __init__(self, row, col, def_value=(False, "0000-00-00 00:00:00"), row_height=28, col_width=56, kernel_size= (56, 56)):
        """
        :param row: shoe locker's row
        :param col: shoe locker's column
        :param row_height: height of small show box
        :param col_width: width of small show box
        :param kernel_size: kernel size of shoe predicting model.
        """
        self.locker = [[def_value for i in range(col)] for j in range(row)]
        self.row = row
        self.col = col
        self.row_height = row_height
        self.col_width = col_width
        self.kernel_size = (56 , 56)

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

        self.locker[x-1][y-1] = status
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

    def change_locker_edge_points_to(self, shoe_box_edge_points):
        """
        :param raspi_im: Name of picture to dissemble, this time raspi_im
        Set 4 edge point of 
        """
        self.x1x1, self.x1y2, self.x2y1, self.x2y2 = shoe_box_edge_points
        return

    def dissemble_big_shoe_box(self, raspi_im="temp/raspi_pic.jpg"):
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
        pts1 = np.float32([
            self.x1x1, self.x1y2,
            self.x2y1, self.x2y2
            ])
        pts2 = np.float32([
            [0,0], [self.col*self.col_width,0],
            [0,self.row*self.row_height],[self.col*self.col_width,self.row*self.row_height]
            ])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        warped_img = cv2.warpPerspective(
            img, M, (self.col * self.col_width, self.row * self.col_width))

        # save image for shoeBox
        for i in range(0,self.row):
            for j in range(0,self.col):
                shoeBox = warped_img[i*self.row_height : (i+1)*self.row_height , j*self.col_width : (j+1)*self.col_width]
                # Current picture size is 28*56, in order to feed 56*56 kernel, we will resize it to kernel_size
                resized_img = cv2.resize(shoeBox, self.kernel_size)
                cv2.imwrite('temp/box%s.png'%(i*self.col+j),resized_img)
        return self.row*self.col

    def get_state(self, count=int):
        """
        :param count: number of a shoe locker's images
        :return: list of tuple ( i, j, (predict, time)) for each shoe locker's box
            i: row number
            j: column number
            predict: bool if there is shoe or not
            time: time get_state has called
        """

        if(count!=self.row*self.col):
            print("count!=row*col")

        # get shoe np array
        shoe_array = pic_to_np_array(count)
        # predict arrays
        predict_list = predict_shoe(shoe_array)
        # for debug
        # return predict_list
        
        time_stamped_predict_list= []
        time = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        for index, predict in enumerate(predict_list):
            # we found index using below formula
            # index = i*self.col+j
            # i row
            i = int(index/self.col)
            # j column
            j = int(index - i*self.col)
            if(predict > 0.8):
                time_stamped_predict_list.append( (i, j, (True, time)) )
            else:
                time_stamped_predict_list.append( (i, j, (False, time)) )
        return time_stamped_predict_list


    def push_state(self, state):
        """
        :param state: list of the shoe locker's state
        :return: nothing, but push the information to SQL server
        """