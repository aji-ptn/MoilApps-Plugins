from PyQt5 import QtWidgets
import datetime
import os
import cv2
import numpy as np


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


def Rotate(src, angle, center=None, scale=1.0):
    """
    Turn an image in a clockwise or counterclockwise direction.

    Args:
        src: original image
        angle: the value angle for turn the image
        center: determine the specific coordinate to rotate image
        scale: scale image

    Returns:
        dst image: rotated image
    """
    h, w = src.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(src, m, (w, h))
    return rotated


def read_image(image_path):
    """
    Reading the image from given file path

    Args:
        image_path : image to be read from the image_path

    return:
        img:
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("`{}` not cannot be loaded".format(image_path))
    return image


def saveImage(filename, image):
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


def drawPoint(image, heightImage, coordinatePoint):
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


def drawPolygon(image, mapX, mapY):
    """
    Draw polygon from mapX and mapY given in the original image.

    Args:
        image: Original image
        mapX: map image X from anypoint process
        mapY: map image Y from anypoint process
    return:
        image:
    """
    hi, wi = image.shape[:2]
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    X3 = []
    Y3 = []
    X4 = []
    Y4 = []

    x = 0
    while x < wi:
        a = mapX[0, ]
        b = mapY[0, ]
        e = mapX[-1, ]
        f = mapY[-1, ]

        if a[x] == 0. or b[x] == 0.:
            pass
        else:
            X1.append(a[x])
            Y1.append(b[x])

        if f[x] == 0. or e[x] == 0.:
            pass
        else:
            Y3.append(f[x])
            X3.append(e[x])
        x += 10

    y = 0
    while y < hi:
        c = mapX[:, 0]
        d = mapY[:, 0]
        g = mapX[:, -1]
        h = mapY[:, -1]

        # eliminate the value 0 for map X
        if d[y] == 0. or c[y] == 0.:  # or d[y] and c[y] == 0.0:
            pass
        else:
            Y2.append(d[y])
            X2.append(c[y])

        # eliminate the value 0 for map Y
        if h[y] == 0. or g[y] == 0.:
            pass
        else:
            Y4.append(h[y])
            X4.append(g[y])

        # render every 10 times, it will be like 1, 11, 21 and so on.
        y += 10

    p = np.array([X1, Y1])
    q = np.array([X2, Y2])
    r = np.array([X3, Y3])
    s = np.array([X4, Y4])
    points = p.T.reshape((-1, 1, 2))
    points2 = q.T.reshape((-1, 1, 2))
    points3 = r.T.reshape((-1, 1, 2))
    points4 = s.T.reshape((-1, 1, 2))

    # Draw polyline on original image
    cv2.polylines(image, np.int32([points]), False, (0, 255, 0), 10)
    cv2.polylines(image, np.int32([points2]), False, (0, 255, 0), 10)
    cv2.polylines(image, np.int32([points3]), False, (0, 255, 0), 10)
    cv2.polylines(image, np.int32([points4]), False, (0, 255, 0), 10)
    return image
