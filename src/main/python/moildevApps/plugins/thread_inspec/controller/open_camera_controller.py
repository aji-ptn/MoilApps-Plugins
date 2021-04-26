from ..view.Ui_Select_source_Camera import *
import cv2


class OpenCameraController(Ui_Dialog):
    """Create class controller open camera with inheritance from Ui Dialog Class
    """
    def __init__(self, MainWindow, RecentWindow):
        super(OpenCameraController, self).__init__()
        self.parent_win = MainWindow
        self.recent_win = RecentWindow
        self.setupUi(self.recent_win)
        self.camera_source = None
        self.camera_stream_link.setText('http://192.168.100.226:8000/stream.mjpg')
        self.handle_activated_comboBox()
        self.connect_event()

    def connect_event(self):
        self.comboBox.activated.connect(self.handle_activated_comboBox)
        self.detectPort.clicked.connect(self.check_Port_USB_Camera)
        self.buttonBox.accepted.connect(self.onclick_comboBox_oke)
        self.buttonBox.rejected.connect(self.onclick_comboBox_cancel)

    def handle_activated_comboBox(self):
        """Handle the selection from comboBox of source camera
        """
        if self.comboBox.currentText() == "USB Camera":
            self.label_59.hide()
            self.camera_stream_link.hide()
            self.framePortUsb.show()

        else:
            self.label_59.show()
            self.camera_stream_link.show()
            self.framePortUsb.hide()

    def check_Port_USB_Camera(self):
        """Detect the USB camera port available and show it on message box prompt
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

    def camera_source_used(self):
        """This function will return the source of camera used depend on what the camera use
        return: camera source
        """
        if self.comboBox.currentText() == "USB Camera":
            self.camera_source = int(self.portCamera.currentText())
        else:
            self.camera_source = self.camera_stream_link.text()
        if self.camera_source is None:
            return None
        else:
            return self.camera_source

    def onclick_comboBox_oke(self):
        """Open the camera following the parent function and close the dialog window
        """
        self.parent_win.open_camera()
        self.recent_win.close()

    def onclick_comboBox_cancel(self):
        """close the window when you click the buttonBox cancel
        """
        self.recent_win.close()
