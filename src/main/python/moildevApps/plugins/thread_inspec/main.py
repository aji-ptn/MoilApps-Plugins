#######################################################
# the application for implementation MoilSDK
# writen by Haryanto
# email: M07158031@o365.mcut.edu.twsour
#######################################################
from moildevApps.base_plugin import Plugin
from .controller.controller import *


class Internal_Thread_Inspection(Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from internal thread inspection"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()
