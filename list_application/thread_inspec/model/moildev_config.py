import math
import json
import numpy as np
import cv2
from Moildev import Moildev


class Moildev_config(object):
    def __init__(self, filename):
        """This is the initial configuration that you need provide the parameter. The camera parameter is the result
        from calibration camera by MOIL laboratory. before the successive functions can work correctly,configuration
        is necessary in the beginning of program.

        :param filename: .json file
        :type filename: dictionary
        """
        super(Moildev_config, self).__init__()
        self.PI = 3.1415926
        self.alphaToRho_Table = []
        self.rhoToAlpha_Table = []
        if filename is None:
            pass
        else:
            with open(filename) as f:
                data = json.load(f)
            self.camera = data["cameraName"]
            self.sensor_width = data['cameraSensorWidth']
            self.sensor_height = data['cameraSensorHeight']
            self.Icx = data['iCx']
            self.Icy = data['iCy']
            self.ratio = data['ratio']
            self.imageWidth = data['imageWidth']
            self.imageHeight = data['imageHeight']
            self.calibrationRatio = data['calibrationRatio']
            self.parameter0 = data['parameter0']
            self.parameter1 = data['parameter1']
            self.parameter2 = data['parameter2']
            self.parameter3 = data['parameter3']
            self.parameter4 = data['parameter4']
            self.parameter5 = data['parameter5']

        self.initAlphaRho_Table()
        self.importMoildev()

    def get_cameraName(self):
        """Get camera name.

        :return: Camera name
        :rtype: string
        """
        return self.camera

    def get_sensorWidth(self):
        """Get sensor width of camera.

        :return: sensor_width
        :rtype: float
        """
        return self.sensor_width

    def get_sensor_height(self):
        """Get sensor height of camera.

        :return: sensor_height
        :rtype: float
        """
        return self.sensor_height

    def get_Icx(self):
        """Get center image from width image.

        :return: Image center X
        :rtype: int
        """
        return self.Icx

    def get_Icy(self):
        """Get center image from height image.

        :return: Image center Y
        :rtype: int
        """
        return self.Icy

    def get_ratio(self):
        """Get ratio camera.

        :return: ratio
        :rtype: float
        """
        return self.ratio

    def get_imageWidth(self):
        """Get image width.

        :return: image width
        :rtype: int
        """
        return self.imageWidth

    def get_imageHeight(self):
        """Get image height.

        :return: image height
        :rtype: int
        """
        return self.imageHeight

    def get_calibrationRatio(self):
        """Get calibration ratio of camera.

        :return: calibration ratio
        :rtype: float
        """
        return self.calibrationRatio

    def get_parameter0(self):
        """Get camera parameter.

        :return: Parameter 0
        :rtype: float
        """
        return self.parameter0

    def get_parameter1(self):
        """Get camera parameter.

        :return: Parameter 1
        :rtype: float
        """
        return self.parameter1

    def get_parameter2(self):
        """Get camera parameter.

        :return: Parameter 2
        :rtype: float
        """
        return self.parameter2

    def get_parameter3(self):
        """Get camera parameter.

        :return: Parameter 3
        :rtype: float
        """
        return self.parameter3

    def get_parameter4(self):
        """Get camera parameter.

        :return: Parameter 4
        :rtype: float
        """
        return self.parameter4

    def get_parameter5(self):
        """Get camera parameter.

        :return: Parameter 5
        :rtype: float
        """
        return self.parameter5

    def importMoildev(self):
        """Create moildev instance from moildev SDK share object library

        :return: None
        :rtype: None
        """
        self.moildev = Moildev(self.camera, self.sensor_width, self.sensor_height, self.Icx, self.Icy, self.ratio,
                               self.imageWidth, self.imageHeight, self.calibrationRatio, self.parameter0, self.parameter1, self.parameter2,
                               self.parameter3, self.parameter4, self.parameter5)
        self.map_x = np.zeros((self.imageHeight, self.imageWidth), dtype=np.float32)
        self.map_y = np.zeros((self.imageHeight, self.imageWidth), dtype=np.float32)
        self.res = self.create_map_result_image()

    def create_map_result_image(self):
        """Create Maps image from zeroes matrix for result image

        :return: Matrix
        :rtype: float
        """
        size = self.imageHeight, self.imageWidth, 3
        return np.zeros(size, dtype=np.uint8)

    def get_anypoint_maps(self, alpha, beta, zoom, mode=1):
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
            self.moildev.AnyPointM(self.map_x, self.map_y, alpha, beta, zoom)

        else:
            if alpha < - 90 or alpha > 90 or beta < -90 or beta > 90:
                alpha = 0
                beta = 0

            else:
                alpha = -90 if alpha < -90 else alpha
                alpha = 90 if alpha > 90 else alpha
                beta = -90 if beta < -90 else beta
                beta = 90 if beta > 90 else beta
            self.moildev.AnyPointM2(self.map_x, self.map_y, alpha, beta, zoom)
        return self.map_x, self.map_y

    def get_panorama_maps(self, alpha_min, alpha_max):
        """ To generate a pair of X-Y Maps for alpha within 0..alpha_max degree, the result X-Y Maps can be used later
        to generate a panorama image from the original fisheye image..

        :param alpha_min: alpha min
        :type alpha_min: float
        :param alpha_max: alpha max
        :type alpha_max: float
        :return: pair maps x-y
        :rtype: array
        """
        self.moildev.Panorama(self.map_x, self.map_y, alpha_min, alpha_max)
        return self.map_x, self.map_y

    def anypoint_view(self, image, alpha, beta, zoom, mode=1):
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
        map_x, map_y = self.get_anypoint_maps(alpha, beta, zoom, mode)
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
        :return:
        :rtype:
        """
        map_x, map_y = self.get_panorama_maps(alpha_min, alpha_max)
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
        :return: reverse image
        :rtype: array
        """
        self.moildev.PanoramaM_Rt(self.map_x, self.map_y, alpha_max, alpha, beta)
        result = cv2.remap(image, self.map_x, self.map_y, cv2.INTER_CUBIC)
        self.moildev.revPanorama(result, self.res, alpha_max, beta)
        return self.res

    def initAlphaRho_Table(self):
        """Create list for initial alpha to rho(height image)

        :return:-
        :rtype:-
        """
        for i in range(1800):
            alpha = i / 10 * 3.1415926 / 180
            self.alphaToRho_Table.append((self.parameter0 * alpha * alpha * alpha * alpha * alpha * alpha
                                          + self.parameter1 * alpha * alpha * alpha * alpha * alpha
                                          + self.parameter2 * alpha * alpha * alpha * alpha
                                          + self.parameter3 * alpha * alpha * alpha
                                          + self.parameter4 * alpha * alpha
                                          + self.parameter5 * alpha) * self.calibrationRatio)
            i += 1

        i = 0
        index = 0
        while i < 1800:
            while index < self.alphaToRho_Table[i]:
                self.rhoToAlpha_Table.append(i)
                index += 1
            i += 1

        while index < 3600:
            self.rhoToAlpha_Table.append(i)
            index += 1

    def getAlphaFromRho(self, rho):
        """Return the alpha from rho image

        :param rho: rho image
        :type rho: int
        :return: alpha
        :rtype: int
        """
        if rho >= 0:
            return self.rhoToAlpha_Table[rho] / 10
        else:
            return -self.rhoToAlpha_Table[-rho] / 10

    def getRhoFromAlpha(self, alpha):
        """return rho image from alpha given

        :param alpha:alpha
        :type alpha: float
        :return: rho image
        :rtype: int
        """
        return self.alphaToRho_Table[round(alpha * 10)]

    def get_alpha_beta(self, mode, delta_x, delta_y):
        """calculate the alpha beta from specific coordinate image.
        Args:
            mode = the anypoint mode.
            mode = integer.
            delta_x = the coordinate point in quadrant 1 X axis.
            delta_x = integer.
            delta_y = the coordinate point in quadrant 1 Y axis.
            delta_y = integer.

        return:
            alpha
            beta.
        """
        if mode == 0:
            r = round(math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2)))
            alpha = self.getAlphaFromRho(r)

            if delta_x == 0:
                angle = 0
            else:
                angle = (math.atan2(delta_y, delta_x) * 180) / self.PI

            beta = 90 - angle

        else:
            alpha = self.getAlphaFromRho(delta_y)
            beta = self.getAlphaFromRho(delta_x)

        return alpha, beta
