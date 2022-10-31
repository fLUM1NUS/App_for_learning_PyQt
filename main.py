import sys

import PyQt5.QtWidgets
from PyQt5 import uic, QtGui, QtCore, QtWebEngineWidgets, QtWidgets
import PyQt5.QtWebEngine
# from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

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
        self.TryImgBtn.clicked.connect(self.go_try_img)
        self.TryDBBtn.clicked.connect(self.go_try_db)

    def go_back(self):
        self.menu_window = MenuWindow()
        self.menu_window.show()
        self.hide()

    def go_try_html(self):
        self.try_html_window = TryHtmlWindow()
        self.try_html_window.show()
        self.hide()

    def go_try_img(self):
        self.try_img_window = TryImgWindow()
        self.try_img_window.show()
        self.hide()

    def go_try_db(self):
        self.try_bd_window = TryDBWindow()
        self.try_bd_window.show()
        self.hide()


class TryHtmlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/TryHtml_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.BackBtn.clicked.connect(self.go_back)
        self.ConvertBtn.clicked.connect(self.convert)
        self.LoadExampleBtn.clicked.connect(self.load_example)
        self.LoadPatternBtn.clicked.connect(self.load_pattern)

    def convert(self):
        self.textBrowser.setHtml(self.textEdit.toPlainText())

    def load_example(self):
        with open('res/html_example.html', mode='r', encoding='utf-8') as f:
            data = f.read()
        self.textEdit.setPlainText(data)
        self.convert()

    def load_pattern(self):
        with open('res/pattern.html', mode='r', encoding='utf-8') as f:
            data = f.read()
        self.textEdit.setPlainText(data)
        self.convert()

    def go_back(self):
        self.try_window = TryWindow()
        self.try_window.show()
        self.hide()


class TryImgWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/TryImg_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.go_default()

        self.backBtn.clicked.connect(self.go_back)
        self.openBtn.clicked.connect(self.open_img)
        self.goDefaultBtn.clicked.connect(self.go_default)

    def go_back(self):
        self.try_window = TryWindow()
        self.try_window.show()
        self.hide()

    def open_img(self):
        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap(QFileDialog.getOpenFileName(self, 'Выберете изображение', '')[0])
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.imgView.setScene(scene)

    def go_default(self):
        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap('res/App_logo-256.png')
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.imgView.setScene(scene)


class TryDBWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/TryDB_window.ui', self)  # Загружаем дизайн
        # настраеваем параметры окна
        self.setWindowIcon(QtGui.QIcon('res/App_logo-256.png'))
        self.setWindowTitle('Учебник PyQt')

        self.backBtn.clicked.connect(self.go_back)
        self.addBtn.clicked.connect(self.create_str)
        self.updBtn.clicked.connect(self.update_str)
        self.delBtn.clicked.connect(self.delete_str)

        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("res/db.db3")
        self.con.open()

        self.update_table()

    def go_back(self):
        self.try_window = TryWindow()
        self.try_window.show()
        self.hide()

    def create_str(self):
        self.con.exec_(f"""
        INSERT INTO class (name)
        VALUES ('{self.addInp.toPlainText()}');""")
        self.update_table()
        self.addInp.setText('')

    def update_str(self):
        self.con.exec_(f"""
        UPDATE class SET name='{self.updSndInp.toPlainText()}' WHERE name='{self.updFstInp.toPlainText()}'
        """)
        self.update_table()
        self.updFstInp.setText('')
        self.updSndInp.setText('')

    def delete_str(self):
        self.con.exec_(f"""
        DELETE FROM class
        WHERE name = '{self.delInp.toPlainText()}'""")
        self.update_table()
        self.delInp.setText('')

    def update_table(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["ФИО"])
        query = QSqlQuery("SELECT name FROM class")
        while query.next():
            rows = self.table.rowCount()
            self.table.setRowCount(rows + 1)
            self.table.setItem(rows, 0, PyQt5.QtWidgets.QTableWidgetItem(query.value(0)))
        self.table.resizeColumnsToContents()


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
