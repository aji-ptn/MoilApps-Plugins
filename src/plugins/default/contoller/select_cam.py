from ..ui_windows.OpenCam import Ui_Dialog
import cv2
from PyQt5 import QtWidgets


def check_port_camera():
    """Check the camera usb that available in computer

    return:
        will showing the port camera available
    """
    all_camera_idx_available = []
    for camera_idx in range(5):
        cap = cv2.VideoCapture(camera_idx)
        if cap.isOpened():
            all_camera_idx_available.append(camera_idx)
            cap.release()

    msgbox = QtWidgets.QMessageBox()
    msgbox.setWindowTitle("Camera Port Available")
    msgbox.setText(
        "Select the port camera from the number in list !! \n"
        "Available Port = " + str(all_camera_idx_available))
    msgbox.exec()


class OpenCameras(Ui_Dialog):
    def __init__(self, MainWindow, recentWindow):
        """
        This class is to control the window selecting camera.

        Args:
            MainWindow (): Is the parent class window. QtWidget of mainWindow UI
            recentWindow (): is the object of this recent window.
            it is QtDialog object inheritance from mainWindow class.
        """
        super(OpenCameras, self).__init__()
        self.parent_window = MainWindow
        self.recent_window = recentWindow
        self.setupUi(self.recent_window)
        self.videoStreamURL = None
        self.lineEdit_14.setText('http://192.168.100.226:8000/stream.mjpg')

        self.handle_activated_combobox()
        self.connect_to_button()

    def connect_to_button(self):
        """
        This is for connect the button or event with class function.

        Returns:
            None.
        """
        self.comboBox.activated.connect(self.handle_activated_combobox)
        self.buttonBox.accepted.connect(self.push_button_ok)
        self.buttonBox.rejected.connect(self.exit)
        self.detectPort.clicked.connect(check_port_camera)

    def handle_activated_combobox(self):
        """
        This function is to handle combo box to select source camera.

        Returns:
            if select USB Camera then it will hide the object UI for streaming camera.
            On the other hand, if you choose a streaming camera, it will hide the
            component object UI for the USB camera.
        """
        if self.comboBox.currentText() == 'USB Camera':
            self.label_59.hide()
            self.lineEdit_14.hide()
            self.framePortUsb.show()

        else:
            self.label_59.show()
            self.lineEdit_14.show()
            self.framePortUsb.hide()

    def video_source(self):
        """To select the video source want to use

        return:
            videoStreamURL
        """
        if self.comboBox.currentText() == 'USB Camera':
            self.videoStreamURL = int(self.portCamera.currentText())
        else:
            self.videoStreamURL = self.lineEdit_14.text()
        return self.videoStreamURL

    def push_button_ok(self):
        """
        To process the final decisions the open camera.

        return:
            Execute open camera function.
        """
        self.parent_window.cameraOpen()
        self.exit()

    def exit(self):
        """
        Exit open camera window when reject the choice

        return:
            close the window.
        """
        self.recent_window.close()
