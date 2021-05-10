
class PanoramaView(object):
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.connect_event()

    def connect_event(self):
        self.parent.ui.btn_panorama.clicked.connect(self.process_to_panorama)

    def process_to_panorama(self):
        if self.parent.image is None:
            pass
        else:
            if self.parent.image is None:
                pass
            else:
                self.parent.ui.normal_mode = False
                self.parent.ui.frame_anypoint.hide()
                self.parent.ui.frame_navigator.hide()
                self.parent.ui.frame_panorama.show()
