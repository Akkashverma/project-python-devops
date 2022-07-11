from PyQt5.QtWidgets import QApplication, QLineEdit, QToolBar, QMainWindow, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys


class Web_browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 700)
        self.setWindowTitle("Web Browser")
        self.setWindowIcon(QIcon('icons/python.png'))

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.back_btn = QPushButton()
        self.back_btn.setIcon(QIcon('icons/back.png'))
        self.back_btn.setIconSize(QSize(36,36))
        self.back_btn.clicked.connect(self.b_btn)



        self.reload_btn= QPushButton()
        self.reload_btn.setIcon(QIcon('icons/reload.png'))
        self.reload_btn.setIconSize(QSize(36,36))
        self.reload_btn.clicked.connect(self.re_btn)



        self.forward_btn = QPushButton()
        self.forward_btn.setIcon(QIcon('icons/forward.png'))
        self.forward_btn.setIconSize(QSize(36,36))
        self.forward_btn.clicked.connect(self.f_btn)


        self.home_btn   = QPushButton()
        self.home_btn.setIcon(QIcon('icons/home.png'))
        self.home_btn.setIconSize(QSize(36,36))
        self.home_btn.clicked.connect(self.h_btn)


        self.lineedit = QLineEdit()
        self.setFont(QFont("Times", 12))
        self.lineedit.returnPressed.connect(self.sea_btn)

        self.search_btn = QPushButton()
        self.search_btn.setIcon(QIcon('icons/search.png'))
        self.search_btn.setIconSize(QSize(36,36))


        toolbar.addWidget(self.back_btn)
        toolbar.addWidget(self.reload_btn)
        toolbar.addWidget(self.forward_btn)
        toolbar.addWidget(self.home_btn)
        toolbar.addWidget(self.lineedit)
        toolbar.addWidget(self.search_btn)

        self.webengine = QWebEngineView()
        self.setCentralWidget(self.webengine)
        initialurl = 'https://www.google.com'
        self.lineedit.setText(initialurl)
        self.webengine.load(QUrl(initialurl))

    def b_btn(self):
        self.webengine.back()

    def f_btn(self):
        self.webengine.forward()

    def sea_btn(self):
        url = self.lineedit.text()
        self.webengine.load(QUrl(url))

    def h_btn(self):
        self.webengine.load(QUrl('https://www.google.com'))

    def re_btn(self):
        self.webengine.reload()








app = QApplication(sys.argv)
window = Web_browser()
window.show()
sys.exit(app.exec())
