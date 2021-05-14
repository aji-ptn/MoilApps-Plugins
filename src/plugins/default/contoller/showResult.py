import cv2
from PyQt5 import QtGui, QtCore
from .resize_image import ResizeImage
from Moildev import rotate


class ShowImageResult(object):
    def __init__(self, MainWindow):
        """
        Class to Show Image Result on user interface.

        Args:
            MainWindow ():
        """
        self.parent = MainWindow
        self.ratio = ResizeImage(self.parent)

    def showInRecenterLabel(self, image):
        """
        Show the recenter label to showing the recenter image on UI.

        Args:
            image ():

        Returns:
            None.
        """
        annotate_image = self.ratio.resize_original_image(image)
        my_label3 = self.parent.ui.labelImagerecenter
        annotate_image = QtGui.QImage(
            annotate_image.data,
            annotate_image.shape[1],
            annotate_image.shape[0],
            QtGui.QImage.Format_RGB888).rgbSwapped()
        my_label3.setPixmap(QtGui.QPixmap.fromImage(annotate_image))

    def showOriginalImage(self, imageOri):
        """
        Showing the original image in label original image UI.

        Args:
            imageOri ():

        Returns:

        """
        imageOriginal = self.ratio.resize_original_image(imageOri)
        image = QtGui.QImage(
            imageOriginal.data,
            imageOriginal.shape[1],
            imageOriginal.shape[0],
            QtGui.QImage.Format_RGB888).rgbSwapped()
        image = QtGui.QPixmap.fromImage(image)
        self.parent.ui.windowOri.setPixmap(image)

    def showPanoAnyImage(self, image, angle=0):
        """
        The method for showing result image after process to panorama or anypoint.

        Args:
            image: The result image
            angle: the angle if want to rotate the image

        return:
            None
        """
        if self.parent.ui.checkBox_ShowRecenterImage.isChecked():
            self.resultImage = cv2.remap(
                self.parent.revImage,
                self.parent.mapX,
                self.parent.mapY,
                cv2.INTER_CUBIC)
        else:
            self.resultImage = cv2.remap(
                image, self.parent.mapX, self.parent.mapY, cv2.INTER_CUBIC)
        self.resultImage = rotate(self.resultImage, angle)
        self.label_result(self.resultImage, self.parent.width_img)
        self.parent.resultImage = self.resultImage

    def view_result(self, image):
        """
        Show the result image.

        Args:
            image ():

        Returns:

        """
        self.showOriginalImage(image)
        if self.parent.ui.btn_Anypoint.isChecked():
            self.parent.anypoint.showPolygon()
            self.showPanoAnyImage(image)
        elif self.parent.ui.btn_Panorama.isChecked():
            self.parent.panorama.showOriginalPanorama()
            self.showPanoAnyImage(image)
        else:
            self.label_result(image, self.parent.width_img)

    def label_result(self, resultImage, width_img):
        """
        This method is to resize the label result image and show the result image in there.

        Args:
            resultImage ():
            width_img ():

        Returns:

        """
        self.parent.ui.windowResult.setMinimumSize(QtCore.QSize(width_img, 0))
        resultImage = self.ratio.resize_result_image(resultImage, width_img)
        image = QtGui.QImage(
            resultImage.data,
            resultImage.shape[1],
            resultImage.shape[0],
            QtGui.QImage.Format_RGB888).rgbSwapped()
        image = QtGui.QPixmap.fromImage(image)
        self.parent.ui.windowResult.setPixmap(image)
