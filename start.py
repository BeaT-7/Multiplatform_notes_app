import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import pyautogui
from database import dbase


def setScreenSize():
    if not loggedIn:
        widget.setGeometry(200, 200, 800, 600)
    else:
        widget.setGeometry(int(scrWidth*0.1), int(scrHeight*0.05), int(scrWidth*0.8), int(scrHeight*0.9))


class LoginWin(QWidget):

    def __init__(self):
        super(LoginWin, self).__init__()
        # button initialization
        self.registerBtn = QtWidgets.QPushButton(self)
        self.loginBtn = QtWidgets.QPushButton(self)
        self.pwLabel = QtWidgets.QLabel(self)
        self.userLabel = QtWidgets.QLabel(self)
        self.userInput = QtWidgets.QLineEdit(self)
        self.pwInput = QtWidgets.QLineEdit(self)
        self.warnLabel = QtWidgets.QLabel(self)
        # ui setup
        setScreenSize()
        self.setWindowTitle("Note4G")
        self.InitUI()

    def InitUI(self):
        font = QtGui.QFont()
        font.setPointSize(14)
        # username input field
        self.userInput.setGeometry(QtCore.QRect(180, 160, 300, 40))
        self.userInput.setFont(font)
        self.userInput.setObjectName("userInput")
        self.userInput.setText("")
        # password input field
        self.pwInput.setGeometry(QtCore.QRect(180, 255, 300, 40))
        self.pwInput.setFont(font)
        self.pwInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwInput.setObjectName("pwInput")
        self.pwInput.setText("")
        # username label
        self.userLabel.setGeometry(QtCore.QRect(180, 130, 150, 20))
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.userLabel.setText("User name")
        # password label
        self.pwLabel.setGeometry(QtCore.QRect(180, 225, 150, 20))
        self.pwLabel.setFont(font)
        self.pwLabel.setObjectName("pwLabel")
        self.pwLabel.setText("Password")
        # login button
        self.loginBtn.setGeometry(QtCore.QRect(180, 310, 141, 41))
        self.loginBtn.setFont(font)
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.setText("Login")
        self.loginBtn.clicked.connect(self.loginCheck)
        # register button
        font.setPointSize(10)
        self.registerBtn.setGeometry(QtCore.QRect(680, 520, 91, 31))
        self.registerBtn.setFont(font)
        self.registerBtn.setObjectName("RegisterBtn")
        self.registerBtn.setText("Register")
        self.registerBtn.clicked.connect(self.toRegisterPage)
        # warning label
        font.setBold(True)
        self.warnLabel.setGeometry(QtCore.QRect(180, 90, 350, 20))
        self.warnLabel.setFont(font)
        self.warnLabel.setObjectName("warnLabel")
        self.warnLabel.setStyleSheet("color:red;")

    def loginCheck(self):
        global loggedIn
        dbase.cursor.execute(f"SELECT id FROM users WHERE '{self.userInput.text()}' = username AND '{self.pwInput.text()}' = password;")
        res = dbase.cursor.fetchall()
        if len(res) < 1:
            self.userInput.setText("")
            self.pwInput.setText("")
            self.warnLabel.setText("Wrong username or email! Try again!")
            print("Failed to log in!")
        else:
            loggedIn = True
            setScreenSize()
            widget.setCurrentWidget(mainWin)

    def toRegisterPage(self):
        global loggedIn
        widget.setCurrentWidget(registerWin)
        loggedIn = False
        setScreenSize()


class RegisterWin(QWidget):

    def __init__(self):
        super(RegisterWin, self).__init__()
        # button initialization
        self.label1 = QtWidgets.QLabel(self)
        # ui setup
        setScreenSize()
        self.setWindowTitle("Note4G")
        self.InitUI()

    def InitUI(self):
        self.label1.setGeometry(200, 200, 300, 100)
        self.label1.setText("Register page, work in progress!")


class MainPage(QWidget):

    def __init__(self):
        super(MainPage, self).__init__()
        # button initialization
        self.note = QtWidgets.QTextEdit(self)
        # ui setup
        setScreenSize()
        self.setWindowTitle("Note4G")
        self.InitUI()

    def InitUI(self):
        self.note.setGeometry(200, 200, 500, 300)
        self.note.setObjectName("note")
        self.note.setText("")

# applications initialization
app = QApplication(sys.argv)

# setup variables
widget = QtWidgets.QStackedWidget()
scrWidth = pyautogui.size()[0]
scrHeight = pyautogui.size()[1]
loggedIn = False

# page class initializations
loginWin = LoginWin()
registerWin = RegisterWin()
mainWin = MainPage()

# Pages added to StackedWidget and displayed
widget.addWidget(loginWin)
widget.addWidget(registerWin)
widget.addWidget(mainWin)
widget.show()

# End GUI
sys.exit(app.exec())
