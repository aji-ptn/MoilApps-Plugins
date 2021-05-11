import cv2


class AnypointView(object):
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4
        self.anypoint_mode = 1
        self.parent.ui.radio_btn_mode_1.setChecked(True)
        self.connect_button_to_event()

    def connect_button_to_event(self):
        """
        Connect button user interface to the function.

        Returns:

        """
        self.parent.ui.btn_anypoint.clicked.connect(self.process_to_anypoint)
        self.parent.ui.label_Result_Image.mouseDoubleClickEvent = self.mouseDoubleclick_event
        self.parent.ui.btn_Up_View.clicked.connect(self.up)
        self.parent.ui.btn_Right_view.clicked.connect(self.right)
        self.parent.ui.btn_left_view.clicked.connect(self.left)
        self.parent.ui.btn_center_view.clicked.connect(self.center)
        self.parent.ui.btn_Down_view.clicked.connect(self.down)
        self.parent.ui.radio_btn_mode_1.clicked.connect(self.anypoint_mode_1)
        self.parent.ui.radio_btn_mode_2.clicked.connect(self.anypoint_mode_2)

    def process_to_anypoint(self):
        """
        This function is to process the image and show on anypoint mode.

        Returns:

        """
        if self.parent.image is not None:
            self.parent.normal_mode = False
            self.parent.ui.frame_anypoint.show()
            self.parent.ui.frame_navigator.show()
            self.parent.ui.frame_panorama.hide()
            self.parent.mapX, self.parent.mapY, = self.parent.moildev.getAnypointMaps(
                self.alpha, self.beta, self.zoom_any, self.anypoint_mode)
            self.parent.show_to_window()

    def anypoint_mode_1(self):
        """
        Execute the anypoint process mode 1.

        Returns:
            None.
        """
        self.anypoint_mode = 1
        self.resetAlphaBeta()
        self.process_to_anypoint()

    def anypoint_mode_2(self):
        """
        Execute the anypoint process mode 2.

        Returns:
            None.
        """
        self.anypoint_mode = 2
        self.resetAlphaBeta()
        self.process_to_anypoint()

    def resetAlphaBeta(self):
        """
        The method for reset alpha, beta, zoom, and angle.

        Returns:
            None.
        """
        self.alpha = 0
        self.beta = 0
        self.zoom_any = 4

    def mouseDoubleclick_event(self, e):
        """
        Reset to default by mouse event.

        Args:
            e ():

        Returns:

        """
        print("tetetete")
        self.resetAlphaBeta()
        self.process_to_anypoint()

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
        delta_x = round(pos_x * ratio_x - self.w * 0.5)
        delta_y = round(- (pos_y * ratio_y - self.h * 0.5))
        self.coordinate_point = (
            round(
                pos_x *
                ratio_x),
            round(
                pos_y *
                ratio_y))
        if self.ui.btn_Anypoint.isChecked():
            self.alpha, self.beta = self.moildev.get_alpha_beta(
                delta_x, delta_y, self.anypointState)
            self.anypoint.anypoint_view()

    def up(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radio_btn_mode_1.isChecked():
            self.alpha = 75
            self.beta = 0
        elif self.parent.ui.radio_btn_mode_2.isChecked():
            self.alpha = 50
            self.beta = 0
        self.process_to_anypoint()

    def left(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = -90
        elif self.parent.ui.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = -75
        self.process_to_anypoint()

    def center(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radio_btn_mode_1.isChecked():
            self.alpha = 0
            self.beta = 0
        elif self.parent.ui.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 0
        self.process_to_anypoint()

    def right(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 90
        elif self.parent.ui.radio_btn_mode_2.isChecked():
            self.alpha = 0
            self.beta = 65
        self.process_to_anypoint()

    def down(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radio_btn_mode_1.isChecked():
            self.alpha = 65
            self.beta = 180
        elif self.parent.ui.radio_btn_mode_2.isChecked():
            self.alpha = -65
            self.beta = 0
        self.process_to_anypoint()
