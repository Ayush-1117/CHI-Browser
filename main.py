import sys

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.wolframalpha.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        navbar = QToolBar()
        self.addToolBar(navbar)

        code_explain = QAction('CODE EXPLAINER', self)
        code_explain.triggered.connect(self.explainer)
        navbar.addAction(code_explain)

        word_pdf = QAction('WORD 2 PDF', self)
        word_pdf.triggered.connect(self.open_converter)
        navbar.addAction(word_pdf)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.wolframalpha.com/'))

    def open_converter(self):
        self.browser.setUrl(QUrl('https://www.ilovepdf.com/word_to_pdf'))

    def explainer(self):
        self.browser.setUrl(QUrl('https://denigma.app/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Chi Browser')
window = MainWindow()
app.exec_()