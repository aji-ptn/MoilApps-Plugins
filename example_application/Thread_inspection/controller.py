from View.Ui_MainWindow import *
from Model.utils_function import select_file, read_image
from View.show_image import Show_Image
from Model.anypoint_view import Anypoint_View
from Model.video_controller import Video_Controller
from open_camera import OpenCameraController
import cv2
from Moildevs import Moildevs


class Controller(QtWidgets.QMainWindow):
    """This is class that control the main window of user interface
    """

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
        self.width_original_image = 300
        self.width_result_image = 1200
        self.connect_event()

        self.openCam = QtWidgets.QDialog()
        self.winOpenCam = OpenCameraController(self, self.openCam)

        self.show_image = Show_Image(self)
        self.video_controller = Video_Controller(self)
        self.anypoint = Anypoint_View(self)

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

    def onclick_open_image(self):
        """Open Dialog to search the file image on local directory.
        """
        filename = select_file("Select Image", "../", "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if filename:
            param_name = select_file("Select Parameter", "../", "Parameter Files (*.json)")
            if param_name:
                self.moildev = Moildevs(param_name)
                self.image = read_image(filename)
                self.show_image.show_result_image(self.image, self.width_result_image)
                self.show_image.show_original_image(self.image, self.width_original_image)

    def onclick_load_video(self):
        """Open Dialog to search video file on local Directory.
        """
        video_source = select_file("Select Video Files", "../", "Video Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if video_source:
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
        self.running_video(camera_source)

    def running_video(self, video_source):
        """Open Video following the source given.
        """
        self.cap = cv2.VideoCapture(video_source)
        self.next_frame_slot()

    def next_frame_slot(self):
        """Control video frame.
        """
        _, image = self.cap.read()
        if image is None:
            QtWidgets.QMessageBox.information(self, "Information", "No source camera founded")
        else:
            self.h, self.w = image.shape[:2]
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
            self.show_image.show_result_image(image, self.width_result_image)
            self.show_image.show_original_image(image, self.width_original_image)

    def mouse_wheelEvent(self, e):
        """Resize image using mouse wheel event.
        """
        if self.image is None:
            pass
        else:
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
                self.show_image.show_result_image(self.image, self.width_result_image)

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def go_to_home_application(self):
        """This function is for close the main window and show the home application
        to chose another application
        - self : represent the current user interface
        - self parent : represent the home window to select the application
        """
        # self.parent.show()
        # self.hide()
        self.close()

    def help(self):
        """showing the message box to show help information obout this application
        """
        self.openCam.close()
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help !!")
        msgbox.setText("Moildev-Apps\n\n"
                       "Moildev-Apps is software to process fisheye "
                       "image with the result panorama view and Anypoint"
                       " view. \n\nThe panoramic view may present a horizontal"
                       "view in a specific immersed environment to meet the"
                       "common human visual perception, while the Anypoint"
                       "view is an image that has been undistorted in a certain"
                       "area according to the input coordinates."
                       "\n\nMore reference about Moildev, contact us\n\n")
        msgbox.setIconPixmap(QtGui.QPixmap('./assets/128.png'))
        msgbox.exec()

    def onclick_exit(self):
        self.close()
        # self.parent.close()
        self.openCam.close()

    def closeEvent(self, event):
        """Control exit application by ask yes or no question.
        """
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                               "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.onclick_exit()
            event.accept()
        else:
            event.ignore()
