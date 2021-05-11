
class PanoramaView(object):
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.pano_alpha_min = 40
        self.pano_alpha_max = 100
        self.connect_event()

    def connect_event(self):
        self.parent.ui.btn_panorama.clicked.connect(self.process_to_panorama)

    def process_to_panorama(self):
        if self.parent.image is not None:
            self.parent.normal_mode = False
            self.parent.ui.frame_anypoint.hide()
            self.parent.ui.frame_navigator.hide()
            self.parent.ui.frame_panorama.show()
            self.parent.mapX, self.parent.mapY, = self.parent.moildev.getPanoramaMaps(
                self.pano_alpha_min, self.pano_alpha_max)
            self.parent.show_to_window()
