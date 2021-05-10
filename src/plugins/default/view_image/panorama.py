from Moildev import draw_point
from ..contoller.showResult import ShowImageResult


class Panorama(object):
    def __init__(self, MainWindow):
        """
        The class to process image ang generate panorama view.

        Args:
            MainWindow (): Is the parent class to access the user interface widget in this application.
        """
        self.parent = MainWindow
        self.show = ShowImageResult(self.parent)
        self.max = float(110)
        self.min = float(10)
        self.parent.ui.lineEdit_Max.setText(str(self.max))
        self.parent.ui.lineEdit_Min.setText(str(self.min))
        self.connectToButton()

    def connectToButton(self):
        """
        This function for connect to button in user interface

        Returns:
            Process button event
        """
        self.parent.ui.btn_Panorama.clicked.connect(self.panorama_view)
        self.parent.ui.btn_setPanorama.clicked.connect(self.set_panorama)
        self.parent.ui.spinBox_coorX.valueChanged.connect(self.positionCoorX)
        self.parent.ui.spinBox_coorY.valueChanged.connect(self.positionCoorY)
        self.parent.ui.checkBox_ShowRecenterImage.clicked.connect(
            self.recenterImage)

    def control_button_on_panorama(self):
        """
        Control the button show or hide on panorama mode.

        Returns:
            None.
        """
        self.parent.ui.btn_Anypoint.setChecked(False)
        self.parent.ui.frame_4.hide()
        self.parent.ui.frame_4.setDisabled(True)
        self.parent.ui.frame_5.show()
        self.parent.ui.frame_5.setDisabled(False)

    def control_button_of_panorama(self):
        """
        Control the button show or hide after you're not in panorama mode.

        Returns:

        """
        self.parent.ui.frame_4.setDisabled(True)
        self.parent.ui.frame_5.setDisabled(True)
        self.parent.ui.frame_4.hide()
        self.parent.ui.frame_5.hide()
        self.parent.ui.checkBox_ShowRecenterImage.setChecked(False)

    def set_panorama(self):
        """
        This function for setting the maximum and minimum of panorama view.

        Returns:
            None.
        """
        self.max = float(self.parent.ui.lineEdit_Max.text())
        self.min = float(self.parent.ui.lineEdit_Min.text())
        self.panorama_view()

    def panorama_view(self):
        """
        This function to process image to panorama view.

        Returns:
            Panorama image.
        """
        image = self.parent.image.copy()
        if self.parent.ui.btn_Panorama.isChecked():
            self.parent.coor = self.parent.center
            self.control_button_on_panorama()
            self.parent.ui.lineEdit_Max.setText(str(self.max))
            self.parent.ui.lineEdit_Min.setText(str(self.min))
            self.parent.mapX, self.parent.mapY = self.parent.moildev.getPanoramaMaps(
                self.min, self.max)
            self.resetCenter()
            self.show.view_result(self.parent.image)

        else:
            self.control_button_of_panorama()
            self.recenterImage()
            self.show.showOriginalImage(image)
            self.show.view_result(image)

    def recenterImage(self):
        """
        Process original image to change the original center image.

        Returns:

        """
        if self.parent.ui.checkBox_ShowRecenterImage.isChecked():
            self.parent.ui.frame.show()
            self.parent.ui.labelRecenter.show()
            self.parent.ui.labelImagerecenter.show()
            self.max = float(self.parent.ui.lineEdit_Max.text())
            self.min = float(self.parent.ui.lineEdit_Min.text())
            self.parent.revImage = self.parent.moildev.reverse_image(
                self.parent.image, 110, self.parent.alpha, self.parent.beta)
            self.parent.mapX, self.parent.mapY = self.parent.moildev.getPanoramaMaps(
                self.min, self.max)
            self.show.showInRecenterLabel(self.parent.revImage)
            self.show.view_result(self.parent.image)
            self.updatePossCenter()

        else:
            self.parent.ui.labelRecenter.hide()
            self.parent.ui.labelImagerecenter.hide()
            self.parent.ui.frame.hide()

    def positionCoorX(self):
        """
        Change the position coordinate center X on image recenter process

        Returns:

        """
        if self.parent.image is None:
            pass
        else:
            self.parent.coorX = self.parent.ui.spinBox_coorX.value()
            self.setCoorCenterObject()
            self.recenterImage()

    def positionCoorY(self):
        """
        Change the position coordinate center Y on image recenter process

        Returns:

        """
        if self.parent.image is None:
            pass
        else:
            self.parent.coorY = self.parent.ui.spinBox_coorY.value()
            self.setCoorCenterObject()
            self.recenterImage()

    def updatePossCenter(self):
        """
        Update position center x and y point in the user interface

        Returns:

        """
        self.parent.ui.spinBox_coorX.setValue(self.parent.coorX)
        self.parent.ui.spinBox_coorY.setValue(self.parent.coorY)

    def resetCenter(self):
        """
        This function for reset coordinate x and y.

        Returns:

        """
        self.parent.coorX = self.parent.w * 0.5
        self.parent.coorY = self.parent.h * 0.5
        self.parent.ui.spinBox_coorX.setValue(self.parent.coorX)
        self.parent.ui.spinBox_coorY.setValue(self.parent.coorY)

    def setCoorCenterObject(self):
        """
        Calculate alpha and beta from the original center image.

        Returns:

        """
        delta_x = round(self.parent.coorX - self.parent.w * 0.5)
        delta_y = round(- (self.parent.coorY - self.parent.h * 0.5))
        self.parent.alpha, self.parent.beta = self.parent.moildev.get_alpha_beta(
            delta_x, delta_y)

    def showOriginalPanorama(self):
        """
        Show original image when doing panorama view on the original label.

        Returns:

        """
        image = self.parent.image.copy()
        if self.parent.coor:
            oriImage = draw_point(image, self.parent.w, self.parent.coor)
        else:
            oriImage = draw_point(image, self.parent.h, self.parent.center)
        self.show.showOriginalImage(oriImage)
