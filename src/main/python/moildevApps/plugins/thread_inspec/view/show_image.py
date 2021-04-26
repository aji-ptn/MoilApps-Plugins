import cv2
from PyQt5 import QtCore, QtGui
from ..model.utils_function import Rotate


class Show_Image(object):
    def __init__(self, MainWindow):
        self.main_w = MainWindow

    @staticmethod
    def calculate_ratio_image(image, image_width):
        """Calculate the size ratio
        """
        h, w = image.shape[:2]
        r = image_width / float(w)
        height = round(h * r)
        return height

    def image_wheel_event(self):
        pass

    def show_original_image(self, image, width):
        height = self.calculate_ratio_image(image, width)
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        label_image = self.main_w.ui.label_Original_Image
        label_image.setMinimumSize(QtCore.QSize(width, height))
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        label_image.setPixmap(QtGui.QPixmap.fromImage(image))

    def show_result_image(self, image, width, angle=0):
        height = self.calculate_ratio_image(image, width)
        image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
        image = Rotate(image, angle)
        label_image = self.main_w.ui.label_Result_Image
        label_image.setMinimumSize(QtCore.QSize(width, height))
        image = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        label_image.setPixmap(QtGui.QPixmap.fromImage(image))
