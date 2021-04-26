import os
import shutil
from PyQt5 import QtGui, QtWidgets
from .application import Application
import platform


class ControllerMainApps(QtWidgets.QMainWindow):
    """The controller class to control UI MainWindow
    """

    def __init__(self, ui_mainwindow):
        """construction method
        """
        super(ControllerMainApps, self).__init__()
        self.ui = ui_mainwindow
        self.plugins = Application("plugins")
        self.ui.comboBox.addItems(self.plugins.name_application)
        self.ui.Open_btn.clicked.connect(self.open_application)
        self.ui.Delete_btn.clicked.connect(self.delete_apps)
        self.ui.install_mor_application.clicked.connect(self.add_application_plugin)
        self.ui.btn_Exit.clicked.connect(self.exit)
        self.ui.pushButton.clicked.connect(self.open_help)

    def open_application(self):
        """Open application depend on selected application available on comboBox
        """
        __index = self.ui.comboBox.currentIndex()
        self.plugins.application(self.ui, __index)
        self.ui.hide()

    def delete_apps(self):
        __index = self.ui.comboBox.currentIndex()
        name = self.plugins.name_application[__index]
        path = self.plugins.path_folder[__index]
        path = path.split(".")[1]
        if path == "default":
            QtWidgets.QMessageBox.information(None, "Information", "Default apps can't delete !!")
        else:
            path = "/opt/Moildev/plugins/" + path
            reply = QtWidgets.QMessageBox.question(None, 'Message',
                                                   "Are you sure want to delete \n" + name + " application ?\n",
                                                   QtWidgets.QMessageBox.Yes |
                                                   QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                shutil.rmtree(path, ignore_errors=True)
                self.plugins.reload_plugins()
                new_list = self.plugins.name_application
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(new_list)
            else:
                pass

    def add_application_plugin(self):
        """add application plugin to system
        """
        if platform.system() == "Windows":
            pass
        else:
            dir_plugin = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Application')
            if dir_plugin:
                paswd = self.getPassword()
                os.system("echo " + paswd + "| sudo -S chown $USER /opt/Moildev/plugins/")
                target = '/opt/Moildev/plugins/'
                self.dir_copy(dir_plugin, target)
                self.plugins.reload_plugins()
                new_list = self.plugins.name_application
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(new_list)

    def open_help(self):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle("Help !!")
        msgbox.setText("Moildev-Apps\n\n"
                       "Moildev-Apps is software to process fisheye "
                       "image with the result panorama view and Anypoint"
                       " view. \n\nThe panoramic view may present a horizontal"
                       "view in a specific immersed environment to meet the"
                       "common human visual perception, while the Anypoint"
                       "view is an image that has been undistorted in a certain"
                       "area according to the input coordinates."
                       "\n\nMore reference about Moildev, contact us\n\n")
        msgbox.setIconPixmap(QtGui.QPixmap('./assets/128.png'))
        msgbox.exec()

    def dir_copy(self, srcpath, dstdir):
        dirname = os.path.basename(srcpath)
        dstpath = os.path.join(dstdir, dirname)
        shutil.copytree(srcpath, dstpath)

    def getPassword(self):
        paswd, ok = QtWidgets.QInputDialog.getText(None, "Authentication", "Sudo Password?",
                                                   QtWidgets.QLineEdit.Password)
        if ok and paswd != '':
            return paswd

    def exit(self):
        """exit main window
        """
        self.ui.close()