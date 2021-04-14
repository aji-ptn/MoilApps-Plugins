import base_plugin
from .controller.controller import *


class Surveillance_apps(base_plugin.Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from surveillance"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()