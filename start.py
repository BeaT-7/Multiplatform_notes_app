import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import pyautogui
from database import *
import bcrypt


def setScreenSize():
    if not loggedIn:
        widget.setGeometry(200, 200, 800, 600)
    else:
        widget.setGeometry(int(scrWidth*0.1), int(scrHeight*0.05), int(scrWidth*0.8), int(scrHeight*0.9))

def initScreens():
    global widget, mainWin
    mainWin = MainPage()
    widget.addWidget(mainWin)


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
        self.userInput.setText("")
        # password input field
        self.pwInput.setGeometry(QtCore.QRect(180, 255, 300, 40))
        self.pwInput.setFont(font)
        self.pwInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwInput.setText("")
        # username label
        self.userLabel.setGeometry(QtCore.QRect(180, 130, 150, 20))
        self.userLabel.setFont(font)
        self.userLabel.setText("User name")
        # password label
        self.pwLabel.setGeometry(QtCore.QRect(180, 225, 150, 20))
        self.pwLabel.setFont(font)
        self.pwLabel.setText("Password")
        # login button
        self.loginBtn.setGeometry(QtCore.QRect(180, 310, 141, 41))
        self.loginBtn.setFont(font)
        self.loginBtn.setText("Login")
        self.loginBtn.clicked.connect(self.loginCheck)
        # register button
        font.setPointSize(10)
        self.registerBtn.setGeometry(QtCore.QRect(680, 520, 91, 31))
        self.registerBtn.setFont(font)
        self.registerBtn.setText("Register")
        self.registerBtn.clicked.connect(self.toRegisterPage)
        # warning label
        font.setBold(True)
        self.warnLabel.setGeometry(QtCore.QRect(180, 90, 350, 20))
        self.warnLabel.setFont(font)
        self.warnLabel.setStyleSheet("color:red;")

    def loginCheck(self):
        global loggedIn, username
        res = dbase.loginUser(self.userInput.text())
        passw = bytearray(self.pwInput.text(), "UTF-8")
        if bcrypt.checkpw(bytes(passw), bytes(res[0][3], "UTF-8")):
            loggedIn = True
            setScreenSize()
            username = self.userInput.text()
            dbase.setupUser(username)
            initScreens()
            widget.setCurrentWidget(mainWin)
        else:
            self.userInput.setText("")
            self.pwInput.setText("")
            self.warnLabel.setText("Wrong username or email! Try again!")

    def toRegisterPage(self):
        global loggedIn
        widget.setCurrentWidget(registerWin)
        loggedIn = False
        setScreenSize()


