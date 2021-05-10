import cv2


class Anypoint_View(object):
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.connect_event()

    def connect_event(self):
        self.parent.ui.btn_anypoint.clicked.connect(self.process_to_anypoint)

    def process_to_anypoint(self):
        """This function is to process the image and show on anypoint mode.
        """
        image = self.parent.moildev.anypoint(self.parent.image, 0, 0, 4, 2)
        self.parent.show_image.show_result_image(image, self.parent.width_result_image)
