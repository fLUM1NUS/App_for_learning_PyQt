import sys

from PyQt5 import uic, QtGui, QtCore, QtWebEngineWidgets, QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

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
        self.SettingsBtn.clicked.connect(self.go_settings)

    def go_learn(self):
        self.learn_window = LearnWindow()
        self.learn_window.show()
        self.hide()

    def go_try(self):
        self.try_window = TryWindow()
        self.try_window.show()
        self.hide()

    def go_settings(self):
        self.sw = SettingsWindow()
        self.sw.show()
        self.hide()


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Settings_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.BackBtn.clicked.connect(self.go_back)
        self.EnDarkBtn.clicked.connect(self.set_theme)

    def go_back(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()

    def set_theme(self):
        with open('res/settings.txt', mode='r') as f:
            th_settings = f.read()
        if th_settings == 'True':
            t_settings = 'False'
        if th_settings == 'False':
            t_settings = 'True'
        with open('res/settings.txt', mode='w') as f:
            f.write(t_settings)
            print(t_settings)
        window = QtWidgets.QMainWindow()
        window.show()
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)


class LearnWindow(QMainWindow):
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

        self.graphicsView.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.graphicsView.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.graphicsView.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.graphicsView.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.PDFJS = 'file:///pdf_js/web/viewer.html'

    def go_back(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()

    def show_text(self):
        match self.sender().objectName():
            case "Btn_1":
                PDF = 'file:///lessons/lesson_1.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_2":
                PDF = 'file:///lessons/lesson_2.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_3":
                PDF = 'file:///lessons/lesson_3.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_4":
                PDF = 'file:///lessons/lesson_4.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_5":
                PDF = 'file:///lessons/lesson_5.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_6":
                PDF = 'file:///lessons/lesson_6.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_7":
                PDF = 'file:///lessons/lesson_7.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_8":
                PDF = 'file:///lessons/lesson_8.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_9":
                PDF = 'file:///lessons/lesson_8.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_10":
                PDF = 'file:///lessons/lesson_8.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_11":
                PDF = 'file:///lessons/lesson_8.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_12":
                PDF = 'file:///lessons/lesson_8.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))
            case "Btn_13":
                PDF = 'file:///lessons/lesson_8.pdf'
                self.graphicsView.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (self.PDFJS, PDF)))


class TryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/Try_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.BackBtn.clicked.connect(self.go_back)
        self.TryQBrowserBtn.clicked.connect(self.go_try_html)

    def go_back(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()

    def go_try_html(self):
        self.try_html_window = TryHtmlWindow()
        self.try_html_window.show()
        self.hide()


class TryHtmlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/TryHtml_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.BackBtn.clicked.connect(self.go_back)

    def go_back(self):
        self.try_window = TryWindow()
        self.try_window.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Подключение стилей {
    with open('res/settings.txt', mode='r') as f:
        settings = f.read()
    if not (settings == 'True' or settings == 'False'):
        settings = 'False'
    if settings == 'True':
        file = QFile("res/darkstyle.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())
    # Подключение стилей }
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())