class RegisterWin(QWidget):

    def __init__(self):
        super(RegisterWin, self).__init__()
        # button initialization
        self.userLabel = QtWidgets.QLabel(self)
        self.emailLabel = QtWidgets.QLabel(self)
        self.passLabel = QtWidgets.QLabel(self)
        self.rePassLabel = QtWidgets.QLabel(self)
        self.userInput = QtWidgets.QLineEdit(self)
        self.emailInput = QtWidgets.QLineEdit(self)
        self.passwInput = QtWidgets.QLineEdit(self)
        self.rePasswInput = QtWidgets.QLineEdit(self)
        self.registerBtn = QtWidgets.QPushButton(self)
        self.warnLabel = QtWidgets.QLabel(self)
        self.complLabel = QtWidgets.QLabel(self)
        self.toLoginBtn = QtWidgets.QPushButton(self)
        # ui setup
        setScreenSize()
        self.setWindowTitle("Note4G")
        self.InitUI()

    def InitUI(self):
        # font
        font = QtGui.QFont()
        font.setPointSize(12)
        # completion label
        self.complLabel.setStyleSheet("color: green; font-size: 16px")
        self.complLabel.setGeometry(220, 510, 200, 40)
        # warning label
        self.warnLabel.setFont(font)
        self.warnLabel.setGeometry(220, 60, 300, 40)
        self.warnLabel.setStyleSheet("Color: red;")
        # button back to login screen
        self.toLoginBtn.setFont(font)
        self.toLoginBtn.setGeometry(20, 20, 150, 35)
        self.toLoginBtn.setText("Back to Login")
        self.toLoginBtn.clicked.connect(lambda: widget.setCurrentWidget(loginWin))
        # username label
        self.userLabel.setGeometry(QtCore.QRect(220, 270, 260, 40))
        self.userLabel.setFont(font)
        self.userLabel.setText("Enter your password:")
        # username input
        self.userInput.setGeometry(QtCore.QRect(220, 130, 260, 40))
        self.userInput.setFont(font)
        self.userInput.setText("")
        # email label
        self.emailLabel.setGeometry(QtCore.QRect(220, 180, 260, 40))
        self.emailLabel.setFont(font)
        self.emailLabel.setText("Enter your email address:")
        # email input
        self.emailInput.setGeometry(QtCore.QRect(220, 220, 260, 40))
        self.emailInput.setFont(font)
        self.emailInput.setText("")
        # password label
        self.passLabel.setGeometry(QtCore.QRect(220, 90, 260, 40))
        self.passLabel.setFont(font)
        self.passLabel.setText("Enter username:")
        # password input
        self.passwInput.setGeometry(QtCore.QRect(220, 310, 260, 40))
        self.passwInput.setFont(font)
        self.passwInput.setText("")
        self.passwInput.setEchoMode(QtWidgets.QLineEdit.Password)
        # password repeat label
        self.rePassLabel.setGeometry(QtCore.QRect(220, 360, 260, 40))
        self.rePassLabel.setFont(font)
        self.rePassLabel.setText("Re-enter your password:")
        # password repeat input
        self.rePasswInput.setGeometry(QtCore.QRect(220, 400, 260, 40))
        self.rePasswInput.setFont(font)
        self.rePasswInput.setText("")
        self.rePasswInput.setEchoMode(QtWidgets.QLineEdit.Password)
        # register button
        font.setPointSize(14)
        self.registerBtn.setGeometry(QtCore.QRect(220, 460, 260, 40))
        self.registerBtn.setFont(font)
        self.registerBtn.setText("Register")
        self.registerBtn.clicked.connect(self.validateRegister)

    def validateRegister(self):
        # check if unique username
        dbase.cursor.execute(
                f"SELECT id FROM users WHERE '{self.userInput.text()}' = username;")
        res = dbase.cursor.fetchall()
        res = dbase.registerUserValidate(self.userInput.text())
        if len(res) > 0:
            self.warnLabel.setText("Username already taken!")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False
        if len(self.userInput.text()) < 4 or len(self.userInput.text()) > 25:
            self.warnLabel.setText("Usernames length needed is 4 to 25 characters!")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False

        # validate email address
        res = dbase.registerEmailValidate(self.emailInput.text())
        if len(res) > 0:
            self.warnLabel.setText("Email already taken!")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False
        if (self.emailInput.text().find("@") < 1):
            self.warnLabel.setText("Not a valid email address!")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False
        if len(self.emailInput.text()) > 50:
            self.warnLabel.setText("Email address too long!")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False

        # validate password
        if len(self.passwInput.text()) < 6:
            self.warnLabel.setText("Password too short, needs at least 6 characters!")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False
        if len(self.passwInput.text()) > 20:
            self.warnLabel.setText("Password too long, max 20 characters")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False
        if not self.passwInput.text() == self.rePasswInput.text():
            self.warnLabel.setText("Re-entered password doesn't match!")
            self.warnLabel.adjustSize()
            self.emptyFields()
            return False
        # validation complete
        # insert new user into database
        dbase.registerUser(self.userInput.text(), self.emailInput.text(), self.passwInput.text())
        self.emptyFields()
        self.complLabel.setText("You have registered, got back to login screen to Log in")
        self.complLabel.adjustSize()

    def emptyFields(self):
        self.userInput.setText("")
        self.emailInput.setText("")
        self.passwInput.setText("")
        self.rePasswInput.setText("")


