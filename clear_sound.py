import sys

from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QAction, QVBoxLayout, QWidget, QRadioButton
from moviepy.editor import VideoFileClip


class CSound(QMainWindow):  # работа с формой очистки видео от звука
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('Clear_Sound.ui', self)
        self.pushButton.clicked.connect(self.browse_folder)

    def browse_folder(self):  # Выбор файла с директории
        self.label.setText('')
        file = QFileDialog.getOpenFileName(self, 'Выберите файл', '')[0]
        self.doc = file
        ffile = file.split('.')[-1]  # получение типа файла без .
        self.format = '.' + str(ffile)  # добавление к типу файла .
        if ffile == 'mp4' or ffile == 'avi':  # проверка типа файла
            self.label.setText('Файл добавлен')
            self.pushButton_2.clicked.connect(self.clear_sound)
        else:
            self.label.setText('Неверный формат файла')

    def clear_sound(self):  # удаление звука с видеофрагмента
        self.label.setText('')
        pname = self.lineEdit.text()
        if pname == '':
            self.label.setText('Введите имя файла')
        else:
            video = VideoFileClip(self.doc)
            new_video = video.without_audio()
            new_video.write_videofile(f'{pname}.mp4')
            self.label.setText('Операция выполнена')
