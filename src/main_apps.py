import os
import shutil
from PyQt5 import QtGui, QtWidgets
from Ui_app_moildev import Ui_MainWindow
from application import Application


def dir_copy(srcpath, dstdir):
    """
    Function for copy directory.

    Args:
        srcpath (): source path or original path folder
        dstdir (): destination directory.

    Returns:
        Copy file to destination directory.

    """

    dirname = os.path.basename(srcpath)
    dstpath = os.path.join(dstdir, dirname)
    shutil.copytree(srcpath, dstpath)


def open_help():
    """
    Open help window.

    Returns:
        Show prompt help.
    """
    msgbox = QtWidgets.QMessageBox()
    msgbox.setWindowTitle("Help !!")
    msgbox.setText(
        "Moildev-Apps\n\n"
        "Moildev-Apps is software to process fisheye "
        "image with the result panorama view and Anypoint"
        " view. \n\nThe panoramic view may present a horizontal"
        "view in a specific immersed environment to meet the"
        "common human visual perception, while the Anypoint"
        "view is an image that has been undistorted in a certain"
        "area according to the input coordinates."
        "\n\nMore reference about Moildev, contact us\n\n")
    msgbox.setIconPixmap(QtGui.QPixmap('./images/moildev.png'))
    msgbox.exec()


def get_password():
    paswd, ok = QtWidgets.QInputDialog.getText(None, "Authentication", "Sudo Password?",
                                               QtWidgets.QLineEdit.Password)
    if ok and paswd != '':
        return paswd


class ControllerMainApps(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """
        The controller class to control UI MainWindow.

        Args:
            parent ():
        """
        super(ControllerMainApps, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.plugins = Application("plugins")
        self.connect_button()

    def connect_button(self):
        """
        Connect button to the execute function.

        Returns:

        """
        self.ui.comboBox.addItems(self.plugins.name_application)
        self.ui.Open_btn.clicked.connect(self.open_application)
        self.ui.Delete_btn.clicked.connect(self.delete_apps)
        self.ui.add_apps.clicked.connect(self.add_application)
        self.ui.btn_Exit.clicked.connect(self.exit)
        self.ui.pushButton.clicked.connect(open_help)

    def open_application(self):
        """
        Open application depend on selected application available on comboBox.

        Returns:
            Will hide the main apps window and show the selection application.
        """
        __index = self.ui.comboBox.currentIndex()
        self.plugins.application(self, __index)
        self.hide()

    def delete_apps(self):
        """
        Delete selected application from the list.

        Returns:
            None.
        """
        __index = self.ui.comboBox.currentIndex()
        name = self.plugins.name_application[__index]
        path = self.plugins.path_folder[__index]
        path = path.split(".")[1]
        if path == "default":
            QtWidgets.QMessageBox.information(
                self, "Information", "Default apps can't delete !!")
        else:
            path = "./plugins/" + path
            reply = QtWidgets.QMessageBox.question(
                self,
                'Message',
                "Are you sure want to delete \n" +
                name +
                " application ?\n",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                shutil.rmtree(path, ignore_errors=True)
                self.plugins.reload_plugins()
                new_list = self.plugins.name_application
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(new_list)
            else:
                pass

    def add_application(self):
        """
        Add application plugin to system.

        Returns:
            None.
        """
        dir_plugin = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Application Folder')
        if dir_plugin:
            paswd = get_password()
            print(paswd)
            # os.system("echo " + paswd + "| sudo -S chown $USER /opt/Moildev/plugins/")
            original = dir_plugin
            target = 'plugins/'
            dir_copy(original, target)
            self.plugins.reload_plugins()
            new_list = self.plugins.name_application
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(new_list)

    def exit(self):
        """
        Exit main window function, Its will connect to close function which is will ask question before close.

        Returns:
            None.
        """
        self.close()


def main():
    """
    Create instance Main window to create the main window of Application.

    Returns:
        None.
    """
    import sys
    apps = QtWidgets.QApplication(sys.argv)
    window = ControllerMainApps()
    window.show()
    sys.exit(apps.exec_())


if __name__ == '__main__':
    main()
