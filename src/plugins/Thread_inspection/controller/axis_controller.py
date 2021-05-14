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
        self.parent.ui.btn_disconnect.clicked.connect(
            self.go_disconnect_serial)
        self.parent.ui.btn_reset.clicked.connect(self.go_reset)
        self.parent.ui.run_abs.clicked.connect(self.go_absolute_moving)
        self.parent.ui.prev.clicked.connect(self.reduce_speed)
        self.parent.ui.next.clicked.connect(self.increase_speed)
        self.parent.ui.prev_speed.clicked.connect(
            self.go_related_moving_backward)
        self.parent.ui.next_speed.clicked.connect(
            self.go_related_moving_forward)

    def open_axis_controller(self):
        if self.parent.axis_controller is False:
            self.parent.ui.frame_axis.show()
            self.parent.axis_controller = True
        else:
            self.parent.ui.frame_axis.hide()
            self.parent.axis_controller = False

    def reduce_speed(self):
        if self.threadAxisAPI:
            if self.speed == 200:
                pass
            else:
                self.speed -= 100
            self.parent.ui.lineEdit_4.setText(str(self.speed))
            self.threadAxisAPI.set_speed(self.speed)

    def increase_speed(self):
        if self.threadAxisAPI:
            if self.speed == 800:
                pass
            else:
                self.speed += 100
            self.parent.ui.lineEdit_4.setText(str(self.speed))
            self.threadAxisAPI.set_speed(self.speed)

    def go_connect_serial(self):
        passwd = getPassword()
        if passwd:
            os.system("echo " + passwd + "| sudo -S chmod a+rw /dev/ttyUSB*")
            try:
                self.threadAxisAPI = ThreadAxisAPI()
                self.threadAxisAPI.connect_serial(serial_port="/dev/ttyUSB0")
                QtWidgets.QMessageBox.information(
                    None, "Info !!", "Serial port connected!!")
            except OSError as err:
                self.threadAxisAPI.logger.error(err)
                QtWidgets.QMessageBox.warning(
                    None,
                    "Error",
                    "Make sure you have connect the serial port to the computer\nOr typing the correct "
                    "password!!\n\nError: " +
                    str(err))

    def go_disconnect_serial(self):
        if self.threadAxisAPI:
            self.threadAxisAPI.disconnect_serial()
            QtWidgets.QMessageBox.information(
                None, "Info !!", "Serial port Disconnected!!")

    def go_reset(self):
        if self.threadAxisAPI:
            self.position = 0
            self.speed = 500
            self.threadAxisAPI.reset()
            self.parent.ui.label_curent_axis.setText("0 mm")
            self.parent.ui.lineEdit_4.setText(str(self.speed))
            QtWidgets.QMessageBox.information(
                None, "Info !!", "Serial configuration has been reset!!")

    def go_absolute_moving(self):
        if self.threadAxisAPI:
            position = self.parent.ui.absolute_val.text()
            self.threadAxisAPI.absolute_moving(position)

    def go_axis_init(self):
        self.threadAxisAPI.axis_init()

    def go_related_moving_forward(self):
        if self.threadAxisAPI:
            self.position = 20
            self.threadAxisAPI.related_moving(self.position)

    def go_related_moving_backward(self):
        if self.threadAxisAPI:
            self.position = - 20
            self.threadAxisAPI.related_moving(self.position)

    def go_default_speed(self):
        self.threadAxisAPI.default_speed()

    def help_axis_controller(self):
        QtWidgets.QMessageBox.about(
            self.parent, "Help", "Please Contact MOIL LAB")
