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

    def get_state(self, imgs):
        """

        :param imgs: list of a shoe locker's images
        :return: list of the shoe locker's state
        """

    def push_state(self, state):
        """

        :param state: list of the shoe locker's state
        :return: nothing, but push the information to SQL server
        """