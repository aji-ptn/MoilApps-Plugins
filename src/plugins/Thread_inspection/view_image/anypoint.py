import cv2


class AnypointView(object):
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.connect_event()

    def connect_event(self):
        self.parent.ui.btn_anypoint.clicked.connect(self.process_to_anypoint)

    def process_to_anypoint(self):
        """This function is to process the image and show on anypoint mode.
        """
        if self.parent.image is None:
            pass
        else:
            self.parent.normal_mode = False
            self.parent.ui.frame_anypoint.show()
            self.parent.ui.frame_navigator.show()
            self.parent.ui.frame_panorama.hide()
            # self.mapx, mapy = self.parent.moildev.getAnypointMaps(
            #     self.parent.alpha, self.parent.beta, self.parent.zoom, self.parent.anypoint_mode)
            self.parent.result_image = self.parent.moildev.anypoint(
                self.parent.image, 0, 0, 4, 2)
            self.parent.show_image.show_result_image(
                self.parent.result_image, self.parent.width_result_image)

    def remap_image(self):
        self.parent.result_image = cv2.remap(
            self.parent.image,
            self.parent.mapX,
            self.parent.mapY,
            cv2.INTER_CUBIC)

    def up(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 75
            self.parent.beta = 0
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 50
            self.parent.beta = 0
        self.parent.anypoint.anypoint_view()

    def left(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = -90
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 0
            self.parent.beta = -75
        self.parent.anypoint.anypoint_view()

    def center(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 0
            self.parent.beta = 0
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 0
            self.parent.beta = 0
        self.parent.anypoint.anypoint_view()

    def right(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = 90
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = 0
            self.parent.beta = 65
        self.parent.anypoint.anypoint_view()

    def down(self):
        """
        The method showing anypoint view in specific area.
        """
        self.parent.coordinate_point = None
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = 180
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = -65
            self.parent.beta = 0
        self.parent.anypoint.anypoint_view()
