import sys
import time
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QWidget
from moviepy.editor import VideoFileClip


class CTSound(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('Cut_Sound.ui', self)
        self.pushButton_2.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.label.setText('')
        file = QFileDialog.getOpenFileName(self, 'Выберите файл', '')[0]
        self.doc = file
        forfile = file.split('.')[-1]  # получение типа файла без .
        nfile = file.split('.')[0]
        self.name = str(nfile) + '.mp3'
        if forfile == 'mp4' or forfile == 'avi':  # проверка типа файла
            self.label.setText('Файл добавлен')
            time.sleep(2)
            self.label.setText('Ожидайте')
            self.pushButton.clicked.connect(self.cut_sound)
        else:
            self.label.setText('Неверный формат файла')

    def cut_sound(self):  # функция вырезания звука из видео
        video = VideoFileClip(self.doc)
        video.audio.write_audiofile(self.name)
        self.label.setText('Операция выполнена')
