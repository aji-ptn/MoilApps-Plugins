import os
from PyQt5 import QtWidgets
from .ThreadAxisAPI import ThreadAxisAPI


def getPassword():
    passwd, ok = QtWidgets.QInputDialog.getText(
        None, "Authentication", "Sudo Password?", QtWidgets.QLineEdit.Password)
    if ok and passwd != '':
        return passwd


class AxisController(object):
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.position = 0
        self.speed = 500
        self.threadAxisAPI = None
        self.connect_button()

    def connect_button(self):
        self.parent.ui.btn_ctrl_axis.clicked.connect(self.open_axis_controller)
        self.parent.ui.help_axis.clicked.connect(self.help_axis_controller)
        self.parent.ui.btn_connect.clicked.connect(self.go_connect_serial)
        self.parent.ui.btn_disconnect.clicked.connect(self.go_disconnect_serial)
        self.parent.ui.btn_reset.clicked.connect(self.go_reset)
        self.parent.ui.run_abs.clicked.connect(self.go_absolute_moving)

    def go_show_position(self):
        self.threadAxisAPI.show_position()

    def open_axis_controller(self):
        if self.parent.axis_controller is False:
            self.parent.ui.frame_axis.show()
            self.parent.axis_controller = True
        else:
            self.parent.ui.frame_axis.hide()
            self.parent.axis_controller = False

    def go_connect_serial(self):
        passwd = getPassword()
        if passwd:
            os.system("echo " + passwd + "| sudo -S chmod a+rw /dev/ttyUSB*")
            self.threadAxisAPI = ThreadAxisAPI(serial_port="/dev/ttyUSB0")
            self.threadAxisAPI.connect_serial()

    def go_disconnect_serial(self):
        self.threadAxisAPI.disconnect_serial()

    def go_reset(self):
        self.position = 0
        self.speed = 500
        self.threadAxisAPI.reset()
        # self.Ui.lineEdit_position.setText(" 0 ")
        # self.Ui.lineEdit_speed.setText(str(self.speed))

    def go_absolute_moving(self):
        position = self.parent.ui.absolute_val.text()
        self.threadAxisAPI.absolute_moving(position)
        self.go_show_position()

    def go_axis_init(self):
        self.threadAxisAPI.axis_init()

    def go_related_moving(self):
        # self.position = self.Ui.lineEdit_position.text()
        self.threadAxisAPI.related_moving(self.position)

    def go_default_speed(self):
        self.threadAxisAPI.default_speed()

    def go_set_speed(self):
        # self.speed = self.Ui.lineEdit_speed.text()
        self.threadAxisAPI.set_speed(self.speed)

    def help_axis_controller(self):
        QtWidgets.QMessageBox.about(
            self.parent, "Help", "Please Contact MOIL LAB")
