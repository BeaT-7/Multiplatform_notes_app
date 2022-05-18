import mysql.connector as mysql


class DBConnection():

    def __init__(self):
        self.connection = mysql.connect(
            host="localhost",
            database="note_base",
            user="noteuser",
            password="1232"
        )
        self.cursor = self.connection.cursor()



dbase = DBConnection()
