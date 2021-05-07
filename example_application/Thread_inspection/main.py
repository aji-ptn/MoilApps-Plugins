import base_plugin
from .controller.controller import *


class Internal_Thread_Inspection(base_plugin.Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from internal thread inspection"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()
