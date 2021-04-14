from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import cv2
import os


class Video_Controller(object):
    def __init__(self, MainWindow):
        """This is the video controller methode that has function to control the video player button
        like play, pause skip, prev and etc. This class need include parent class to access the attribute.
        MainWindow is the parent class.
        """
        self.parent = MainWindow
        self.play = False
        self.record = False
        self.videoDir = None
        self.connect_event()

    def connect_event(self):
        self.parent.ui.btn_play_pouse.clicked.connect(self.onclick_play_pause_button)
        self.parent.ui.btn_stop_video.clicked.connect(self.stop_video)
        self.parent.ui.btn_prev_video.clicked.connect(self.prev_video)
        self.parent.ui.btn_skip_video.clicked.connect(self.skip_video)

    def set_button_disable(self):
        """Disable video control button when the application not using camera or video mode
        """
        self.parent.ui.btn_play_pouse.setDisabled(True)

    def set_button_enable(self):
        """Enable video control button when application using camera or video mode
        """
        self.parent.ui.btn_play_pouse.setEnabled(True)

    def control_camera_mode(self):
        """Control the widget when on camera mode
        ex: time slider will disabled"""
        pass

    def onclick_play_pause_button(self):
        """Control the play and pause video controller button
        for example, if play is true: it will change the icon button
        """
        if self.play:
            self.timer.stop()
            self.parent.ui.btn_play_pouse.setIcon(QtGui.QIcon("images/play.png"))
            self.play = False

        else:
            self.parent.ui.btn_play_pouse.setIcon(QtGui.QIcon("images/pause.png"))
            self.play_video()
            self.play = True

    def play_video(self):
        """Play video by connect to timer function
        """
        if self.parent.cap.isOpened():
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.parent.next_frame_slot)
            self.timer.start(1000. / self.parent.fps)
        else:
            pass

    def stop_video(self):
        """Stop video and set the time as a beginning, including the slider time
        """
        self.play = False
        self.parent.ui.btn_play_pouse.setIcon(QtGui.QIcon("images/play.png"))
        if self.parent.cap.isOpened():
            self.timer.stop()
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.parent.next_frame_slot()
            self.reset_label_time()
        else:
            pass

    def reset_label_time(self):
        """Reset the time when open the new video.
        """
        current = self.parent.ui.label_time_recent
        current.setAlignment(QtCore.Qt.AlignCenter)
        current.setText("00:00")

        current_1 = self.parent.ui.label_time_end
        current_1.setAlignment(QtCore.Qt.AlignCenter)
        current_1.setText("00:00")

    def prev_video(self):
        """Previous video is 5 seconds.
        """
        if self.parent.cap.isOpened():
            position = self.parent.pos_frame - 5 * self.parent.fps
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.parent.next_frame_slot()
        else:
            pass

    def skip_video(self):
        """skip video in 5 seconds.
        """
        if self.parent.cap.isOpened():
            position = self.parent.pos_frame + 5 * self.parent.fps
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            self.parent.next_frame_slot()
        else:
            pass

    def changeValueSlider(self, value):
        """Set and control the slider to control the video.
        """
        if self.parent.cap.isOpened():
            dst_frame = self.parent.frame_count * value / self.parent.ui.slider_Video.maximum() + 1
            self.parent.cap.set(cv2.CAP_PROP_POS_FRAMES, dst_frame)
            self.parent.next_frame_slot()
            self.timer.stop()
        else:
            pass
