import mysql.connector
import os,getpass


class Mysqldata:
    # __password = os.environ['MYSQLPWD']

    def __init__(self, pwd):
        self.__password = pwd
        self.dbcon = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd=self.__password,
            database='world'
        )
        self.dbcur = self.dbcon.cursor()

    def fetch(self, opt):
        sqlstmt = "SELECT * FROM "
        if opt == 1:
            sqlstmt += "CITY"
        elif opt == 2:
            sqlstmt += "country"
        elif opt == 3:
            sqlstmt += "countrylanguage"
        else:
            print('Wrong Input')
            exit()
        self.dbcur.execute(sqlstmt)
        self.data = self.dbcur.fetchall()
        for i in self.data:
            print(i)

    def __del__(self):
        self.dbcon.close


pwd = getpass.getpass(prompt="Enter the Password")
obj = Mysqldata(pwd)

opt = int(input('1.City\n2.country\n3.Country Languages\nWhich table needed?'))

obj.fetch(opt)
