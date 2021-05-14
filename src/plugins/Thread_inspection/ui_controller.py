import cv2
import numpy as np
from Moildev import Moildev
from Moildev import read_image, draw_polygon

from .ui_windows.Ui_MainWindow import *
from .view_image.anypoint import AnypointView
from .view_image.panorama import PanoramaView
from .controller.video_controller import VideoController
from .controller.open_camera import OpenCameraController
from .controller.help import open_help_moildev
from .controller.show_result import ShowImage
from .controller.axis_controller import AxisController
from .controller.addition import select_file


class Controller(QtWidgets.QMainWindow):
    """This is class that control the main window of user interface
    """
    resized = QtCore.pyqtSignal()

    def __init__(self, main_application):
        """Constructor method:
        - create instance from user interface class
        - connect event to the function
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent = main_application
        self.image = None
        self.cap = None
        self.cam = False
        self.normal_mode = True
        self.panorama_mode = False
        self.axis_controller = False
        self.mapX = None
        self.mapY = None
        self.mapX_pano = None
        self.mapY_pano = None
        self.moildev = None

        self.resized.connect(self.set_place_frame_parameter)
        self.result_image = None
        self.width_original_image = 300
        self.width_result_image = 1400
        self.angle = 0
        self.connect_event()

        self.openCam = QtWidgets.QDialog()
        self.winOpenCam = OpenCameraController(self, self.openCam)

        self.show_image = ShowImage(self)
        self.video_controller = VideoController(self)
        self.anypoint = AnypointView(self)
        self.panorama = PanoramaView(self)
        self.axis_control = AxisController(self)

        self.video_controller.set_button_disable()
        self.ui.frame_panorama.hide()
        self.ui.frame_navigator.hide()
        self.ui.frame_axis.hide()

    def set_place_frame_parameter(self):
        """
        To set the place of parameter anypoint or panorama following the size of label.

        Returns:

        """
        pos_x = self.ui.scrollArea.width()
        self.ui.frame_navigator.setGeometry(
            QtCore.QRect(pos_x - 180, 10, 160, 290))
        self.ui.frame_panorama.setGeometry(
            QtCore.QRect(pos_x - 220, 10, 210, 80))

    def connect_event(self):
        """Connect every event on user interface like button event, mouse event
        and etc to the function processing
        """
        self.ui.btn_Open_Image.clicked.connect(self.onclick_open_image)
        self.ui.btn_Home.clicked.connect(self.go_to_home_application)
        self.ui.btn_Open_Cam.clicked.connect(self.onclick_open_camera_button)
        self.ui.btn_Open_Video.clicked.connect(self.onclick_load_video)
        self.ui.btn_Quit.clicked.connect(self.onclick_exit)
        self.ui.actionExit.triggered.connect(self.onclick_exit)
        self.ui.btn_show_help.clicked.connect(self.help)
        self.ui.label_Result_Image.wheelEvent = self.mouse_wheelEvent

        self.ui.pushButton_29.clicked.connect(open_help_moildev)
        self.ui.btn_Rotate_Left.clicked.connect(self.rotate_left)
        self.ui.btn_Rotate_Right.clicked.connect(self.rotate_right)
        self.ui.btn_Zoom_in.clicked.connect(self.zoom_in)
        self.ui.btn_Zoom_out.clicked.connect(self.zoom_out)
        self.ui.btn_normal.clicked.connect(self.show_normal)

    def onclick_open_image(self):
        """Open Dialog to search the file image on local directory.
        """
        filename = select_file(
            "Select Image",
            "../",
            "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            param_name = select_file(
                "Select Parameter", "../", "Parameter Files (*.json)")
            if param_name:
                self.moildev = Moildev(param_name)
                self.image = read_image(filename)
                self.h, self.w = self.image.shape[:2]
                self.show_to_window()

    def onclick_load_video(self):
        """Open Dialog to search video file on local Directory.
        """
        video_source = select_file(
            "Select Video Files",
            "../",
            "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
            param_name = select_file(
                "Select Parameter", "../", "Parameter Files (*.json)")
            if param_name:
                self.moildev = Moildev(param_name)
                self.running_video(video_source)

    def onclick_open_camera_button(self):
        """Show the window of selection camera source.
        """
        self.openCam.show()

    def open_camera(self):
        """Select the camera from the available source in the system,
        this function provide 2 source namely USB cam and Streaming Cam from Raspberry pi.
        """
        camera_source = self.winOpenCam.camera_source_used()
        if camera_source:
            param_name = select_file(
                "Select Parameter", "../", "Parameter Files (*.json)")
            if param_name:
                self.moildev = Moildev(param_name)
                self.running_video(camera_source)
                self.cam = True

    def running_video(self, video_source):
        """Open Video following the source given.
        """
        self.video_controller.set_button_enable()
        self.cap = cv2.VideoCapture(video_source)
        self.next_frame_slot()

    def next_frame_slot(self):
        """Control video frame.
        """
        _, self.image = self.cap.read()
        if self.image is None:
            QtWidgets.QMessageBox.information(
                self, "Information", "No source camera founded")
        else:
            self.h, self.w = self.image.shape[:2]
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.pos_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
            self.pos_msec = self.cap.get(cv2.CAP_PROP_POS_MSEC)
            self.frame_count = float(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration_sec = int(self.frame_count / self.fps)
            self.minutes = duration_sec // 60
            duration_sec %= 60
            self.seconds = duration_sec
            sec_pos = int(self.pos_frame / self.fps)
            self.minute = int(sec_pos // 60)
            sec_pos %= 60
            self.sec = sec_pos
            self.show_to_window()

    def mouse_wheelEvent(self, e):
        """Resize image using mouse wheel event.
        """
        if self.image is not None:
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == QtCore.Qt.ControlModifier:
                wheel_counter = e.angleDelta()
                if wheel_counter.y() / 120 == -1:
                    if self.width_result_image == 1000:
                        pass
                    else:
                        self.width_result_image -= 100

                if wheel_counter.y() / 120 == 1:
                    if self.width_result_image == 4000:
                        pass
                    else:
                        self.width_result_image += 100
                self.show_to_window()

    def zoom_in(self):
        if self.image is not None:
            if self.width_result_image == 4000:
                pass
            else:
                self.width_result_image += 100
            self.show_to_window()

    def zoom_out(self):
        if self.image is not None:
            if self.width_result_image == 1000:
                pass
            else:
                self.width_result_image -= 100
            self.show_to_window()

    def rotate_left(self):
        if self.image is not None:
            if self.angle == 180:
                pass
            else:
                self.angle += 10
            self.show_to_window()

    def rotate_right(self):
        if self.image is not None:
            if self.angle == 180:
                pass
            else:
                self.angle -= 10
            self.show_to_window()

    def show_normal(self):
        """
        Function for show the original image frame in window.

        Returns:

        """
        if self.image is not None:
            self.show_image.show_original_image(
                self.image, self.width_original_image)
            self.show_image.show_result_image(
                self.image, self.width_result_image, self.angle)
            self.normal_mode = True
            self.ui.frame_navigator.hide()
            self.ui.frame_panorama.hide()

    def show_to_window(self):
        """
        show image frame to windows user interface.
        Returns:

        """
        if self.normal_mode:
            self.show_image.show_original_image(
                self.image, self.width_original_image)
            self.show_image.show_result_image(
                self.image, self.width_result_image, self.angle)

        else:
            if self.panorama_mode:
                image = draw_polygon(
                    self.image.copy(),
                    self.mapX_pano,
                    self.mapY_pano)
                mapX = np.load(
                    './plugins/Thread_inspection/view_image/maps_pano/mapX.npy')
                mapY = np.load(
                    './plugins/Thread_inspection/view_image/maps_pano/mapY.npy')
                rho = self.panorama.rho

                self.result_image = cv2.remap(
                    self.image,
                    mapX,
                    mapY,
                    cv2.INTER_CUBIC)
                self.result_image = self.result_image[round(
                    rho + round(self.moildev.getRhoFromAlpha(30))):self.h, 0:self.w]
                # print(self.width_result_image)
            else:
                image = draw_polygon(self.image.copy(), self.mapX, self.mapY)
                self.result_image = cv2.remap(
                    self.image,
                    self.mapX,
                    self.mapY,
                    cv2.INTER_CUBIC)
            self.show_image.show_original_image(
                image, self.width_original_image)
            self.show_image.show_result_image(
                self.result_image, self.width_result_image, self.angle)

    def go_to_home_application(self):
        """This function is for close the main window and show the home application
        to chose another application
        - self : represent the current user interface
        - self parent : represent the home window to select the application
        """
        self.parent.show()
        self.hide()

    def help(self):
        """showing the message box to show help information obout this application
        """
        self.openCam.close()
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help !!")
        msgbox.setText(
            "Moildev-Apps\n\n"
            "Moildev-Apps is software to process fisheye "
            "image with the result panorama view and Anypoint"
            " view. \n\nThe panoramic view may present a horizontal"
            "view in a specific immersed environment to meet the"
            "common human visual perception, while the Anypoint"
            "view is an image that has been undistorted in a certain"
            "area according to the input coordinates."
            "\n\nMore reference about Moildev, contact us\n\n")
        msgbox.setIconPixmap(QtGui.QPixmap('images/moildev.png'))
        msgbox.exec()

    def onclick_exit(self):
        self.close()
        self.openCam.close()

    def resizeEvent(self, event):
        self.resized.emit()

    def closeEvent(self, event):
        """Control exit application by ask yes or no question.
        """
        reply = QtWidgets.QMessageBox.question(
            self,
            'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.onclick_exit()
            event.accept()
        else:
            event.ignore()
