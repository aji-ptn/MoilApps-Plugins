from moildevApps.base_plugin import Plugin
from .controller.controller import *


class Surveillance_apps(Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from surveillance"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()