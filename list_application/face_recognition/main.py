import base_plugin
from .controller.controller import *


class Face_Recognition(base_plugin.Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from Face recognition"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()