class MainPage(QWidget):

    def __init__(self):
        super(MainPage, self).__init__()
        # button initialization
        self.addGroup = QtWidgets.QPushButton(self)
        self.addNote = QtWidgets.QPushButton(self)
        self.noteButtons = []
        self.labels = []
        self.noteDelBtns = []
        self.groupDelBtns = []
        self.getAllNotes()
        # ui setup
        setScreenSize()
        self.setWindowTitle("Note4G")
        self.InitUI()

    def InitUI(self):
        self.addGroup.setGeometry(0,0,120,40)
        self.addGroup.setText("ADD GROUP")
        self.addGroup.clicked.connect(self.addGroupName)
        self.addNote.setGeometry(125, 0, 120, 40)
        self.addNote.setText("ADD NOTE")
        self.addNote.clicked.connect(self.addNoteName)
        self.showNotes()

    def getAllNotes(self):
        for i in self.noteButtons:
            i.deleteLater()
            i = None
        for i in self.noteDelBtns:
            i.deleteLater()
            i = None
        for i in self.labels:
            i.deleteLater()
            i = None
        for i in self.groupDelBtns:
            i.deleteLater()
            i = None
        self.noteButtons = []
        self.labels = []
        self.noteDelBtns = []
        self.groupDelBtns = []
        for group in range(len(dbase.groups)):
            self.labels.append(QtWidgets.QLabel(self))
            self.groupDelBtns.append(QtWidgets.QPushButton(self))
            for note in range(len(dbase.groups[group].notes)):
                self.noteButtons.append(QtWidgets.QPushButton(self))
                self.noteDelBtns.append(QtWidgets.QPushButton(self))

    def showNotes(self):
        y = 40
        noteY = 90
        noteX = 20
        counter = 0
        noteCounter = 0
        for group in range(len(self.labels)):
            self.labels[group].setGeometry(0, y, 1500, 40)
            self.labels[group].setText(dbase.groups[group].name)
            self.labels[group].setStyleSheet(
                "font-size: 24px;"
                "font-weight: 500;"
                "background-color: #A9A9A9;"
                "padding-left:20px;"
            )
            self.groupDelBtns[group].setGeometry(1420, y + 10, 60, 20)
            self.groupDelBtns[group].setText("Delete")
            self.groupDelBtns[group].clicked.connect(lambda checked, arg=group: self.groupDelete(arg))

            self.groupDelBtns[group].show()
            self.labels[group].show()

            for note in range(len(dbase.groups[group].notes)):
                self.noteButtons[noteCounter].setGeometry(noteX, noteY, dbase.groups[group].notes[note].size[0], dbase.groups[group].notes[note].size[1])
                self.noteButtons[noteCounter].setText(dbase.groups[group].notes[note].name)
                self.noteButtons[noteCounter].setStyleSheet(
                    "backgroundcolor: #805353;"
                    "font-size: 16px"
                )
                IDs = (group, note, noteCounter)
                self.noteButtons[noteCounter].clicked.connect(lambda checked, arg=IDs: self.openEditor(arg))

                self.noteDelBtns[noteCounter].setGeometry(noteX + 78, noteY + 2, 20, 20)
                self.noteDelBtns[noteCounter].setText("X")
                self.noteDelBtns[noteCounter].clicked.connect(lambda checked, arg=IDs: self.noteDelete(arg))

                self.noteDelBtns[noteCounter].show()
                self.noteButtons[noteCounter].show()

                if counter > 10:
                    counter = 0
                    noteX = 20
                    noteY += 150
                    y += 200
                else:
                    noteX += 110
                    counter += 1
                noteCounter += 1
            y += 200
            noteY += 200
            noteX = 20

    def openEditor(self, IDs):
        htmlText = dbase.groups[IDs[0]].notes[IDs[1]].text
        noteWin.editor.clear()
        noteWin.editor.insertHtml(htmlText)
        noteWin.currentNote = IDs
        widget.setCurrentWidget(noteWin)

    def groupDelete(self, val):
        ID = dbase.groups[val].id
        empty = True
        if len(dbase.groups[val].notes) > 0:
            empty = False
        dbase.deleteGroup(ID, empty)
        self.getAllNotes()
        self.showNotes()

    def noteDelete(self, IDs):
        ID = dbase.groups[IDs[0]].notes[IDs[1]].id
        dbase.deleteNote(ID)
        self.getAllNotes()
        self.showNotes()

    def addGroupName(self):
        self.popUp = PopUp(True)
        self.popUp.show()

    def addNoteName(self):
        self.popUp = PopUp(False)
        self.popUp.show()


