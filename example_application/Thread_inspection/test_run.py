from controller import *
import sys


def main():
    apps = QtWidgets.QApplication(sys.argv)
    window = Controller("none")
    window.show()
    sys.exit(apps.exec_())


if __name__ == '__main__':
    main()