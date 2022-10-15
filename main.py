import asyncio
import logging
import sys
import time

from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class StartWindow(QMainWindow):
    def open_menu(self):
        self.main_window = MenuWindow()
        self.main_window.show()
        self.hide()

    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Start_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        # Устанавливаем заставку
        self.StartButton.clicked.connect(self.open_menu)
        self.StartButton.setIcon(QtGui.QIcon('res/App_logo.png'))
        self.StartButton.setIconSize(QtCore.QSize(843, 843))


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Menu_window.ui', self)  # Загружаем дизайн
        # Настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')
        # Привязываем к кнопкам действия
        self.GoLearnButton.clicked.connect(self.go_learn)
        self.GoTryButton.clicked.connect(self.go_try)

    def go_learn(self):
        self.learn_window = LearnWindow()
        self.learn_window.show()
        self.hide()

    def go_try(self):
        pass


class LearnWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Learn_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())
