from PyQt5 import QtWidgets
from ..view.Ui_Mainwindow import *


class Controller(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.old = parent
        self.ui.pushButton.clicked.connect(self.home)

    def home(self):
        self.old.show()
        self.close()