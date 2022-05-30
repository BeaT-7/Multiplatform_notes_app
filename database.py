import mysql.connector as mysql
from Groups import Group
from Notes import Note


class DBConnection():

    def __init__(self):
        self.connection = mysql.connect(
            #host="localhost",
            #database="note_base",
            #user="noteuser",
            #password="1232"
            host="sql11.freemysqlhosting.net",
            user="sql11496494",
            password="psppHndwlA",
            database="sql11496494"
        )
        self.cursor = self.connection.cursor()
        self.conUserId = 0
        self.conUsername = ""
        self.conUserEmail = ""
        self.groups = []


    def setupUser(self, username):
        sql = f"SELECT id, username, email FROM users WHERE username = '{username}'"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.conUserId = int(res[0][0])
        self.conUsername = res[0][1]
        self.conUserEmail = res[0][2]
        self.getAllGroups()
        self.getAllNotes()


    def loginUser(self, username, password):
        sql = f"SELECT id FROM users WHERE '{username}' = username AND '{password}' = password;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def registerUserValidate(self, username):
        sql = f"SELECT id FROM users WHERE '{username}' = username;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def registerEmailValidate(self, email):
        sql = f"SELECT id FROM users WHERE '{email}' = email;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def registerUser(self, username, email, password):
        # create user
        sql = f"INSERT INTO users(username, email, password) VALUES (" \
              f"'{username}', '{email}', '{password}'" \
              f")"
        self.cursor.execute(sql)
        self.connection.commit()
        # create default note group for the user
        sql = f"SELECT id FROM users WHERE username = '{username}'"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.conUserId = int(res[0][0])
        sql = f"INSERT INTO sql11496494.groups(owner, group_name) VALUES ('{self.conUserId}', 'Default')"
        self.cursor.execute(sql)
        self.connection.commit()

    def createGroup(self, groupName):
        sql = f"INSERT INTO sql11496494.groups(owner, group_name) VALUES ('{self.conUserId}', '{groupName}')"
        self.cursor.execute(sql)
        self.connection.commit()
        self.getAllGroups()

    def createNote(self, noteName, groupName):
        #gets groups ID
        id = 0
        for group in self.groups:
            if group.name == groupName:
                id = group.id
        sql = f"INSERT INTO sql11496494.notes(notes.group, note_name, text) VALUES ('{id}', '{noteName}', '')"
        self.cursor.execute(sql)
        self.connection.commit()
        self.getAllNotes()

    def getAllGroups(self):
        sql = f"SELECT * FROM sql11496494.groups WHERE owner = {self.conUserId}"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        self.groups = []
        for i in range(len(res)):
            self.groups.append(Group(res[i][0], res[i][1], res[i][2]))

    def getAllNotes(self):
        groupIDs = ()
        for group in self.groups:
            groupIDs += (group.id, )
        if len(groupIDs) == 1:
            groupIDs +=(0,)
        sql = f"SELECT * FROM sql11496494.notes WHERE notes.group in {groupIDs}"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for group in self.groups:
            group.notes = []
            for i in range(len(res)):
                if group.id == res[i][1]:
                    group.appendNote(Note(res[i][0], res[i][1], res[i][2], res[i][3]))

    def getAllGroupNames(self):
        groupNames = []
        for group in self.groups:
            groupNames.append(group.name)
        return groupNames

    def saveNoteText(self, text, note):
        sql = f"UPDATE sql11496494.notes SET text = '{text}' WHERE id = {self.groups[note[0]].notes[note[1]].id}"
        sql = sql.replace("'", "\\'").replace("\\' WHERE id = ", "' WHERE id = ").replace('sql11496494.notes SET text = \\', "sql11496494.notes SET text = ")
        self.cursor.execute(sql)
        self.connection.commit()


dbase = DBConnection()
