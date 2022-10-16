import os
import sys

from PyQt5 import uic, QtGui, QtCore, QtWebEngine
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWebEngineWidgets import QWebEngineView


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
        self.try_window = TryWindow()
        self.try_window.show()
        self.hide()


class LearnWindow(QMainWindow):  # (QtWebEngine.QtWebEngine): # (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Learn_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.Btn_1.clicked.connect(self.show_text)
        self.Btn_2.clicked.connect(self.show_text)
        self.Btn_3.clicked.connect(self.show_text)
        self.Btn_4.clicked.connect(self.show_text)
        self.Btn_5.clicked.connect(self.show_text)
        self.Btn_6.clicked.connect(self.show_text)
        self.Btn_7.clicked.connect(self.show_text)
        self.Btn_8.clicked.connect(self.show_text)
        self.Btn_9.clicked.connect(self.show_text)
        self.Btn_10.clicked.connect(self.show_text)
        self.Btn_11.clicked.connect(self.show_text)
        self.Btn_12.clicked.connect(self.show_text)
        self.Btn_13.clicked.connect(self.show_text)

        self.BackBtn.clicked.connect(self.go_back)

    def go_back(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()

    def show_text(self):
        match self.sender().objectName():
            case "Btn_1":
                with open('lessons/lesson_1.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_2":
                with open('lessons/lesson_2.html', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_3":
                with open('lessons/lesson_3.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_4":
                PDFJS = '' # как прописать правильный путь? как вернуть привязку от размера окна для QWebEngineView
                PDF = f'file://{os.path.abspath("lessons/pdf.pdf")}'
                self.graphicsView.load(QtCore.QUrl.fromUserInput(f'{PDFJS}?file={PDF}'))

            # self.graphicsView(QtCore.QUrl.fromUserInput('%s?file=%s' % 'pdf_js/web/viewer.html', 'lessons/pdf.pdf'))
            # s.graphicsView(QtCore.QUrl.fromUserInput('%s?file=%s' % ("pdf_js/web/viewer.html", "lessons/pdf.pdf")))
                # with open('lessons/lesson_4.txt', mode='rt', encoding='utf-8') as f:
                #     data = f.read()
                # self.textBrowser.setText(data)
            case "Btn_5":
                with open('lessons/lesson_5.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_6":
                with open('lessons/lesson_6.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_7":
                with open('lessons/lesson_7.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_8":
                with open('lessons/lesson_8.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_9":
                with open('lessons/lesson_9.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_10":
                with open('lessons/lesson_10.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_11":
                with open('lessons/lesson_11.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_12":
                with open('lessons/lesson_12.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)
            case "Btn_13":
                with open('lessons/lesson_13.txt', mode='rt', encoding='utf-8') as f:
                    data = f.read()
                self.textBrowser.setText(data)

# self.textBrowser.anchorClicked.connect(QtGui.QDesktopServices.openUrl)


class TryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Try_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.BackBtn.clicked.connect(self.go_back)

    def go_back(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Подключение стилей {
    file = QFile("res/darkstyle.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    # Подключение стилей }
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())
