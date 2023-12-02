import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QAction, QVBoxLayout, QWidget, QRadioButton
from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets
from clear_sound import CSound  # импорт формы: удаление звука из видеозаписи
from cut_sound import CTSound  # импорт формы: вырез звука из видео
from About_Program import About_Program  # импорт формы: о программе
import os
import moviepy
import shutil
import logging
from PIL import Image

without_zvuk = None  # переменная для создания окна очистки звука с видео
without_video = None  # переменная для создания окна выреза звука с видео
about_program = None  # переменная для создания окна о программе


class QMainWindow(QMainWindow):  # создание основного окна, подключение кнопок
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('Конвертор.ui', self)
        self.pushButton.clicked.connect(self.browse_folder)
        self.about_action.triggered.connect(self.about)
        self.about_action2.triggered.connect(self.exit)
        self.pushButton_2.clicked.connect(self.fkonv)
        self.vzvuk.triggered.connect(self.vir_zvuk)
        self.izvuk.triggered.connect(self.izv_zvuk)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
            datefmt='%H:%M:%S',
        )

    def about(self):  # кнопка: О программе
        global about_program
        if about_program is None:
            about_program = About_Program()
        about_program.show()

    def exit(self):  # кнопка выхода
        self.close()
        self.logger.info('Нажата кнопка выхода')

    def browse_folder(self):  # Выбор файла из директории
        file = QFileDialog.getOpenFileName(self, 'Выберите файл', '')[0]
        self.doc = file
        rfile = file.split('.')[-1]  # получение типа файла без "."
        self.t = '.' + str(rfile)  # получение типа файла с "."
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
        global audio
        self.label_3.setText('')
        self.label_4.setText('')
        if self.radioButton_4.isChecked():  # проверка файла на соответствие
            self.logger.info('Выбран тип "Текст"')
            if self.radioButton_3.isChecked():  # Текстовый файл
                type = self.comboBox.currentText()
                if not (self.t == type):
                    new_doc = f'{self.name}{type}'
                    shutil.copy(self.doc, new_doc)
                    self.label_4.setText('Подождите некоторое время')
                    self.logger.info('Процесс конвертации текстового файла начат')
                    while True:
                        if os.path.exists(new_doc):
                            self.logger.info('Процесс конвертации текстового файла окончен')
                            self.label_4.setText('Операция выполнена')
                            break
                else:
                    self.label_3.setText('Файл уже в таком формате')
            else:
                self.label_3.setText('Невозможно конвертировать')
        elif self.radioButton_5.isChecked():
            if self.radioButton_2.isChecked():  # Изображение
                self.logger.info('Выбран тип "Изображение"')
                type = self.comboBox_2.currentText()
                if not (self.t == type):
                    new_image = f'{self.name}{type}'
                    Image.open(self.doc).save(new_image)
                    self.logger.info('Процесс конвертации изображения начат')
                    # os.rename(self.doc, f'{self.name}{type}') - old system
                    self.label_4.setText('Подождите некоторое время')
                    while True:
                        if os.path.exists(new_image):
                            self.logger.info('Процесс конвертации изображения окончен')
                            self.label_4.setText('Операция выполнена')
                            break
                else:
                    self.label_3.setText('Файл уже в таком формате')
            else:
                self.label_3.setText('Невозможно конвертировать')
        elif self.radioButton_6.isChecked():
            if self.radioButton.isChecked():  # Звук
                self.logger.info('Выбран тип "Звук')
                type = self.comboBox_3.currentText()
                type_1 = self.comboBox_3.currentText()
                if not (self.t == type):
                    new_audio = f'{self.name}{type_1}'
                    os.rename(self.doc, f'{self.name}{type}')
                    self.label_4.setText('Подождите некоторое время')
                    while True:
                        if os.path.exists(new_audio):
                            self.logger.info('Процесс обработки звука завершен')
                            self.label_4.setText('Операция выполнена')
                            break
                else:
                    self.label_3.setText('Файл уже в таком формате')
            else:
                self.label_3.setText('Невозможно конвертировать')
        elif self.radioButton_8.isChecked():
            if self.radioButton_7.isChecked():  # архив
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
