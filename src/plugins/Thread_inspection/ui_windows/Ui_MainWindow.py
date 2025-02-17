# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'from_figma.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 917)
        MainWindow.showMaximized()
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(60, 60))
        self.frame_2.setStyleSheet("background-color: #71D1BA;   \n"
                                   "border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_Home = QtWidgets.QPushButton(self.frame_2)
        self.btn_Home.setGeometry(QtCore.QRect(5, 5, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Home.sizePolicy().hasHeightForWidth())
        self.btn_Home.setSizePolicy(sizePolicy)
        self.btn_Home.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_Home.setToolTipDuration(-1)
        self.btn_Home.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("images/home.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Home.setIcon(icon)
        self.btn_Home.setIconSize(QtCore.QSize(40, 40))
        self.btn_Home.setObjectName("btn_Home")
        self.verticalLayout_4.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                 "border-radius: 5px;\n"
                                 "background-color: #71D1BA; ")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.frame_feature = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_feature.sizePolicy().hasHeightForWidth())
        self.frame_feature.setSizePolicy(sizePolicy)
        self.frame_feature.setMinimumSize(QtCore.QSize(60, 160))
        self.frame_feature.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                         "border-radius: 10px;\n"
                                         "background-color: #71D1BA; ")
        self.frame_feature.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_feature.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_feature.setObjectName("frame_feature")
        self.btn_normal = QtWidgets.QPushButton(self.frame_feature)
        self.btn_normal.setGeometry(QtCore.QRect(5, 10, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_normal.sizePolicy().hasHeightForWidth())
        self.btn_normal.setSizePolicy(sizePolicy)
        self.btn_normal.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.btn_normal.setFont(font)
        self.btn_normal.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_normal.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("images/default.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_normal.setIcon(icon1)
        self.btn_normal.setIconSize(QtCore.QSize(40, 40))
        self.btn_normal.setCheckable(True)
        self.btn_normal.setChecked(False)
        self.btn_normal.setObjectName("btn_normal")
        self.btn_anypoint = QtWidgets.QPushButton(self.frame_feature)
        self.btn_anypoint.setGeometry(QtCore.QRect(5, 60, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_anypoint.sizePolicy().hasHeightForWidth())
        self.btn_anypoint.setSizePolicy(sizePolicy)
        self.btn_anypoint.setMinimumSize(QtCore.QSize(30, 40))
        self.btn_anypoint.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_anypoint.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("images/icon-anypoint.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_anypoint.setIcon(icon2)
        self.btn_anypoint.setIconSize(QtCore.QSize(40, 40))
        self.btn_anypoint.setCheckable(False)
        self.btn_anypoint.setObjectName("btn_anypoint")
        self.btn_panorama = QtWidgets.QPushButton(self.frame_feature)
        self.btn_panorama.setGeometry(QtCore.QRect(5, 110, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_panorama.sizePolicy().hasHeightForWidth())
        self.btn_panorama.setSizePolicy(sizePolicy)
        self.btn_panorama.setMinimumSize(QtCore.QSize(30, 40))
        self.btn_panorama.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_panorama.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("images/icon-panorama.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_panorama.setIcon(icon3)
        self.btn_panorama.setIconSize(QtCore.QSize(40, 40))
        self.btn_panorama.setCheckable(False)
        self.btn_panorama.setObjectName("btn_panorama")
        self.verticalLayout_4.addWidget(self.frame_feature)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                   "border-radius: 5px;\n"
                                   "background-color: #71D1BA; ")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(60, 160))
        self.frame.setStyleSheet("background-color: #71D1BA;   \n"
                                 "border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_show_help = QtWidgets.QPushButton(self.frame)
        self.btn_show_help.setGeometry(QtCore.QRect(5, 110, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_show_help.sizePolicy().hasHeightForWidth())
        self.btn_show_help.setSizePolicy(sizePolicy)
        self.btn_show_help.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_show_help.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_show_help.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("images/icons_help.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_show_help.setIcon(icon4)
        self.btn_show_help.setIconSize(QtCore.QSize(40, 40))
        self.btn_show_help.setObjectName("btn_show_help")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setGeometry(QtCore.QRect(5, 10, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_18.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.pushButton_18.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("images/moildev.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon5)
        self.pushButton_18.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_29 = QtWidgets.QPushButton(self.frame)
        self.pushButton_29.setGeometry(QtCore.QRect(5, 60, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMinimumSize(QtCore.QSize(30, 40))
        self.pushButton_29.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.pushButton_29.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("images/information.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.pushButton_29.setIcon(icon6)
        self.pushButton_29.setIconSize(QtCore.QSize(30, 40))
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout_4.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(
            10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_Open_Source = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_Open_Source.sizePolicy().hasHeightForWidth())
        self.frame_Open_Source.setSizePolicy(sizePolicy)
        self.frame_Open_Source.setMinimumSize(QtCore.QSize(170, 50))
        self.frame_Open_Source.setStyleSheet("background-color: #71D1BA;   \n"
                                             "border-radius: 10px;")
        self.frame_Open_Source.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Open_Source.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Open_Source.setObjectName("frame_Open_Source")
        self.btn_Open_Image = QtWidgets.QPushButton(self.frame_Open_Source)
        self.btn_Open_Image.setGeometry(QtCore.QRect(10, 5, 38, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Open_Image.sizePolicy().hasHeightForWidth())
        self.btn_Open_Image.setSizePolicy(sizePolicy)
        self.btn_Open_Image.setMinimumSize(QtCore.QSize(35, 30))
        self.btn_Open_Image.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_Open_Image.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Open_Image.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap("images/open_image_out.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Open_Image.setIcon(icon7)
        self.btn_Open_Image.setIconSize(QtCore.QSize(40, 40))
        self.btn_Open_Image.setCheckable(False)
        self.btn_Open_Image.setObjectName("btn_Open_Image")
        self.btn_Open_Video = QtWidgets.QPushButton(self.frame_Open_Source)
        self.btn_Open_Video.setGeometry(QtCore.QRect(60, 5, 38, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Open_Video.sizePolicy().hasHeightForWidth())
        self.btn_Open_Video.setSizePolicy(sizePolicy)
        self.btn_Open_Video.setMinimumSize(QtCore.QSize(38, 30))
        self.btn_Open_Video.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Open_Video.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap("images/video.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Open_Video.setIcon(icon8)
        self.btn_Open_Video.setIconSize(QtCore.QSize(40, 40))
        self.btn_Open_Video.setObjectName("btn_Open_Video")
        self.btn_Open_Cam = QtWidgets.QPushButton(self.frame_Open_Source)
        self.btn_Open_Cam.setGeometry(QtCore.QRect(110, 5, 50, 40))
        self.btn_Open_Cam.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Open_Cam.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap("images/icons8-video-call-96.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Open_Cam.setIcon(icon9)
        self.btn_Open_Cam.setIconSize(QtCore.QSize(40, 40))
        self.btn_Open_Cam.setObjectName("btn_Open_Cam")
        self.horizontalLayout_3.addWidget(self.frame_Open_Source)
        self.frame_rotate = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_rotate.sizePolicy().hasHeightForWidth())
        self.frame_rotate.setSizePolicy(sizePolicy)
        self.frame_rotate.setMinimumSize(QtCore.QSize(110, 50))
        self.frame_rotate.setStyleSheet("background-color: #71D1BA;   \n"
                                        "border-radius: 10px;")
        self.frame_rotate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rotate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rotate.setObjectName("frame_rotate")
        self.btn_Rotate_Left = QtWidgets.QPushButton(self.frame_rotate)
        self.btn_Rotate_Left.setGeometry(QtCore.QRect(10, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Rotate_Left.sizePolicy().hasHeightForWidth())
        self.btn_Rotate_Left.setSizePolicy(sizePolicy)
        self.btn_Rotate_Left.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Rotate_Left.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Rotate_Left.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap("images/rotate-left.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Rotate_Left.setIcon(icon10)
        self.btn_Rotate_Left.setIconSize(QtCore.QSize(35, 35))
        self.btn_Rotate_Left.setObjectName("btn_Rotate_Left")
        self.btn_Rotate_Right = QtWidgets.QPushButton(self.frame_rotate)
        self.btn_Rotate_Right.setGeometry(QtCore.QRect(60, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Rotate_Right.sizePolicy().hasHeightForWidth())
        self.btn_Rotate_Right.setSizePolicy(sizePolicy)
        self.btn_Rotate_Right.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Rotate_Right.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Rotate_Right.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap("images/rotate-right.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Rotate_Right.setIcon(icon11)
        self.btn_Rotate_Right.setIconSize(QtCore.QSize(35, 35))
        self.btn_Rotate_Right.setObjectName("btn_Rotate_Right")
        self.horizontalLayout_3.addWidget(self.frame_rotate)
        self.frame_zoom = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_zoom.sizePolicy().hasHeightForWidth())
        self.frame_zoom.setSizePolicy(sizePolicy)
        self.frame_zoom.setMinimumSize(QtCore.QSize(110, 50))
        self.frame_zoom.setStyleSheet("background-color: #71D1BA;   \n"
                                      "border-radius: 10px;")
        self.frame_zoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_zoom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_zoom.setObjectName("frame_zoom")
        self.btn_Zoom_in = QtWidgets.QPushButton(self.frame_zoom)
        self.btn_Zoom_in.setGeometry(QtCore.QRect(60, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Zoom_in.sizePolicy().hasHeightForWidth())
        self.btn_Zoom_in.setSizePolicy(sizePolicy)
        self.btn_Zoom_in.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Zoom_in.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Zoom_in.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap("images/zoom-in.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Zoom_in.setIcon(icon12)
        self.btn_Zoom_in.setIconSize(QtCore.QSize(40, 40))
        self.btn_Zoom_in.setObjectName("btn_Zoom_in")
        self.btn_Zoom_out = QtWidgets.QPushButton(self.frame_zoom)
        self.btn_Zoom_out.setGeometry(QtCore.QRect(10, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Zoom_out.sizePolicy().hasHeightForWidth())
        self.btn_Zoom_out.setSizePolicy(sizePolicy)
        self.btn_Zoom_out.setMinimumSize(QtCore.QSize(40, 30))
        self.btn_Zoom_out.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Zoom_out.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap("images/zoom-out.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Zoom_out.setIcon(icon13)
        self.btn_Zoom_out.setIconSize(QtCore.QSize(40, 40))
        self.btn_Zoom_out.setObjectName("btn_Zoom_out")
        self.horizontalLayout_3.addWidget(self.frame_zoom)
        self.frame_save = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_save.sizePolicy().hasHeightForWidth())
        self.frame_save.setSizePolicy(sizePolicy)
        self.frame_save.setMinimumSize(QtCore.QSize(125, 50))
        self.frame_save.setStyleSheet("background-color: #71D1BA;   \n"
                                      "border-radius: 10px;")
        self.frame_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_save.setObjectName("frame_save")
        self.btn_Save_Image = QtWidgets.QPushButton(self.frame_save)
        self.btn_Save_Image.setGeometry(QtCore.QRect(10, 5, 45, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Save_Image.sizePolicy().hasHeightForWidth())
        self.btn_Save_Image.setSizePolicy(sizePolicy)
        self.btn_Save_Image.setMinimumSize(QtCore.QSize(45, 30))
        self.btn_Save_Image.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Save_Image.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap("images/camera.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Save_Image.setIcon(icon14)
        self.btn_Save_Image.setIconSize(QtCore.QSize(40, 40))
        self.btn_Save_Image.setObjectName("btn_Save_Image")
        self.btn_Record_video = QtWidgets.QPushButton(self.frame_save)
        self.btn_Record_video.setGeometry(QtCore.QRect(65, 5, 50, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Record_video.sizePolicy().hasHeightForWidth())
        self.btn_Record_video.setSizePolicy(sizePolicy)
        self.btn_Record_video.setMinimumSize(QtCore.QSize(50, 40))
        self.btn_Record_video.setStyleSheet(
            "QPushButton{ background-color :  rgb(211, 215, 207);}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_Record_video.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(
            QtGui.QPixmap("images/video-record.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Record_video.setIcon(icon15)
        self.btn_Record_video.setIconSize(QtCore.QSize(50, 40))
        self.btn_Record_video.setObjectName("btn_Record_video")
        self.horizontalLayout_3.addWidget(self.frame_save)

        self.frame_ctrl_axis = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_ctrl_axis.sizePolicy().hasHeightForWidth())
        self.frame_ctrl_axis.setSizePolicy(sizePolicy)
        self.frame_ctrl_axis.setMinimumSize(QtCore.QSize(65, 50))
        self.frame_ctrl_axis.setStyleSheet("background-color: #71D1BA;   \n"
                                           "border-radius: 10px;")
        self.frame_ctrl_axis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ctrl_axis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ctrl_axis.setObjectName("frame_ctrl_axis")
        self.btn_ctrl_axis = QtWidgets.QPushButton(self.frame_ctrl_axis)
        self.btn_ctrl_axis.setGeometry(QtCore.QRect(10, 5, 45, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ctrl_axis.sizePolicy().hasHeightForWidth())
        self.btn_ctrl_axis.setSizePolicy(sizePolicy)
        self.btn_ctrl_axis.setMinimumSize(QtCore.QSize(45, 30))
        self.btn_ctrl_axis.setStyleSheet("QPushButton{ background-color :  rgb(211, 215, 207);}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_ctrl_axis.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/axis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ctrl_axis.setIcon(icon16)
        self.btn_ctrl_axis.setIconSize(QtCore.QSize(40, 35))
        self.btn_ctrl_axis.setObjectName("btn_ctrl_axis")
        self.horizontalLayout_3.addWidget(self.frame_ctrl_axis)


        self.label_Application = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_Application.setFont(font)
        self.label_Application.setStyleSheet("border-radius: 10px;\n"
                                             "background-color: #71AED1;   ")
        self.label_Application.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Application.setObjectName("label_Application")
        self.horizontalLayout_3.addWidget(self.label_Application)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_5.setStyleSheet("background-color: #71D1BA;   \n"
                                   "border-radius: 10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.btn_Quit = QtWidgets.QPushButton(self.frame_5)
        self.btn_Quit.setGeometry(QtCore.QRect(5, 5, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_Quit.sizePolicy().hasHeightForWidth())
        self.btn_Quit.setSizePolicy(sizePolicy)
        self.btn_Quit.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_Quit.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;\n"
            "border-radius: 10px;")
        self.btn_Quit.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(
            QtGui.QPixmap("images/shutdown.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_Quit.setIcon(icon16)
        self.btn_Quit.setIconSize(QtCore.QSize(40, 40))
        self.btn_Quit.setObjectName("btn_Quit")
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 1450, 711))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_Result_Image = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_Result_Image.sizePolicy().hasHeightForWidth())
        self.label_Result_Image.setSizePolicy(sizePolicy)
        self.label_Result_Image.setMinimumSize(QtCore.QSize(1200, 400))
        self.label_Result_Image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Result_Image.setText("")
        self.label_Result_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Result_Image.setObjectName("label_Result_Image")

        self.frame_navigator = QtWidgets.QFrame(self.scrollArea)
        self.frame_navigator.setGeometry(QtCore.QRect(120, 140, 160, 290))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_navigator.sizePolicy().hasHeightForWidth())
        self.frame_navigator.setSizePolicy(sizePolicy)
        self.frame_navigator.setMinimumSize(QtCore.QSize(160, 160))
        self.frame_navigator.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_navigator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_navigator.setLineWidth(0)
        self.frame_navigator.setObjectName("frame_navigator")
        self.frame_20 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_20.setGeometry(QtCore.QRect(60, 10, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_20.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.btn_Up_View = QtWidgets.QPushButton(self.frame_20)
        self.btn_Up_View.setGeometry(QtCore.QRect(0, 0, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Up_View.sizePolicy().hasHeightForWidth())
        self.btn_Up_View.setSizePolicy(sizePolicy)
        self.btn_Up_View.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_Up_View.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                       "QPushButton::pressed{ background-color : #71AED1; }\n"
                                       "border-radius: 10px;")
        self.btn_Up_View.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Up_View.setIcon(icon)
        self.btn_Up_View.setIconSize(QtCore.QSize(40, 40))
        self.btn_Up_View.setObjectName("btn_Up_View")
        self.frame_21 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_21.setGeometry(QtCore.QRect(110, 60, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_21.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.btn_Right_view = QtWidgets.QPushButton(self.frame_21)
        self.btn_Right_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_Right_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                          "QPushButton::pressed{ background-color : #71AED1; }\n"
                                          "border-radius: 10px;")
        self.btn_Right_view.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Right_view.setIcon(icon1)
        self.btn_Right_view.setIconSize(QtCore.QSize(40, 40))
        self.btn_Right_view.setObjectName("btn_Right_view")
        self.frame_22 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_22.setGeometry(QtCore.QRect(10, 60, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_22.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.btn_left_view = QtWidgets.QPushButton(self.frame_22)
        self.btn_left_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_left_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_left_view.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_left_view.setIcon(icon2)
        self.btn_left_view.setIconSize(QtCore.QSize(40, 40))
        self.btn_left_view.setObjectName("btn_left_view")
        self.frame_23 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_23.setGeometry(QtCore.QRect(60, 110, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_23.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.btn_Down_view = QtWidgets.QPushButton(self.frame_23)
        self.btn_Down_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.btn_Down_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                         "QPushButton::pressed{ background-color : #71AED1; }\n"
                                         "border-radius: 10px;")
        self.btn_Down_view.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Down_view.setIcon(icon3)
        self.btn_Down_view.setIconSize(QtCore.QSize(40, 40))
        self.btn_Down_view.setObjectName("btn_Down_view")
        self.frame_24 = QtWidgets.QFrame(self.frame_navigator)
        self.frame_24.setGeometry(QtCore.QRect(60, 60, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_24.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.btn_center_view = QtWidgets.QPushButton(self.frame_24)
        self.btn_center_view.setGeometry(QtCore.QRect(0, 0, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_center_view.sizePolicy().hasHeightForWidth())
        self.btn_center_view.setSizePolicy(sizePolicy)
        self.btn_center_view.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_center_view.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                           "QPushButton::pressed{ background-color : #71AED1; }\n"
                                           "border-radius: 10px;")
        self.btn_center_view.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/C.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_center_view.setIcon(icon4)
        self.btn_center_view.setIconSize(QtCore.QSize(30, 40))
        self.btn_center_view.setObjectName("btn_center_view")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_navigator)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 160, 161, 27))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_mode = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.label_mode.setFont(font)
        self.label_mode.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_mode.setObjectName("label_mode")
        self.horizontalLayout_4.addWidget(self.label_mode)
        self.radio_btn_mode_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radio_btn_mode_1.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.radio_btn_mode_1.setFont(font)
        self.radio_btn_mode_1.setObjectName("radio_btn_mode_1")
        self.horizontalLayout_4.addWidget(self.radio_btn_mode_1)
        self.radio_btn_mode_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        self.radio_btn_mode_2.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.radio_btn_mode_2.setFont(font)
        self.radio_btn_mode_2.setObjectName("radio_btn_mode_2")
        self.horizontalLayout_4.addWidget(self.radio_btn_mode_2)
        self.alpha_2 = QtWidgets.QLabel(self.frame_navigator)
        self.alpha_2.setGeometry(QtCore.QRect(0, 189, 50, 27))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.alpha_2.setFont(font)
        self.alpha_2.setObjectName("alpha_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_navigator)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 250, 35, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(35, 0))
        self.pushButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icon_help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.oke_alpha_2 = QtWidgets.QPushButton(self.frame_navigator)
        self.oke_alpha_2.setGeometry(QtCore.QRect(120, 190, 35, 50))
        self.oke_alpha_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/oke.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oke_alpha_2.setIcon(icon6)
        self.oke_alpha_2.setObjectName("oke_alpha_2")
        self.anypoint_zoom_2 = QtWidgets.QDoubleSpinBox(self.frame_navigator)
        self.anypoint_zoom_2.setGeometry(QtCore.QRect(55, 250, 55, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.anypoint_zoom_2.sizePolicy().hasHeightForWidth())
        self.anypoint_zoom_2.setSizePolicy(sizePolicy)
        self.anypoint_zoom_2.setDecimals(1)
        self.anypoint_zoom_2.setMaximum(14.0)
        self.anypoint_zoom_2.setSingleStep(0.1)
        self.anypoint_zoom_2.setObjectName("anypoint_zoom_2")
        self.beta_2 = QtWidgets.QLabel(self.frame_navigator)
        self.beta_2.setGeometry(QtCore.QRect(0, 219, 50, 27))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.beta_2.setFont(font)
        self.beta_2.setObjectName("beta_2")
        self.lineedit_alpha_2 = QtWidgets.QLineEdit(self.frame_navigator)
        self.lineedit_alpha_2.setGeometry(QtCore.QRect(55, 190, 55, 25))
        self.lineedit_alpha_2.setObjectName("lineedit_alpha_2")
        self.lineedit_beta_2 = QtWidgets.QLineEdit(self.frame_navigator)
        self.lineedit_beta_2.setGeometry(QtCore.QRect(55, 220, 55, 25))
        self.lineedit_beta_2.setObjectName("lineedit_beta_2")

        # self.oke_beta_2 = QtWidgets.QPushButton(self.frame_navigator)
        # self.oke_beta_2.setGeometry(QtCore.QRect(120, 220, 35, 25))
        # self.oke_beta_2.setText("")
        # self.oke_beta_2.setIcon(icon6)
        # self.oke_beta_2.setObjectName("oke_beta_2")

        self.zoom_2 = QtWidgets.QLabel(self.frame_navigator)
        self.zoom_2.setGeometry(QtCore.QRect(0, 250, 50, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_2.sizePolicy().hasHeightForWidth())
        self.zoom_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(12)
        self.zoom_2.setFont(font)
        self.zoom_2.setObjectName("zoom_2")

        self.frame_panorama = QtWidgets.QFrame(self.scrollArea)
        self.frame_panorama.setGeometry(QtCore.QRect(560, 210, 211, 81))
        self.frame_panorama.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_panorama.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_panorama.setObjectName("frame_panorama")
        self.max_pano = QtWidgets.QLineEdit(self.frame_panorama)
        self.max_pano.setGeometry(QtCore.QRect(80, 15, 60, 25))
        self.max_pano.setObjectName("max_pano")
        self.max = QtWidgets.QLabel(self.frame_panorama)
        self.max.setGeometry(QtCore.QRect(10, 10, 70, 30))
        self.max.setObjectName("max")
        self.min_pano = QtWidgets.QLineEdit(self.frame_panorama)
        self.min_pano.setGeometry(QtCore.QRect(80, 45, 60, 25))
        self.min_pano.setObjectName("min_pano")
        self.min = QtWidgets.QLabel(self.frame_panorama)
        self.min.setGeometry(QtCore.QRect(10, 40, 70, 30))
        self.min.setObjectName("min")
        self.pushButton = QtWidgets.QPushButton(self.frame_panorama)
        self.pushButton.setGeometry(QtCore.QRect(150, 15, 50, 54))
        self.pushButton.setText("")
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")

        self.horizontalLayout_2.addWidget(self.label_Result_Image)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(
            50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_16.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.btn_prev_video = QtWidgets.QPushButton(self.frame_16)
        self.btn_prev_video.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_prev_video.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_prev_video.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_prev_video.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap("images/prev.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_prev_video.setIcon(icon17)
        self.btn_prev_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_prev_video.setObjectName("btn_prev_video")
        self.horizontalLayout_4.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_17.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.btn_play_pouse = QtWidgets.QPushButton(self.frame_17)
        self.btn_play_pouse.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_play_pouse.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_play_pouse.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_play_pouse.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(
            QtGui.QPixmap("images/play.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_play_pouse.setIcon(icon18)
        self.btn_play_pouse.setIconSize(QtCore.QSize(40, 40))
        self.btn_play_pouse.setObjectName("btn_play_pouse")
        self.horizontalLayout_4.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_18.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.btn_stop_video = QtWidgets.QPushButton(self.frame_18)
        self.btn_stop_video.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_stop_video.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_stop_video.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_stop_video.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(
            QtGui.QPixmap("images/icons8-stop.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_stop_video.setIcon(icon19)
        self.btn_stop_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_stop_video.setObjectName("btn_stop_video")
        self.horizontalLayout_4.addWidget(self.frame_18)
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QtCore.QSize(50, 40))
        self.frame_13.setStyleSheet("background-color: #71D1BA;   \n"
                                    "border-radius: 10px;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.btn_skip_video = QtWidgets.QPushButton(self.frame_13)
        self.btn_skip_video.setGeometry(QtCore.QRect(5, 5, 40, 30))
        self.btn_skip_video.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_skip_video.setStyleSheet(
            "QPushButton{ background-color :  #71D1BA;}\n"
            "QPushButton::pressed{ background-color : #71AED1; }\n"
            "border-radius: 10px;")
        self.btn_skip_video.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(
            QtGui.QPixmap("images/skip.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.btn_skip_video.setIcon(icon20)
        self.btn_skip_video.setIconSize(QtCore.QSize(40, 40))
        self.btn_skip_video.setObjectName("btn_skip_video")
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.label_time_recent = QtWidgets.QLabel(self.centralwidget)
        self.label_time_recent.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.label_time_recent.setFont(font)
        self.label_time_recent.setStyleSheet("border-color: #71D1BA;\n"
                                             "border-width: 2px;        \n"
                                             "border-style: solid;\n"
                                             "border-radius: 10px;")
        self.label_time_recent.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_recent.setObjectName("label_time_recent")
        self.horizontalLayout_4.addWidget(self.label_time_recent)
        self.slider_Video = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.slider_Video.sizePolicy().hasHeightForWidth())
        self.slider_Video.setSizePolicy(sizePolicy)
        self.slider_Video.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.slider_Video.setFont(font)
        self.slider_Video.setStyleSheet("")
        self.slider_Video.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Video.setObjectName("slider_Video")
        self.horizontalLayout_4.addWidget(self.slider_Video)
        self.label_time_end = QtWidgets.QLabel(self.centralwidget)
        self.label_time_end.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.label_time_end.setFont(font)
        self.label_time_end.setStyleSheet("border-color: #71D1BA;\n"
                                          "border-width: 2px;        \n"
                                          "border-style: solid;\n"
                                          "border-radius: 10px;")
        self.label_time_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_end.setObjectName("label_time_end")
        self.horizontalLayout_4.addWidget(self.label_time_end)
        spacerItem6 = QtWidgets.QSpacerItem(
            50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(
            10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_saved_image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_saved_image.sizePolicy().hasHeightForWidth())
        self.label_saved_image.setSizePolicy(sizePolicy)
        self.label_saved_image.setMinimumSize(QtCore.QSize(320, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_saved_image.setFont(font)
        self.label_saved_image.setStyleSheet(
            "border-color: rgb(66, 69, 183);\n"
            "background-color: #71D1BA;\n"
            "border-radius: 10px;")
        self.label_saved_image.setFrameShape(QtWidgets.QFrame.Box)
        self.label_saved_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_saved_image.setObjectName("label_saved_image")
        self.verticalLayout.addWidget(self.label_saved_image)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.scrollArea_saved_Image = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea_saved_Image.sizePolicy().hasHeightForWidth())
        self.scrollArea_saved_Image.setSizePolicy(sizePolicy)
        self.scrollArea_saved_Image.setMinimumSize(QtCore.QSize(340, 0))
        self.scrollArea_saved_Image.setStyleSheet("")
        self.scrollArea_saved_Image.setWidgetResizable(True)
        self.scrollArea_saved_Image.setObjectName("scrollArea_saved_Image")
        self.scrollAreaWidgetContents_saved_Image = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_saved_Image.setGeometry(
            QtCore.QRect(0, 0, 338, 546))
        self.scrollAreaWidgetContents_saved_Image.setObjectName(
            "scrollAreaWidgetContents_saved_Image")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_saved_Image)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_saved_Image.setWidget(
            self.scrollAreaWidgetContents_saved_Image)
        self.verticalLayout.addWidget(self.scrollArea_saved_Image)

        self.frame_axis = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_axis.sizePolicy().hasHeightForWidth())
        self.frame_axis.setSizePolicy(sizePolicy)
        self.frame_axis.setMinimumSize(QtCore.QSize(0, 220))
        self.frame_axis.setMaximumSize(QtCore.QSize(16777215, 220))
        self.frame_axis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_axis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_axis.setObjectName("frame_axis")
        self.label_saved_image_2 = QtWidgets.QLabel(self.frame_axis)
        self.label_saved_image_2.setGeometry(QtCore.QRect(10, 10, 320, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_saved_image_2.sizePolicy().hasHeightForWidth())
        self.label_saved_image_2.setSizePolicy(sizePolicy)
        self.label_saved_image_2.setMinimumSize(QtCore.QSize(320, 40))
        self.label_saved_image_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_saved_image_2.setFont(font)
        self.label_saved_image_2.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                               "background-color: #71D1BA;\n"
                                               "border-radius: 10px;")
        self.label_saved_image_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_saved_image_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_saved_image_2.setObjectName("label_saved_image_2")
        self.btn_disconnect = QtWidgets.QPushButton(self.frame_axis)
        self.btn_disconnect.setGeometry(QtCore.QRect(230, 60, 100, 30))
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.btn_connect = QtWidgets.QPushButton(self.frame_axis)
        self.btn_connect.setGeometry(QtCore.QRect(10, 60, 100, 30))
        self.btn_connect.setObjectName("btn_connect")
        self.btn_reset = QtWidgets.QPushButton(self.frame_axis)
        self.btn_reset.setGeometry(QtCore.QRect(120, 60, 100, 30))
        self.btn_reset.setObjectName("btn_reset")
        self.next_speed = QtWidgets.QPushButton(self.frame_axis)
        self.next_speed.setGeometry(QtCore.QRect(270, 100, 60, 30))
        self.next_speed.setText("")
        self.next_speed.setObjectName("next_speed")
        self.prev = QtWidgets.QPushButton(self.frame_axis)
        self.prev.setGeometry(QtCore.QRect(80, 100, 60, 30))
        self.prev.setText("")
        self.prev.setObjectName("prev")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_axis)
        self.lineEdit_4.setGeometry(QtCore.QRect(145, 100, 50, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.next = QtWidgets.QPushButton(self.frame_axis)
        self.next.setGeometry(QtCore.QRect(200, 100, 60, 30))
        self.next.setText("")
        self.next.setObjectName("next")
        self.prev_speed = QtWidgets.QPushButton(self.frame_axis)
        self.prev_speed.setGeometry(QtCore.QRect(10, 100, 60, 30))
        self.prev_speed.setText("")
        self.prev_speed.setObjectName("prev_speed")
        self.run_abs = QtWidgets.QPushButton(self.frame_axis)
        self.run_abs.setGeometry(QtCore.QRect(230, 140, 100, 30))
        self.run_abs.setObjectName("run_abs")
        self.absolute_val = QtWidgets.QLineEdit(self.frame_axis)
        self.absolute_val.setGeometry(QtCore.QRect(134, 140, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_val.sizePolicy().hasHeightForWidth())
        self.absolute_val.setSizePolicy(sizePolicy)
        self.absolute_val.setMaximumSize(QtCore.QSize(100, 16777215))
        self.absolute_val.setObjectName("absolute_val")
        self.label_3 = QtWidgets.QLabel(self.frame_axis)
        self.label_3.setGeometry(QtCore.QRect(10, 138, 114, 30))
        self.label_3.setObjectName("label_3")
        self.help_axis = QtWidgets.QPushButton(self.frame_axis)
        self.help_axis.setGeometry(QtCore.QRect(230, 180, 100, 30))
        self.help_axis.setObjectName("help_axis")
        self.label_6 = QtWidgets.QLabel(self.frame_axis)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 120, 30))
        self.label_6.setObjectName("label_6")
        self.label_curent_axis = QtWidgets.QLabel(self.frame_axis)
        self.label_curent_axis.setGeometry(QtCore.QRect(140, 180, 80, 30))
        self.label_curent_axis.setObjectName("label_curent_axis")
        self.verticalLayout.addWidget(self.frame_axis)

        self.frame_original_image = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_original_image.sizePolicy().hasHeightForWidth())
        self.frame_original_image.setSizePolicy(sizePolicy)
        self.frame_original_image.setMinimumSize(QtCore.QSize(0, 220))
        self.frame_original_image.setStyleSheet(
            "background-color: rgb(0, 0, 0);\n"
            "border-radius: 10px;")
        self.frame_original_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_original_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_original_image.setObjectName("frame_original_image")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(
            self.frame_original_image)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_Original_Image = QtWidgets.QLabel(self.frame_original_image)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_Original_Image.sizePolicy().hasHeightForWidth())
        self.label_Original_Image.setSizePolicy(sizePolicy)
        self.label_Original_Image.setMinimumSize(QtCore.QSize(266, 200))
        self.label_Original_Image.setStyleSheet("border-radius: 10px;")
        self.label_Original_Image.setText("")
        self.label_Original_Image.setScaledContents(False)
        self.label_Original_Image.setObjectName("label_Original_Image")
        self.horizontalLayout_11.addWidget(self.label_Original_Image)
        self.verticalLayout.addWidget(self.frame_original_image)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 34))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        font.setUnderline(False)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Image = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image.setIcon(icon7)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionLoad_Image.setFont(font)
        self.actionLoad_Image.setObjectName("actionLoad_Image")
        self.actionLoad_Video = QtWidgets.QAction(MainWindow)
        self.actionLoad_Video.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionLoad_Video.setFont(font)
        self.actionLoad_Video.setObjectName("actionLoad_Video")
        self.actionOpen_Cam = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionOpen_Cam.setFont(font)
        self.actionOpen_Cam.setObjectName("actionOpen_Cam")
        self.actionRecord_video = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionRecord_video.setFont(font)
        self.actionRecord_video.setObjectName("actionRecord_video")
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionSave_Image.setFont(font)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setIcon(icon16)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Apps = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionAbout_Apps.setFont(font)
        self.actionAbout_Apps.setObjectName("actionAbout_Apps")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.actionAbout_Us.setFont(font)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.menuFile.addAction(self.actionLoad_Image)
        self.menuFile.addAction(self.actionLoad_Video)
        self.menuFile.addAction(self.actionOpen_Cam)
        self.menuFile.addAction(self.actionRecord_video)
        self.menuFile.addAction(self.actionSave_Image)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_Apps)
        self.menuHelp.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Home.setToolTip(_translate("MainWindow", "Back to home"))
        self.btn_Home.setStatusTip(
            _translate(
                "MainWindow",
                "Back to default Application"))
        self.btn_Home.setShortcut(_translate("MainWindow", "H"))
        self.label.setText(_translate("MainWindow", "View"))
        self.btn_normal.setToolTip(_translate("MainWindow", "Anypoint View"))
        self.btn_normal.setStatusTip(_translate("MainWindow", "Anypoint View"))
        self.btn_anypoint.setToolTip(_translate("MainWindow", "Panorama View"))
        self.btn_anypoint.setStatusTip(
            _translate("MainWindow", "Panorama View"))
        self.btn_panorama.setToolTip(_translate("MainWindow", "Panorama View"))
        self.btn_panorama.setStatusTip(
            _translate("MainWindow", "Panorama View"))
        self.label_2.setText(_translate("MainWindow", "Help"))
        self.btn_show_help.setShortcut(
            _translate("MainWindow", "Ctrl+Shift+/"))
        self.btn_Open_Image.setToolTip(_translate("MainWindow", "Load Image"))
        self.btn_Open_Image.setStatusTip(
            _translate(
                "MainWindow",
                "Open image from local directory"))
        self.btn_Open_Image.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.btn_Open_Video.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.btn_Open_Cam.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.btn_Zoom_in.setShortcut(_translate("MainWindow", "="))
        self.btn_Zoom_out.setShortcut(_translate("MainWindow", "-"))
        self.label_Application.setText(_translate("MainWindow", "Application"))
        self.btn_prev_video.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.btn_play_pouse.setShortcut(_translate("MainWindow", "Space"))
        self.btn_stop_video.setShortcut(_translate("MainWindow", "0"))
        self.btn_skip_video.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.label_time_recent.setText(_translate("MainWindow", "00.00"))
        self.label_time_end.setText(_translate("MainWindow", "00.00"))
        self.label_saved_image.setText(_translate("MainWindow", "Image Saved"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionLoad_Video.setText(_translate("MainWindow", "Load Video"))
        self.actionOpen_Cam.setText(_translate("MainWindow", "Open Cam"))
        self.actionRecord_video.setText(
            _translate("MainWindow", "Record video"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_Apps.setText(_translate("MainWindow", "About Apps"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))

        self.btn_Up_View.setShortcut(_translate("MainWindow", "Up"))
        self.btn_Right_view.setShortcut(_translate("MainWindow", "Right"))
        self.btn_left_view.setShortcut(_translate("MainWindow", "Left"))
        self.btn_Down_view.setShortcut(_translate("MainWindow", "Down"))
        self.label_mode.setText(_translate("MainWindow", "Mode:"))
        self.radio_btn_mode_1.setText(_translate("MainWindow", "1"))
        self.radio_btn_mode_2.setText(_translate("MainWindow", "2"))
        self.alpha_2.setText(_translate("MainWindow", "Alpha:"))
        self.beta_2.setText(_translate("MainWindow", "Beta  :"))
        self.zoom_2.setText(_translate("MainWindow", "Zoom:"))

        self.max.setText(_translate("MainWindow", "Max Fov :"))
        self.min.setText(_translate("MainWindow", "Min Fov :"))

        self.label_saved_image_2.setText(_translate("MainWindow", "Axis Controller"))
        self.btn_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.btn_connect.setText(_translate("MainWindow", "Connect"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.lineEdit_4.setText(_translate("MainWindow", "500"))
        self.run_abs.setText(_translate("MainWindow", "Run"))
        self.label_3.setText(_translate("MainWindow", "Absolute Move:"))
        self.help_axis.setText(_translate("MainWindow", "Help"))
        self.label_6.setText(_translate("MainWindow", "Current Position:"))
        self.label_curent_axis.setText(_translate("MainWindow", "00 mm"))
