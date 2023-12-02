import sys
import time
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QWidget


class About_Program(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('About_Program.ui', self)

