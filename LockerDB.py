import pymysql.cursors

class LockerDB:

    def __init__(self, host, user, password, db, charset="utf8", cursorclass=pymysql.cursors.DictCursor):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.cursorclass = cursorclass

