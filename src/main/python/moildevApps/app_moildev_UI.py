# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Moil_Software.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ctx):
        super(Ui_MainWindow, self).__init__()
        self.ctx = ctx
        self.setObjectName("MainWindow")
        self.resize(473, 329)
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(66, 69, 183);\n"
                                 "background-color: #71D1BA;\n"
                                 "border-radius: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Serif")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.install_mor_application = QtWidgets.QPushButton(self.centralwidget)
        self.install_mor_application.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.install_mor_application.setFont(font)
        self.install_mor_application.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                                   "QPushButton::pressed{ background-color : #71AED1; }\n"
                                                   "QPushButton{border-style:\"solid\";}\n"
                                                   "QPushButton{border-radius:\"15\";}")
        self.install_mor_application.setObjectName("install_mor_application")
        self.horizontalLayout_2.addWidget(self.install_mor_application)
        self.Open_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Open_btn.sizePolicy().hasHeightForWidth())
        self.Open_btn.setSizePolicy(sizePolicy)
        self.Open_btn.setMinimumSize(QtCore.QSize(80, 50))
        self.Open_btn.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                    "QPushButton::pressed{ background-color : #71AED1; }\n"
                                    "QPushButton{border-style:\"solid\";}\n"
                                    "QPushButton{border-radius:\"10\";}")
        self.Open_btn.setObjectName("Open_btn")
        self.horizontalLayout_2.addWidget(self.Open_btn)
        self.Delete_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete_btn.sizePolicy().hasHeightForWidth())
        self.Delete_btn.setSizePolicy(sizePolicy)
        self.Delete_btn.setMinimumSize(QtCore.QSize(80, 50))
        self.Delete_btn.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                      "QPushButton::pressed{ background-color : #71AED1; }\n"
                                      "QPushButton{border-style:\"solid\";}\n"
                                      "QPushButton{border-radius:\"10\";}")
        self.Delete_btn.setObjectName("Delete_btn")
        self.horizontalLayout_2.addWidget(self.Delete_btn)
        self.btn_Exit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Exit.sizePolicy().hasHeightForWidth())
        self.btn_Exit.setSizePolicy(sizePolicy)
        self.btn_Exit.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_Exit.setFont(font)
        self.btn_Exit.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                    "QPushButton::pressed{ background-color : #DE1212; }\n"
                                    "QPushButton{border-style:\"solid\";}\n"
                                    "QPushButton{border-radius:\"15\";}")
        self.btn_Exit.setObjectName("btn_Exit")
        self.horizontalLayout_2.addWidget(self.btn_Exit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton.setStyleSheet("QPushButton{ background-color :  #71D1BA;}\n"
                                      "QPushButton::pressed{ background-color : #71AED1; }\n"
                                      "QPushButton{border-style:\"solid\";}\n"
                                      "QPushButton{border-radius:\"25\";}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap.fromImage(self.ctx.icon_help), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to Moil Software"))
        self.label_3.setText(_translate("MainWindow", "   Select application here:"))
        self.install_mor_application.setText(_translate("MainWindow", "Add"))
        self.Open_btn.setText(_translate("MainWindow", "Open"))
        self.Delete_btn.setText(_translate("MainWindow", "Delete"))
        self.btn_Exit.setText(_translate("MainWindow", "Exit"))
