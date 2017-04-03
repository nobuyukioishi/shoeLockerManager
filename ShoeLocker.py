from functions import *


class ShoeLocker:
    def __init__(self, row, col, def_value=(False, "0000-00-00 00:00:00")):
        """
        :param row: shoe locker's row
        :param col: shoe locker's column
        """
        self.locker = [[def_value for i in range(col)] for j in range(row)]

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

        self.locker[x][y] = status
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

    def dissemble_big_picture(self, raspi_im="temp/raspi_pic.jpg"):
        """
        :param raspi_im: Name of picture to dissemble, this time raspi_im
        :return count: number of dissembled picture
        Save dissembled pictures to temp/, names box%s.png %s is integer goes 0 to count-1
        """
        


    def get_state(self, count=int):
        """
        :param imgs: list of a shoe locker's images
        :return: list of tuple (predict, time) for each shoe locker's state
        """

        if(count!=row*col):
            print("count!=row*col")
            break
        
        # get shoe np array
        shoesArray = functions.pic_to_np_array(count)
        # predict arrays
        predict_list = functions.predict(shoesArray)
        print(shoesArray)
        
        time_stamped_predict_list= []
        time = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        for predict in predict_list:
            time_stamped_predict_list.append( (predict, time) )
        return time_stamped_predict_list


    def push_state(self, state):
        """
        :param state: list of the shoe locker's state
        :return: nothing, but push the information to SQL server
        """