class PopUp(QWidget):

    def __init__(self, isGroup):
        super(PopUp, self).__init__()
        # button initialization
        self.label = QtWidgets.QLabel(self)
        self.button = QtWidgets.QPushButton(self)
        self.name = QtWidgets.QLineEdit(self)
        self.addedLabel = QtWidgets.QLabel(self)
        self.isGroup = isGroup
        self.groupCombo = QtWidgets.QComboBox(self)
        self.groupLabel = QtWidgets.QLabel(self)
        # UI setup
        self.setGeometry(300, 300, 450, 300)
        self.InitUI()


    def InitUI(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addedLabel.setFont(font)
        self.addedLabel.setGeometry(50, 300, 200, 40)
        self.addedLabel.setStyleSheet("color: red;")
        if self.isGroup:
            # Create group window
            self.groupCombo.hide()
            self.groupLabel.hide()
            self.setWindowTitle("Add Group")
            self.label.setGeometry(100, 65, 300, 40)
            self.label.setFont(font)
            self.label.setText("Enter new Groups name:")
            self.name.setGeometry(100,100, 200, 40)
            self.name.setFont(font)
            self.button.setGeometry(100, 150, 100, 40)
            self.button.setText("Create")
            self.button.setFont(font)
            self.button.clicked.connect(self.newGroup)
        else:
            # Create note window
            self.setWindowTitle("Add Note")
            self.groupCombo.setGeometry(280, 100, 150, 40)
            self.groupCombo.setFont(font)
            groups = dbase.getAllGroupNames()
            self.groupCombo.addItems(groups)
            self.groupCombo.setCurrentText("Default")
            self.groupLabel.setGeometry(280, 65, 200, 40)
            self.groupLabel.setFont(font)
            self.groupLabel.setText("Add To Group:")
            self.label.setGeometry(30, 65, 220, 40)
            self.label.setFont(font)
            self.label.setText("Enter new notes name:")
            self.name.setGeometry(30, 100, 220, 40)
            self.name.setFont(font)
            self.button.setGeometry(30, 150, 100, 40)
            self.button.setText("Create")
            self.button.setFont(font)
            self.button.clicked.connect(self.newNote)

    def newGroup(self):
        if len(self.name.text()) > 30 or len(self.name.text()) == 0:
            self.addedLabel.setText("Group name too long!")
        else:
            dbase.createGroup(self.name.text())
            mainWin.getAllNotes()
            mainWin.showNotes()
            self.close()

    def newNote(self):
        if len(self.name.text()) > 30 or len(self.name.text()) == 0:
            self.addedLabel.setText("Note name too long!")
        else:
            dbase.createNote(self.name.text(), self.groupCombo.currentText())
            mainWin.getAllNotes()
            mainWin.showNotes()
            self.close()


class NotePage(QWidget):

    def __init__(self):
        super(NotePage, self).__init__()
        self.currentNote = (0, 0)
        # button initialization
        self.font = QtGui.QFont()
        self.editor = QtWidgets.QTextEdit(self)
        self.fontComboBox = QtWidgets.QFontComboBox(self)
        self.spinBox = QtWidgets.QSpinBox(self)
        self.txtAlignLeft = QtWidgets.QPushButton(QIcon('images/edit-alignment.png'), "", self)
        self.txtAlignCenter = QtWidgets.QPushButton(QIcon('images/edit-alignment-center.png'), "", self)
        self.txtAlignRight = QtWidgets.QPushButton(QIcon('images/edit-alignment-right.png'), "", self)
        self.txtAlignJustify = QtWidgets.QPushButton(QIcon('images/edit-alignment-justify.png'), "", self)
        self.boldText = QtWidgets.QPushButton(QIcon('images/edit-bold.png'), "", self)
        self.italicText = QtWidgets.QPushButton(QIcon('images/edit-italic.png'), "", self)
        self.underlineText = QtWidgets.QPushButton(QIcon('images/edit-underline.png'), "", self)
        self.export = QtWidgets.QPushButton(self)
        self.closeBtn = QtWidgets.QPushButton(self)
        # ui setup
        setScreenSize()
        self.setWindowTitle("Note4G")
        self.InitUI()

    def InitUI(self):
        # close button
        self.closeBtn.setGeometry(1496, 0, 40,40)
        self.closeBtn.setText("Close")
        self.closeBtn.clicked.connect(self.closeEditor)
        # export button
        self.export.setGeometry(700, 0, 120, 40)
        self.export.setText("export")
        self.export.clicked.connect(self.exportHTML)
        # font select combo box
        self.fontComboBox.setGeometry(QtCore.QRect(0, 0, 231, 41))
        self.fontComboBox.currentFontChanged.connect(lambda: self.editor.setFontFamily(self.fontComboBox.currentText()))
        # font size spinBox
        self.spinBox.setGeometry(QtCore.QRect(230, 0, 51, 41))
        self.spinBox.setMinimum(4)
        self.spinBox.setMaximum(88)
        self.spinBox.setSingleStep(2)
        self.spinBox.setProperty("value", 12)
        self.spinBox.valueChanged.connect(lambda: self.editor.setFontPointSize(self.spinBox.value()))
        # font
        self.font.setPointSize(self.spinBox.value())
        self.font.setKerning(True)
        # text align left
        self.txtAlignLeft.setGeometry(282, 0, 40, 40)
        self.txtAlignLeft.setStatusTip("Align text left")
        self.txtAlignLeft.clicked.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        # text align center
        self.txtAlignCenter.setGeometry(322, 0, 40, 40)
        self.txtAlignCenter.setStatusTip("Center text")
        self.txtAlignCenter.clicked.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        # text align right
        self.txtAlignRight.setGeometry(362, 0, 40, 40)
        self.txtAlignRight.setStatusTip("Align text Right")
        self.txtAlignRight.clicked.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        # text align justify
        self.txtAlignJustify.setGeometry(402, 0, 40, 40)
        self.txtAlignJustify.setStatusTip("Justify text")
        self.txtAlignJustify.clicked.connect(lambda: self.editor.setAlignment(Qt.AlignJustify))
        # text bold
        self.boldText.setGeometry(442, 0, 40, 40)
        self.boldText.setStatusTip("Bold text")
        self.boldText.setCheckable(True)
        self.boldText.toggled.connect(lambda x: self.editor.setFontWeight(QFont.Bold if x else QFont.Normal))
        # text italic
        self.italicText.setGeometry(482, 0, 40, 40)
        self.italicText.setStatusTip("Italic text")
        self.italicText.setCheckable(True)
        self.italicText.toggled.connect(self.editor.setFontItalic)
        # text underline
        self.underlineText.setGeometry(522, 0, 40, 40)
        self.underlineText.setStatusTip("Underline text")
        self.underlineText.setCheckable(True)
        self.underlineText.toggled.connect(self.editor.setFontUnderline)
        # editor
        self.editor.setGeometry(QtCore.QRect(0, 40, int(scrWidth * 0.8), int(scrHeight * 0.9)))
        self.editor.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.editor.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.editor.setFont(self.font)
        self.editor.setText("")

    def closeEditor(self):
        dbase.saveNoteText(self.editor.toHtml(), self.currentNote)
        self.editor.clear()
        dbase.getAllNotes()
        widget.setCurrentWidget(mainWin)

    def exportHTML(self):
        text = self.editor.toHtml()
        with open("text.txt", "w") as file:
            file.writelines(text)


# applications initialization
app = QApplication(sys.argv)

# setup variables
widget = QtWidgets.QStackedWidget()
scrWidth = pyautogui.size()[0]
scrHeight = pyautogui.size()[1]
loggedIn = False
username = ""
userID = ""

# page class initializations
loginWin = LoginWin()
registerWin = RegisterWin()
mainWin = None
noteWin = NotePage()

# Pages added to StackedWidget and displayed
widget.addWidget(loginWin)
widget.addWidget(registerWin)
widget.addWidget(noteWin)
widget.show()

# End GUI
sys.exit(app.exec())
