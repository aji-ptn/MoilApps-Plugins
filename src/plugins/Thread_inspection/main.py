#######################################################
# the application for implementation MoilSDK
# writen by Haryanto
# email: M07158031@o365.mcut.edu.twsour
#######################################################
import plugin
from .main_controller import *


class Internal_Thread_Inspection(plugin.Plugin):
    def __init__(self):
        """
        The class that represent the plugins application, class name will be read as the name of application.
        """
        super().__init__()
        self.description = "This is default application"

    def perform_operation(self, argument):
        """
        The main application will execute this function when click button open.

        Args:
            argument (): is the object widget from main application class.

        Returns:
            Will show the window of application.

        """
        apps = Controller(argument)
        apps.show()