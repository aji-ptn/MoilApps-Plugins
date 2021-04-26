#######################################################
# the application for implementation MoilSDK
# writen by Haryanto
# email: M07158031@o365.mcut.edu.tw
#######################################################
from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property
from PyQt5 import QtGui
from moildevApps.app_moildev_UI import Ui_MainWindow
from moildevApps.controller import ControllerMainApps
from moildevApps.Moutils import Moutils
import sys
import numpy as np
import cv2


class AppContext(ApplicationContext):
    """The ApplicationContext provides a central location for initialising and storing these components, as well as
    providing access to some core fbs features. The ApplicationContext object also creates and holds a reference to a
    global QApplication object
    """

    def run(self):
        """The function to run Application user interface(UI)"""
        super(AppContext, self).__init__()
        control = ControllerMainApps(self.main_window)
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def main_window(self):
        return Ui_MainWindow(self)

    @cached_property
    def icon_home(self):
        return QtGui.QImage(self.get_resource("images/home.png"))

    @cached_property
    def icon_moildev(self):
        return QtGui.QImage(self.get_resource("images/moildev.png"))

    @cached_property
    def icon_moildev2(self):
        return QtGui.QImage(self.get_resource("images/moildev2.png"))

    """Mode------------------------------------------------------------------------"""
    @cached_property
    def icon_any(self):
        return QtGui.QImage(self.get_resource("images/any.png"))

    @cached_property
    def icon_pano(self):
        return QtGui.QImage(self.get_resource("images/pano.png"))

    @cached_property
    def icon_panorama(self):
        return QtGui.QImage(self.get_resource("images/icon-panorama.png"))

    @cached_property
    def icon_anypoint(self):
        return QtGui.QImage(self.get_resource("images/icon-anypoint.png"))

    """ up right left down ---------------------------------------------------------"""
    @cached_property
    def icon_up(self):
        return QtGui.QImage(self.get_resource("images/up.png"))

    @cached_property
    def icon_right(self):
        return QtGui.QImage(self.get_resource("images/right.png"))

    @cached_property
    def icon_left(self):
        return QtGui.QImage(self.get_resource("images/left.png"))

    @cached_property
    def icon_down(self):
        return QtGui.QImage(self.get_resource("images/down.png"))

    @cached_property
    def icon_center(self):
        return QtGui.QImage(self.get_resource("images/Center.png"))

    """Source-----------------------------------------------------------------------"""
    @cached_property
    def icon_open_image(self):
        return QtGui.QImage(self.get_resource("images/open_image.png"))

    @cached_property
    def icon_open_video(self):
        return QtGui.QImage(self.get_resource("images/open_video.png"))

    @cached_property
    def icon_open_cam(self):
        return QtGui.QImage(self.get_resource("images/open_cam.png"))

    @cached_property
    def icon_cam_live(self):
        return QtGui.QImage(self.get_resource("images/cam_live.png"))

    """Video Player-----------------------------------------------------------------"""
    @cached_property
    def icon_stop(self):
        return QtGui.QImage(self.get_resource("images/icon_stop.png"))

    @cached_property
    def icon_play(self):
        return QtGui.QImage(self.get_resource("images/play.png"))

    @cached_property
    def icon_pause(self):
        return QtGui.QImage(self.get_resource("images/pause.png"))

    @cached_property
    def icon_rewind(self):
        return QtGui.QImage(self.get_resource("images/rewind.png"))

    @cached_property
    def icon_forward(self):
        return QtGui.QImage(self.get_resource("images/forward.png"))

    @cached_property
    def stop(self):
        return QtGui.QImage(self.get_resource("images/stop.png"))

    """Rotate------------------------------------------------------------------------"""
    @cached_property
    def icon_rotate_left(self):
        return QtGui.QImage(self.get_resource("images/rotate-left.png"))

    @cached_property
    def icon_rotate_right(self):
        return QtGui.QImage(self.get_resource("images/rotate-right.png"))

    """Zoom--------------------------------------------------------------------------"""
    @cached_property
    def icon_zoom_in(self):
        return QtGui.QImage(self.get_resource("images/zoom-in.png"))

    @cached_property
    def icon_zoom_out(self):
        return QtGui.QImage(self.get_resource("images/zoom-out.png"))

    """save--------------------------------------------------------------------------"""
    @cached_property
    def icon_save_camera(self):
        return QtGui.QImage(self.get_resource("images/save_camera.png"))

    @cached_property
    def icon_video_record(self):
        return QtGui.QImage(self.get_resource("images/video-record.png"))

    @cached_property
    def icon_rec_stop(self):
        return QtGui.QImage(self.get_resource("images/rec_stop.png"))

    @cached_property
    def icon_rec(self):
        return QtGui.QImage(self.get_resource("images/rec.png"))

    @cached_property
    def icon_record(self):
        return QtGui.QImage(self.get_resource("images/record.png"))

    """info and  help-----------------------------------------------------------------"""
    @cached_property
    def icon_information(self):
        return QtGui.QImage(self.get_resource("images/icon_information.png"))

    @cached_property
    def icon_info(self):
        return QtGui.QImage(self.get_resource("images/icon_info.png"))

    @cached_property
    def icon_help(self):
        return QtGui.QImage(self.get_resource("images/icon_help.png"))

    """Quit and shutdown--------------------------------------------------------------"""
    @cached_property
    def icon_quit(self):
        return QtGui.QImage(self.get_resource("images/Quit.png"))

    @cached_property
    def icon_shutdown(self):
        return QtGui.QImage(self.get_resource("images/shutdown.png"))


if __name__ == "__main__":
    apps = AppContext()
    exit_code = apps.run()
    sys.exit(exit_code)
