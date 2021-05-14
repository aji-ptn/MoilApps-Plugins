import datetime
import os
from PyQt5 import QtWidgets


def select_file(title, dir_path, file_filter):
    """
    Find the file path from the directory computer.

    Args:
        title: the title window of open dialog
        file_filter: determine the specific file want to search
        dir_path: Navigate to specific directory

    return:
        file_path:
    """
    options = QtWidgets.QFileDialog.DontUseNativeDialog
    file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, title, dir_path,
                                                         file_filter,
                                                         options=options)
    return file_path


def draw_point(image, heightImage, coordinatePoint):
    """
    Drawing the dot on the image from the coordinate given

    Args:
        image : Image
        heightImage : to determine the point size in the image
        coordinatePoint : determine the location of the point in the image

    return:
        image:
    """
    if heightImage >= 1000:
        cv2.circle(image, coordinatePoint, 10, (0, 255, 0), 20, -1)
    else:
        cv2.circle(image, coordinatePoint, 6, (0, 255, 0), 12, -1)
    return image


def save_image(filename, image):
    """
    Saving images and give a name to store in local directory

    Args:
        filename : give the image a filename
        image : the captured image

    return:
        None
    """
    save_time = datetime.datetime.now().strftime("%H_%M_%S")
    name = "../result/Images/" + filename + "_" + str(save_time) + ".png"
    os.makedirs(os.path.dirname(name), exist_ok=True)
    cv2.imwrite(name, image)
    QtWidgets.QMessageBox.information(None, "Information", "Image saved !!")
