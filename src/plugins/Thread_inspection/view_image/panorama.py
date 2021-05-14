import numpy as np


class PanoramaView(object):
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.pano_alpha_min = 10
        self.pano_alpha_max = 110
        self.rho = None
        self.parent.ui.min_pano.setText(str(self.pano_alpha_min))
        self.parent.ui.max_pano.setText(str(self.pano_alpha_max))
        self.connect_event()

    def connect_event(self):
        self.parent.ui.btn_panorama.clicked.connect(self.process_to_panorama)
        self.parent.ui.pushButton.clicked.connect(self.change_panorama_fov)

    def process_to_panorama(self):
        if self.parent.image is not None:
            self.parent.normal_mode = False
            self.parent.panorama_mode = True
            # self.parent.width_result_image = self.parent.ui.label_Result_Image.width()
            self.rho = self.parent.moildev.getRhoFromAlpha(self.pano_alpha_min)
            self.parent.ui.frame_navigator.hide()
            self.parent.ui.frame_panorama.show()
            mapX, mapY, = self.parent.moildev.getPanoramaMaps(
                10, 100)
            np.save("./plugins/Thread_inspection/view_image/maps_pano/mapX.npy", mapX)
            np.save("./plugins/Thread_inspection/view_image/maps_pano/mapY.npy", mapY)

            self.parent.mapX_pano, self.parent.mapY_pano = self.parent.moildev.getPanoramaMaps(
                self.pano_alpha_min, self.pano_alpha_max)
            self.parent.show_to_window()

    def change_panorama_fov(self):
        """
        Change the panorama view with change the field of view.

        Returns:

        """
        self.pano_alpha_min = int(self.parent.ui.min_pano.text())
        self.pano_alpha_max = int(self.parent.ui.max_pano.text())
        # self.rho = self.parent.moildev.getRhoFromAlpha(self.pano_alpha_min)
        self.process_to_panorama()


