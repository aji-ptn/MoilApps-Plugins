import datetime
import cv2
from Moildev import Moildev
from Moildev import read_image

from .ui_windows.Ui_Mainwindow import *
from .contoller.select_cam import OpenCameras
from .contoller.videocontroller import VideoController
from .contoller.showResult import ShowImageResult
from .contoller.control_window import ViewWindow
from .contoller.addition import select_file
from .view_image.anypoint import AnyPoint
from .view_image.panorama import Panorama


class Controller(QtWidgets.QMainWindow):
    def __init__(self, MainWindow):
        """
        The controller class to control UI MainWindow.

        Args:
            MainWindow (): Its object window from parent application(argument from main apps)
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent = MainWindow
        self.ui.frame_4.hide()
        self.ui.frame_5.hide()
        self.ui.frame.hide()
        self.ui.labelRecenter.hide()
        self.ui.labelImagerecenter.hide()
        self.moildev = None
        self.image = None
        self.coordinate_point = None
        self.revImage = None
        self.resultImage = None
        self.cap = None
        self.dir_save = None
        self.anypointState = 1
        self.angle = 0
        self.alpha = 0
        self.beta = 0
        self.zoom = 4
        self.width_img = 1400
        self.connect_button()

        self.showing = ShowImageResult(self)
        self.view = ViewWindow(self)
        self.videoControl = VideoController(self)
        self.videoControl.videoButtonDisable()
        self.anypoint = AnyPoint(self)
        self.panorama = Panorama(self)
        self.dialogOpenCam = QtWidgets.QDialog()
        self.winOpenCam = OpenCameras(self, self.dialogOpenCam)

    def connect_button(self):
        """
        Connect the button and event to the function.

        Returns:
            --
        """
        self.ui.actionLoad_video.triggered.connect(self.open_video_file)
        self.ui.actionLoad_Image.triggered.connect(self.open_image)
        self.ui.actionOpen_Cam.triggered.connect(self.onclick_open_camera)
        self.ui.actionAbout_Us.triggered.connect(self.aboutUs)
        self.ui.windowOri.mousePressEvent = self.mouse_event
        self.ui.windowOri.mouseMoveEvent = self.mouseMovedOriImage
        self.ui.windowOri.wheelEvent = self.mouse_wheelEvent
        self.ui.windowOri.mouseReleaseEvent = self.mouse_release_event
        self.ui.PlussIcon.mouseReleaseEvent = self.mouse_release_event
        self.ui.PlussIcon.mouseDoubleClickEvent = self.mouseDoubleclick_event
        self.ui.PlussIcon.wheelEvent = self.mouse_wheelEvent
        self.ui.PlussIcon.mouseMoveEvent = self.mouseMovedResultImage
        self.ui.closeEvent = self.closeEvent
        self.ui.backtoHome.triggered.connect(self.back_to_home)
        self.ui.actionHelp.triggered.connect(self.help)
        self.ui.actionExit.triggered.connect(self.exit)

    def open_image(self):
        """
        Load image from directory using file open dialog.

        Returns:
            Image.
        """
        file_image = select_file(
            "Select Image",
            "../",
            "Image Files (*.jpeg *.jpg *.png *.gif *.bmg)")
        if file_image:
            file_param = select_file(
                "Select Parameter",
                "../",
                "Parameter Files (*.json)")
            if file_param:
                self.ui.btn_Anypoint.setChecked(False)
                self.ui.btn_Panorama.setChecked(False)
                self.image = read_image(file_image)
                self.h, self.w = self.image.shape[:2]
                self.moildev = Moildev(file_param)
                self.showing.view_result(self.image)
                self.center = self.getCenterWindowsOri()
                self.cam = False
                self.anypoint.resetAlphaBeta()

    def open_video_file(self):
        """
        Load video file from local directory using file open dialog.

        Returns:
            Video.
        """
        file_video = select_file(
            "Select Video Files",
            "../",
            "Image Files (*.mp4 *.avi *.mpg *.gif *.mov)")
        if file_video:
            file_param = select_file(
                "Select Parameter",
                "../",
                "Parameter Files (*.json)")
            if file_param:
                self.anypoint.resetAlphaBeta()
                self.videoControl.videoButtonEnable()
                self.coordinate_point = None
                self.moildev = Moildev(file_param)
                self.cap = cv2.VideoCapture(file_video)
                _, image = self.cap.read()
                if image is None:
                    QtWidgets.QMessageBox.information(
                        self, "Information", "No source camera founded")
                else:
                    self.cam = True
                    self.next_frame_slot()

    def onclick_open_camera(self):
        """
        Showing the window to select the source camera.

        Returns:
            None.
        """
        self.dialogOpenCam.show()

    def cameraOpen(self):
        """
        Open camera following the source given. the source has 2 choice which is usb camera and url camera
        raspberry pi. we have to running the server on raspberry to use the url camera.

        Returns:
            Camera open.
        """
        video_source = self.winOpenCam.video_source()
        if video_source is None:
            pass
        else:
            self.cap = cv2.VideoCapture(video_source)
            self.coordinate_point = None
            _, image = self.cap.read()
            if image is None:
                QtWidgets.QMessageBox.information(
                    self, "Information", "No source camera founded")
            else:
                QtWidgets.QMessageBox.information(
                    self, "Information", "Select Parameter Camera !!")
                file_name = select_file(
                    "Select Left Parameter", "../", "Parameter Files (*.json)")
                if file_name:
                    self.moildev = Moildev(file_name)
                    self.videoControl.videoButtonCamera()
                    self.cam = True
                    self.next_frame_slot()
                else:
                    self.cap.release()

    def next_frame_slot(self):
        """
        Control video frame, Its will Lopping the frame following the timer.

        Returns:
            None
        """
        _, self.image = self.cap.read()
        self.oriImage = self.image.copy()
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
        self.videoControl.controller()
        self.center = self.getCenterWindowsOri()
        image = self.image.copy()
        self.showing.view_result(image)
        if self.videoControl.record:
            if self.ui.btn_Anypoint.isChecked() or self.ui.btn_Panorama.isChecked():
                self.videoControl.video_writer.write(
                    self.showing.resultImage)
            else:
                self.videoControl.video_writer.write(self.image)

    def init_ori_ratio(self):
        """
        Calculate the initial ratio of the image.

        Returns:
            ratio_x : ratio width between image and ui window.
            ratio_y : ratio height between image and ui window.
            center : find the center image on window user interface.
        """
        h = self.ui.windowOri.height()
        w = self.ui.windowOri.width()
        height, width = self.image.shape[:2]
        ratio_x = width / w
        ratio_y = height / h
        return ratio_x, ratio_y

    def getCenterWindowsOri(self):
        """
        Get the center coordinate on label windows original.

        Returns:
            center coordinate
        """
        h = self.ui.windowOri.height()
        w = self.ui.windowOri.width()
        ratio_x, ratio_y = self.init_ori_ratio()
        center = (round((w / 2) * ratio_x), round((h / 2) * ratio_y))
        return center

    def mouse_event(self, e):
        """
        Specify coordinate from mouse left event to generate anypoint view and recenter image.

        Args:
            e (): Coordinate point return by pyqt core

        Returns:

        """
        if self.image is None:
            pass
        else:
            if e.button() == QtCore.Qt.LeftButton:
                pos_x = round(e.x())
                pos_y = round(e.y())
                ratio_x, ratio_y = self.init_ori_ratio()
                self.coorX = round(pos_x * ratio_x)
                self.coorY = round(pos_y * ratio_y)
                if self.ui.btn_Anypoint.isChecked():
                    self.alpha, self.beta = self.moildev.get_alpha_beta(
                        self.coorX, self.coorY, self.anypointState)
                    self.anypoint.anypoint_view()
                elif self.ui.checkBox_ShowRecenterImage.isChecked():
                    self.alpha, self.beta = self.moildev.get_alpha_beta(
                        self.coorX, self.coorY, 1)
                    self.panorama.recenterImage()
                else:
                    print("coming soon")

    def mouseDoubleclick_event(self, e):
        """
        Reset to default by mouse event.

        Args:
            e ():

        Returns:

        """
        self.anypoint.resetAlphaBeta()
        if self.ui.btn_Anypoint.isChecked():
            self.anypoint.anypoint_view()
        elif self.ui.btn_Panorama.isChecked():
            self.panorama.resetCenter()
            self.panorama.recenterImage()
        else:
            pass

    def mouse_wheelEvent(self, e):
        """
        Resize image using mouse wheel event.

        Args:
            e ():

        Returns:

        """
        if self.image is None:
            pass
        else:
            modifiers = QtWidgets.QApplication.keyboardModifiers()
            if modifiers == QtCore.Qt.ControlModifier:
                wheelcounter = e.angleDelta()
                if wheelcounter.y() / 120 == -1:
                    if self.width_img == 1100:
                        pass
                    else:
                        self.width_img -= 100

                if wheelcounter.y() / 120 == 1:
                    if self.width_img == 4000:
                        pass
                    else:
                        self.width_img += 100
                self.showing.view_result(self.image)

    def mouseMovedOriImage(self, e):
        """
        Mouse move event to look in surrounding view in result label image.

        Args:
            e ():

        Returns:

        """
        pos_x = round(e.x())
        pos_y = round(e.y())
        ratio_x, ratio_y = self.init_ori_ratio()
        self.coorX = round(pos_x * ratio_x)
        self.coorY = round(pos_y * ratio_y)
        self.coordinate_point = (self.coorX, self.coorY)
        if self.ui.btn_Anypoint.isChecked():
            self.alpha, self.beta = self.moildev.get_alpha_beta(
                self.coorX, self.coorY, self.anypointState)
            self.anypoint.anypoint_view()

    def mouseMovedResultImage(self, e):
        """
        Mouse move event to look in surrounding view in original label image.

        Args:
            e ():

        Returns:

        """
        pos_x = round(e.x())
        pos_y = round(e.y())
        h = self.ui.PlussIcon.height()
        w = self.ui.PlussIcon.width()
        ratio_x = self.w / w
        ratio_y = self.h / h
        delta_x = round(pos_x * ratio_x)
        delta_y = round(pos_y * ratio_y)
        self.coordinate_point = (
            round(
                pos_x *
                ratio_x),
            round(
                pos_y *
                ratio_y))
        self.coorX = round(pos_x * ratio_x)
        self.coorY = round(pos_y * ratio_y)
        if self.ui.btn_Anypoint.isChecked():
            self.alpha, self.beta = self.moildev.get_alpha_beta(
                delta_x, delta_y, self.anypointState)
            self.anypoint.anypoint_view()

    def mouse_release_event(self, e):
        """
        Mouse release event right click to show menu. the menu can select is show maximum, show minimum,
        save image, and show info.

        Args:
            e ():

        Returns:
            None.
        """
        if e.button() == QtCore.Qt.LeftButton:
            pass
        else:
            if self.image is None:
                pass
            else:
                self.menuMouseEvent(e)

    def menuMouseEvent(self, e):
        """
        showing the menu image when release right click.

        Args:
            e ():

        Returns:
            None.
        """
        menu = QtWidgets.QMenu()
        maxi = menu.addAction("Show Maximized")
        maxi.triggered.connect(self.view.showMaximized)
        mini = menu.addAction("Show Minimized")
        mini.triggered.connect(self.view.show_Minimized)
        save = menu.addAction("Save Image")
        info = menu.addAction("Show Info")
        save.triggered.connect(self.saveImage)
        info.triggered.connect(self.help)
        menu.exec_(e.globalPos())

    def saveImage(self):
        """
        Save image on local directory. the first time you save image, it will open dialog to select the directory,
        then the image saved will always stored on directory selected.

        Returns:
            None.
        """
        ss = datetime.datetime.now().strftime("%m_%d_%H_%M_%S")
        name_image = "Original"
        image = self.image
        if self.ui.btn_Panorama.isChecked() or self.ui.btn_Anypoint.isChecked():
            name_image = "result"
            image = self.resultImage
        if self.dir_save is None or self.dir_save == "":
            self.selectDir()
        else:
            name = self.dir_save + "/" + name_image + "_" + str(ss) + ".png"
            cv2.imwrite(name, image)
            QtWidgets.QMessageBox.information(
                self, "Information", "Image saved !!\n\nLoc @: " + self.dir_save)

    def selectDir(self):
        """
        Select directory to save image. This function create to make it not always ask the directory by open dialog,
        after directory save not None, it will pass open dialog prompt.

        Returns:
            None.
        """
        self.dir_save = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Save Folder')
        if self.dir_save:
            self.saveImage()

    def aboutUs(self):
        """
        Showing prompt About us information (MOIL LAB).

        Returns:
            None.
        """
        self.dialogOpenCam.close()
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("About Us")
        msgbox.setText(
            "MOIL \n\nOmnidirectional Imaging & Surveillance Lab\nMing Chi University of Technology\n")
        msgbox.setIconPixmap(QtGui.QPixmap('./images/moildev2.png'))
        msgbox.exec()

    def help(self):
        """
        showing the message box to show help information obout this application.

        Returns:
            None.
        """
        self.dialogOpenCam.close()
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
        msgbox.setIconPixmap(QtGui.QPixmap('./images/moildev.png'))
        msgbox.exec()

    def back_to_home(self):
        """
        This function is for back to main windows, because we just hide the main window so it possible to show
        the main window following the event given.

        Returns:
            None.
        """
        self.parent.show()
        self.hide()

    def exit(self):
        """
        Exit the apps with showing the QMessageBox.

        Returns:
            None.
        """
        self.dialogOpenCam.close()
        self.close()

    def closeEvent(self, event):
        """
        Control exit application by ask yes or no question.

        Args:
            event ():when you click the icon (x) or exit button

        Returns:
            destroy the window.
        """
        reply = QtWidgets.QMessageBox.question(
            self,
            'Message',
            "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.exit()
            event.accept()
        else:
            event.ignore()
