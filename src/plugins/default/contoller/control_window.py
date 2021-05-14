from PyQt5 import QtCore


class ViewWindow(object):
    def __init__(self, MainWindow):
        """
        Initial Class to control the window in user interface.

        Args:
            MainWindow (): Is the parent class to access the user interface widget in this application.
        """
        self.parent = MainWindow
        self.connectToButton()

    def connectToButton(self):
        """
        The method for connect the function with UI event

        Returns:
            The event will connect to function.

        """
        self.parent.ui.actionMaximized.triggered.connect(self.showMaximized)
        self.parent.ui.actionMinimized.triggered.connect(self.show_Minimized)
        self.parent.ui.actionHide_Toolbar.triggered.connect(self.hideToolbar)

    def showMaximized(self):
        """
        To showing the result image in maximize window. it will hide the original label image.

        Returns:
            showing image on Maximum windows.
        """
        if self.parent.image is None:
            pass
        else:
            self.parent.ui.scrollArea_2.hide()
            self.parent.width_img = 2000
            self.parent.ui.scrollArea_3.setMaximumSize(
                QtCore.QSize(self.parent.width_img, 16777215))
            self.parent.showing.view_result(self.parent.image)
            self.maxi = True

    def show_Minimized(self):
        """
        To showing the result image in minimized window. it will hide the original label image.

        Returns:
            Showing the minimum windows.
        """
        if self.parent.image is None:
            pass
        else:
            self.parent.ui.scrollArea_2.show()
            self.parent.width_img = 1400
            self.parent.ui.scrollArea_3.setMaximumSize(
                QtCore.QSize(self.parent.width_img, 16777215))
            self.parent.showing.view_result(self.parent.image)
            self.maxi = False

    def hideToolbar(self):
        """
        Hide the toolbar from main window.

        Returns:
            toolbar hidden.
        """
        if self.parent.ui.actionHide_Toolbar.isChecked():
            self.parent.ui.toolBar.hide()
        else:
            self.parent.ui.toolBar.show()
