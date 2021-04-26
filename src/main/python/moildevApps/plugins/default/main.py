#######################################################
# the application for implementation MoilSDK
# writen by Haryanto
# email: M07158031@o365.mcut.edu.twsour 
#######################################################
from moildevApps.base_plugin import Plugin
from .Ui_Controller import *


class Default_apps(Plugin):
    def __init__(self):
        super().__init__()
        self.description = "this is from internal thread inspection"

    def perform_operation(self, argument):
        self.w = Controller(argument)
        self.w.show()
