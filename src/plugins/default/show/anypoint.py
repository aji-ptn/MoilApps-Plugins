from ..contoller.utils import drawPoint, drawPolygon
from ..contoller.showResult import ShowImageResult
import numpy as np
import cv2


class AnyPoint(object):
    def __init__(self, MainWindow):
        """
        Anypoint class to process image on anypoint view.

        Args:
            MainWindow ():
        """
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.connectToButton()

    def connectToButton(self):
        """
        The method for connected function and event on main window user interface.

        Returns:
            None.
        """
        self.parent.ui.Button_setAnypoint.clicked.connect(self.set_anypoint)
        self.parent.ui.btn_Anypoint.clicked.connect(self.onclickAnypoint)
        self.parent.ui.radioAnypointM1.clicked.connect(self.anypoint_mode_1)
        self.parent.ui.radioAnypointM2.clicked.connect(self.anypoint_mode_2)
        self.parent.ui.spinBox_zoom.valueChanged.connect(self.zoomValue)
        self.parent.ui.btn_up.clicked.connect(self.up)
        self.parent.ui.btn_left.clicked.connect(self.left)
        self.parent.ui.btn_center.clicked.connect(self.center)
        self.parent.ui.btn_right.clicked.connect(self.right)
        self.parent.ui.brn_down.clicked.connect(self.down)
        self.parent.ui.radioAnypointM1.setChecked(True)

    def zoomValue(self):
        """
        The methode to change the zoom value when doing anypoint view.

        Returns:
            None.
        """
        self.parent.zoom = self.parent.ui.spinBox_zoom.value()
        self.anypoint_view()

    def resetAlphaBeta(self):
        """
        The method for reset alpa, beta, zoom, and angle.

        Returns:

        """
        self.parent.alpha = 0
        self.parent.beta = 0
        self.parent.zoom = 4
        self.parent.angle = 0
        if self.parent.image is None:
            self.parent.coordinate_point = None
        else:
            self.parent.coordinate_point = self.parent.center

    def onclickAnypoint(self):
        """
        The method for click button anypoint.

        Returns:

        """
        self.parent.ui.checkBox_ShowRecenterImage.setChecked(False)
        self.parent.panorama.recenterImage()
        if self.parent.ui.radioAnypointM1.isChecked():
            self.anypoint_mode_1()
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.anypoint_mode_2()

    def anypoint_view(self):
        """
        The method to clearly process image on anypoint view.

        Returns:

        """
        if self.parent.image is None:
            pass
        else:
            image = self.parent.image.copy()
            if self.parent.ui.btn_Anypoint.isChecked():
                self.parent.ui.btn_Panorama.setChecked(False)
                self.parent.ui.frame_4.show()
                self.parent.ui.frame_5.hide()
                self.parent.ui.frame_4.setDisabled(False)
                self.parent.ui.frame_5.setDisabled(True)
                self.alpha = self.parent.alpha
                self.beta = self.parent.beta
                self.zoom = self.parent.zoom
                self.parent.mapX, self.parent.mapY = self.parent.moildev.getAnypointMaps(
                    self.alpha, self.beta, self.zoom, self.parent.anypointState)

                self.show.view_result(self.parent.image)
                self.updateParamAnypoint()

            else:
                self.parent.ui.frame_4.setDisabled(True)
                self.parent.ui.frame_5.setDisabled(True)
                self.parent.ui.frame_4.hide()
                self.parent.ui.frame_5.hide()
                self.show.showOriginalImage(image)
                self.show.view_result(image)

    def showPolygon(self):
        """
        Showing the polygon on original image.

        Returns:

        """
        image = self.parent.image.copy()
        image = drawPolygon(image, self.parent.mapX, self.parent.mapY)
        if self.parent.coordinate_point is None:
            self.show.showOriginalImage(image)
        else:
            image = drawPoint(
                image,
                self.parent.h,
                self.parent.coordinate_point)
            self.show.showOriginalImage(image)

    def updateParamAnypoint(self):
        """
        The method for update anypoint on the beta, alpha and zoom.

        Returns:

        """
        self.parent.ui.lineEdit_beta.setText("%.2f" % self.beta)
        self.parent.ui.lineEdit_alpha.setText("%.2f" % self.alpha)
        self.parent.ui.spinBox_zoom.setValue(self.zoom)

    def anypoint_mode_1(self):
        """
        Determine the anypoint mode 1.

        Returns:

        """
        self.parent.anypointState = 1
        self.resetAlphaBeta()
        self.anypoint_view()

    def anypoint_mode_2(self):
        """
        Determine the anypoint mode 2.

        Returns:

        """
        self.parent.anypointState = 2
        self.resetAlphaBeta()
        self.anypoint_view()

    def set_anypoint(self):
        """
        The method for event on click button set anypoint when has modify the parameter.

        Returns:

        """
        self.parent.alpha = float(self.parent.ui.lineEdit_alpha.text())
        self.parent.beta = float(self.parent.ui.lineEdit_beta.text())
        self.parent.zoom = float(self.parent.ui.spinBox_zoom.text())
        self.anypoint_view()

    def up(self):
        """
        The method showing anypoint view in specific area.

        Returns:

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

        Returns:

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

        Returns:

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

        Returns:

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

        Returns:

        """
        self.parent.coordinate_point = None
        if self.parent.ui.radioAnypointM1.isChecked():
            self.parent.alpha = 65
            self.parent.beta = 180
        elif self.parent.ui.radioAnypointM2.isChecked():
            self.parent.alpha = -65
            self.parent.beta = 0
        self.parent.anypoint.anypoint_view()
