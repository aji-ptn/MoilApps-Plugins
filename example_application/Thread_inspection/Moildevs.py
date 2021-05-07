import math
import json
import numpy as np
import cv2
from Moildev import Moildev


class Moildevs(object):
    def __init__(self, camera_parameter):
        """This is the initial configuration that you need provide the parameter. The camera parameter is the result
        from calibration camera by MOIL laboratory. before the successive functions can work correctly,configuration
        is necessary in the beginning of program.

        :param camera_parameter: .json file
        :type camera_parameter: dictionary
        """
        super(Moildevs, self).__init__()
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
        """Create list for initial alpha to rho(height image)

        :return:-
        :rtype:-
        """
        for i in range(1800):
            alpha = i / 10 * 3.1415926 / 180
            self.__alphaToRho_Table.append((self.__parameter0 * alpha * alpha * alpha * alpha * alpha * alpha
                                            + self.__parameter1 * alpha * alpha * alpha * alpha * alpha
                                            + self.__parameter2 * alpha * alpha * alpha * alpha
                                            + self.__parameter3 * alpha * alpha * alpha
                                            + self.__parameter4 * alpha * alpha
                                            + self.__parameter5 * alpha) * self.__calibrationRatio)
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

        :return: Camera name
        :rtype: string
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
        self.__moildev = Moildev(self.__camera, self.__sensor_width, self.__sensor_height, self.__Icx, self.__Icy,
                               self.__ratio, self.__imageWidth, self.__imageHeight, self.__calibrationRatio,
                               self.__parameter0, self.__parameter1, self.__parameter2,
                               self.__parameter3, self.__parameter4, self.__parameter5)
        self.__map_x = np.zeros((self.__imageHeight, self.__imageWidth), dtype=np.float32)
        self.__map_y = np.zeros((self.__imageHeight, self.__imageWidth), dtype=np.float32)
        self.__res = self.__create_map_result_image()

    def __create_map_result_image(self):
        """Create Maps image from zeroes matrix for result image

        :return: Matrix
        :rtype: float
        """
        size = self.__imageHeight, self.__imageWidth, 3
        return np.zeros(size, dtype=np.uint8)

    def create_anypoint_maps(self, alpha, beta, zoom, mode=1):
        """The purpose is to generate a pair of X-Y Maps for the specified alpha, beta and zoom parameters,
        the result X-Y Maps can be used later to remap the original fisheye image to the target angle image.

        :param alpha: alpha
        :type alpha: float
        :param beta: beta
        :type beta: float
        :param zoom: decimal zoom factor, normally 1..12
        :type zoom: int
        :param mode: selection anypoint mode(1 or 2)
        :type mode: int
        :return: map_x, map_y
        :rtype: float
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
            self.__moildev.AnyPointM(self.__map_x, self.__map_y, alpha, beta, zoom)

        else:
            if alpha < - 90 or alpha > 90 or beta < -90 or beta > 90:
                alpha = 0
                beta = 0

            else:
                alpha = -90 if alpha < -90 else alpha
                alpha = 90 if alpha > 90 else alpha
                beta = -90 if beta < -90 else beta
                beta = 90 if beta > 90 else beta
            self.__moildev.AnyPointM2(self.__map_x, self.__map_y, alpha, beta, zoom)
        return self.__map_x, self.__map_y

    def create_panorama_maps(self, alpha_min, alpha_max):
        """ To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image..

        :param alpha_min: alpha min
        :type alpha_min: float
        :param alpha_max: alpha max
        :type alpha_max: float
        :return: pair maps x-y
        :rtype: array
        """
        self.__moildev.Panorama(self.__map_x, self.__map_y, alpha_min, alpha_max)
        return self.__map_x, self.__map_y

    def anypoint(self, image, alpha, beta, zoom, mode=1):
        """Generate anypoint view.for mode 1, the result rotation is betaOffset degree rotation around the
        Z-axis(roll) after alphaOffset degree rotation around the X-axis(pitch). for mode 2, The result rotation
        is thetaY degree rotation around the Y-axis(yaw) after thetaX degree rotation around the X-axis(pitch).

        :param image: source image
        :type image: array
        :param alpha: alpha
        :type alpha: float
        :param beta: beta
        :type beta: float
        :param zoom: zoom
        :type zoom: int
        :param mode: mode anypoint view
        :type mode: int
        :return: anypoint view
        :rtype: array
        """
        map_x, map_y = self.create_anypoint_maps(alpha, beta, zoom, mode)
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
        map_x, map_y = self.create_panorama_maps(alpha_min, alpha_max)
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
        self.__moildev.PanoramaM_Rt(self.__map_x, self.__map_y, alpha_max, alpha, beta)
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
