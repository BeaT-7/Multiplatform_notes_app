import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import pyautogui


class Group():

    def __init__(self, groupID, userID, groupName):
        self.id = int(groupID)
        self.owner = int(userID)
        self.name = groupName
        self.notes = []

    def appendNote(self, note):
        self.notes.append(note)

    def __len__(self):
        return len(self.notes)

