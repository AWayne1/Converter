import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QAction, QVBoxLayout, QWidget, QRadioButton
from PyQt5 import uic
from PyQt5 import QtWidgets
from clear_sound import CSound  # импорт формы: удаление звука из видеозаписи
from cut_sound import CTSound  # импорт формы: вырез звука из видео
import os
import moviepy

without_zvuk = None  # переменная для создания окна очистки звука с видео
without_video = None  # переменная для создания окна выреза звука с видео


class AboutWindow(QWidget):  # создание окна: О программе
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText('Конвертор файлов в различные форматы: \n Текстовый файл: 1) .txt 2) .doc 3) .rtf; \n'
                          'Изображение: 1) .png 2) .jpeg 3) .bmp; \n Звуковой файл: 1) .wav 2) .mp3 3) .mid')
        self.layout().addWidget(self.info)


class QMainWindow(QMainWindow):  # создание основного окна, подключение кнопок
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('Конвертор.ui', self)
        self.pushButton.clicked.connect(self.browse_folder)
        self.about_action.triggered.connect(self.about)
        self.about_window = AboutWindow()
        self.about_action2.triggered.connect(self.exit)
        self.pushButton_2.clicked.connect(self.fkonv)
        self.vzvuk.triggered.connect(self.vir_zvuk)
        self.izvuk.triggered.connect(self.izv_zvuk)

    def about(self):  # кнопка: О программе
        self.about_window.show()

    def exit(self):  # кнопка выхода
        sys.exit('Goodbye')

    def browse_folder(self):  # Выбор файла из директории
        file = QFileDialog.getOpenFileName(self, 'Выберите файл', '')[0]
        self.doc = file
        rfile = file.split('.')[-1]  # получение типа файла без .
        self.t = '.' + str(rfile)  # получение типа файла с .
        ffile = file.split('.')[0]  # получение названия файла
        self.name = ffile
        self.label_4.setText('')
        self.label_3.setText('')
        # проверка соответствия кнопок и типа файла
        if self.radioButton_3.isChecked() and (rfile == 'docx' or rfile == 'txt' or rfile == 'doc' or rfile == 'rtf'):
            self.label_4.setText('Файл добавлен')

        elif self.radioButton_2.isChecked() and (rfile == 'jpeg' or rfile == 'png' or rfile == 'bmp' or rfile == 'jpg'):
            self.label_4.setText('Файл добавлен')

        elif self.radioButton.isChecked() and (rfile == 'wav' or rfile == 'mp3' or rfile == 'kar' or rfile == 'ogg'):
            self.label_4.setText('Файл добавлен')

        elif self.radioButton_7.isChecked() and (rfile == 'rar' or rfile == 'zip' or rfile == 'arj'):
            self.label_4.setText('Файл добавлен')

        else:
            self.label_3.setText('Неверный формат файла!')

    def fkonv(self):  # конвертация файла
        self.label_3.setText('')
        self.label_4.setText('')
        if self.radioButton_4.isChecked():  # проверка файла на соответствие
            if self.radioButton_3.isChecked():
                type = self.comboBox.currentText()
                if not (self.t == type):
                    os.rename(self.doc, f'{self.name}{type}')
                    self.label_4.setText('Операция выполнена')
                else:
                    self.label_3.setText('Файл уже в таком формате')
            else:
                self.label_3.setText('Невозможно конвертировать')
        elif self.radioButton_5.isChecked():
            if self.radioButton_2.isChecked():
                type = self.comboBox_2.currentText()
                if not (self.t == type):
                    os.rename(self.doc, f'{self.name}{type}')
                    self.label_4.setText('Операция выполнена')
                else:
                    self.label_3.setText('Файл уже в таком формате')
            else:
                self.label_3.setText('Невозможно конвертировать')
        elif self.radioButton_6.isChecked():
            if self.radioButton.isChecked():
                type = self.comboBox_3.currentText()
                if not (self.t == type):
                    os.rename(self.doc, f'{self.name}{type}')
                    self.label_4.setText('Операция выполнена')
                else:
                    self.label_3.setText('Файл уже в таком формате')
            else:
                self.label_3.setText('Невозможно конвертировать')
        elif self.radioButton_8.isChecked():
            if self.radioButton_7.isChecked():
                type = self.comboBox_4.currentText()
                if not (self.t == type):
                    os.rename(self.doc, f'{self.name}{type}')
                    self.label_4.setText('Операция выполнена')
                else:
                    self.label_3.setText('Файл уже в таком формате')
            else:
                self.label_3.setText('Невозможно конвертировать')

    def vir_zvuk(self):  # обработка нажатия на кнопку: Удаление звука из видео
        global without_zvuk
        if without_zvuk is None:
            without_zvuk = CSound()
        without_zvuk.show()

    def izv_zvuk(self):
        global without_video
        if without_video is None:
            without_video = CTSound()
        without_video.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QMainWindow()
    ex.show()
    sys.exit(app.exec_())
