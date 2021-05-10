import math
import json
import datetime
import os
import cv2
import numpy as np
from PyQt5 import QtWidgets
from MoilCV import MoilCV


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


def draw_polygon(image, mapX, mapY):
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
        a = mapX[0,]
        b = mapY[0,]
        e = mapX[-1,]
        f = mapY[-1,]

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


def rotate(src, angle, center=None, scale=1.0):
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


class Moildev(object):
    def __init__(self, camera_parameter):
        """
        This is the initial configuration that you need provide the parameter. The camera parameter is the result
        from calibration camera by MOIL laboratory. before the successive functions can work correctly,configuration
        is necessary in the beginning of program.

        Args:
            camera_parameter (): .json file

        for more detail, please reference https://github.com/MoilOrg/moildev
        """
        super(Moildev, self).__init__()
        self.__PI = 3.1415926
        self.__alphaToRho_Table = []
        self.__rhoToAlpha_Table = []
        if camera_parameter is None:
            pass
        else:
            with open(camera_parameter) as f:
                data = json.load(f)
            self.__camera = data["cameraName"]
            self.__sensor_width = data['cameraSensorWidth']
            self.__sensor_height = data['cameraSensorHeight']
            self.__Icx = data['iCx']
            self.__Icy = data['iCy']
            self.__ratio = data['ratio']
            self.__imageWidth = data['imageWidth']
            self.__imageHeight = data['imageHeight']
            self.__calibrationRatio = data['calibrationRatio']
            self.__parameter0 = data['parameter0']
            self.__parameter1 = data['parameter1']
            self.__parameter2 = data['parameter2']
            self.__parameter3 = data['parameter3']
            self.__parameter4 = data['parameter4']
            self.__parameter5 = data['parameter5']

        self.__initAlphaRho_Table()
        self.__importMoildev()

    def __initAlphaRho_Table(self):
        """
        Create list for initial alpha to rho(height image).

        Returns:
            Initial alpha and rho table.
        """
        for i in range(1800):
            alpha = i / 10 * 3.1415926 / 180
            self.__alphaToRho_Table.append(
                (self.__parameter0 *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter1 *
                 alpha *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter2 *
                 alpha *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter3 *
                 alpha *
                 alpha *
                 alpha +
                 self.__parameter4 *
                 alpha *
                 alpha +
                 self.__parameter5 *
                 alpha) *
                self.__calibrationRatio)
            i += 1

        i = 0
        index = 0
        while i < 1800:
            while index < self.__alphaToRho_Table[i]:
                self.__rhoToAlpha_Table.append(i)
                index += 1
            i += 1

        while index < 3600:
            self.__rhoToAlpha_Table.append(i)
            index += 1

    def get_cameraName(self):
        """Get camera name.

        Returns:
            Camera name
        """
        return self.__camera

    def get_Icx(self):
        """Get center image from width image.

        :return: Image center X
        :rtype: int
        """
        return self.__Icx

    def get_Icy(self):
        """Get center image from height image.

        :return: Image center Y
        :rtype: int
        """
        return self.__Icy

    def get_imageWidth(self):
        """Get image width.

        :return: image width
        :rtype: int
        """
        return self.__imageWidth

    def get_imageHeight(self):
        """Get image height.

        :return: image height
        :rtype: int
        """
        return self.__imageHeight

    def __importMoildev(self):
        """Create moildev instance from Moildev SDK share object library

        :return: None
        :rtype: None
        """
        self.__moildev = MoilCV(
            self.__camera,
            self.__sensor_width,
            self.__sensor_height,
            self.__Icx,
            self.__Icy,
            self.__ratio,
            self.__imageWidth,
            self.__imageHeight,
            self.__calibrationRatio,
            self.__parameter0,
            self.__parameter1,
            self.__parameter2,
            self.__parameter3,
            self.__parameter4,
            self.__parameter5)
        self.__map_x = np.zeros(
            (self.__imageHeight,
             self.__imageWidth),
            dtype=np.float32)
        self.__map_y = np.zeros(
            (self.__imageHeight,
             self.__imageWidth),
            dtype=np.float32)
        self.__res = self.__create_map_result_image()

    def __create_map_result_image(self):
        """
        Create Maps image from zeroes matrix for result image.

        Returns:
            Zeroes matrix same size with original image to stored data from result image.
        """
        size = self.__imageHeight, self.__imageWidth, 3
        return np.zeros(size, dtype=np.uint8)

    def getAnypointMaps(self, alpha, beta, zoom, mode=1):
        """The purpose is to generate a pair of X-Y Maps for the specified alpha, beta and zoom parameters,
        the result X-Y Maps can be used later to remap the original fisheye image to the target angle image.

        Args:
            alpha (): value of zenital distance(float).
            beta (): value of azimuthal distance based on cartography system(float)
            zoom (): value of zoom(float)
            mode (): selection anypoint mode(1 or 2)

        Returns:
            mapX:
            mapY:

        """
        if mode == 1:
            if beta < 0:
                beta = beta + 360
            if alpha < -90 or alpha > 90 or beta < 0 or beta > 360:
                alpha = 0
                beta = 0

            else:
                alpha = -90 if alpha < -90 else alpha
                alpha = 90 if alpha > 90 else alpha
                beta = 0 if beta < 0 else beta
                beta = 360 if beta > 360 else beta
            self.__moildev.AnyPointM(
                self.__map_x, self.__map_y, alpha, beta, zoom)

        else:
            if alpha < - 90 or alpha > 90 or beta < -90 or beta > 90:
                alpha = 0
                beta = 0

            else:
                alpha = -90 if alpha < -90 else alpha
                alpha = 90 if alpha > 90 else alpha
                beta = -90 if beta < -90 else beta
                beta = 90 if beta > 90 else beta
            self.__moildev.AnyPointM2(
                self.__map_x, self.__map_y, alpha, beta, zoom)
        return self.__map_x, self.__map_y

    def getPanoramaMaps(self, alpha_min, alpha_max):
        """
        To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image.

        Args:
            alpha_min ():
            alpha_max ():

        Returns:

        """
        self.__moildev.Panorama(
            self.__map_x,
            self.__map_y,
            alpha_min,
            alpha_max)
        return self.__map_x, self.__map_y

    def anypoint(self, image, alpha, beta, zoom, mode=1):
        """
        Generate anypoint view.for mode 1, the result rotation is betaOffset degree rotation around the
        Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch). for mode 2, The result rotation
        is thetaY degree rotation around the Y-axis(yaw) after thetaX degree rotation around the X-axis(pitch).

        Args:
            image ():
            alpha ():
            beta ():
            zoom ():
            mode ():

        Returns:

        """
        map_x, map_y = self.getAnypointMaps(alpha, beta, zoom, mode)
        image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
        return image

    def panorama(self, image, alpha_min, alpha_max):
        """The panorama image centered at the 3D direction with alpha = iC_alpha_degree and beta = iC_beta_degree

        :param image:
        :type image:
        :param alpha_min:
        :type alpha_min:
        :param alpha_max:
        :type alpha_max:
        :return: panorama image
        :rtype: array
        """
        map_x, map_y = self.getPanoramaMaps(alpha_min, alpha_max)
        image = cv2.remap(image, map_x, map_y, cv2.INTER_CUBIC)
        return image

    def reverse_image(self, image, alpha_max, alpha, beta):
        """To generate the image reverse image from panorama that can change the focus direction from the original
        images. The panorama reverse image centered at the 3D direction with alpha_max = max of alpha and beta =
        iC_beta_degree.

        :param image: source image
        :type image: array
        :param alpha_max: alpha max
        :type alpha_max: float
        :param alpha: alpha
        :type alpha: float
        :param beta: beta
        :type beta: float
        :return: reverse view image
        :rtype: array
        """
        self.__moildev.PanoramaM_Rt(
            self.__map_x, self.__map_y, alpha_max, alpha, beta)
        result = cv2.remap(image, self.__map_x, self.__map_y, cv2.INTER_CUBIC)
        self.__moildev.revPanorama(result, self.__res, alpha_max, beta)
        return self.__res

    def getAlphaFromRho(self, rho):
        """Get the alpha from rho image.

        :param rho: rho image
        :type rho: int
        :return: alpha
        :rtype: float
        """
        if rho >= 0:
            return self.__rhoToAlpha_Table[rho] / 10
        else:
            return -self.__rhoToAlpha_Table[-rho] / 10

    def getRhoFromAlpha(self, alpha):
        """Get rho image from alpha given.

        :param alpha:alpha
        :type alpha: float
        :return: rho image
        :rtype: int
        """
        return self.__alphaToRho_Table[round(alpha * 10)]

    def get_alpha_beta(self, delta_x, delta_y, mode=1):
        """Get the alpha beta from specific coordinate image.

        :param mode: the anypoint mode.
        :type mode: int
        :param delta_x: the coordinate point in quadrant one (1) X axis.
        :type delta_x: int
        :param delta_y: the coordinate point in quadrant one (1) Y axis.
        :type delta_y: int
        :return: alpha, beta
        :rtype: float
        """
        if mode == 1:
            r = round(math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2)))
            alpha = self.getAlphaFromRho(r)

            if delta_x == 0:
                angle = 0
            else:
                angle = (math.atan2(delta_y, delta_x) * 180) / self.__PI

            beta = 90 - angle

        else:
            alpha = self.getAlphaFromRho(delta_y)
            beta = self.getAlphaFromRho(delta_x)

        return alpha, beta
