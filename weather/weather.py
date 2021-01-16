# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_weather(object):
    def setupUi(self, weather):
        weather.setObjectName("weather")
        weather.resize(638, 702)
        weather.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(weather)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.search = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setMinimumSize(QtCore.QSize(180, 50))
        self.search.setMaximumSize(QtCore.QSize(180, 50))
        self.search.setObjectName("search")
        self.verticalLayout_3.addWidget(self.search)
        self.select = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select.sizePolicy().hasHeightForWidth())
        self.select.setSizePolicy(sizePolicy)
        self.select.setMinimumSize(QtCore.QSize(180, 350))
        self.select.setMaximumSize(QtCore.QSize(180, 16777215))
        self.select.setBaseSize(QtCore.QSize(0, 0))
        self.select.setObjectName("select")
        self.verticalLayout_3.addWidget(self.select)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(180, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(180, 50))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.time0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time0.sizePolicy().hasHeightForWidth())
        self.time0.setSizePolicy(sizePolicy)
        self.time0.setMinimumSize(QtCore.QSize(150, 50))
        self.time0.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.time0.setFont(font)
        self.time0.setText("")
        self.time0.setObjectName("time0")
        self.verticalLayout.addWidget(self.time0)
        self.weap0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weap0.sizePolicy().hasHeightForWidth())
        self.weap0.setSizePolicy(sizePolicy)
        self.weap0.setMinimumSize(QtCore.QSize(150, 150))
        self.weap0.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.weap0.setFont(font)
        self.weap0.setText("")
        self.weap0.setObjectName("weap0")
        self.verticalLayout.addWidget(self.weap0)
        self.wea0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wea0.sizePolicy().hasHeightForWidth())
        self.wea0.setSizePolicy(sizePolicy)
        self.wea0.setMinimumSize(QtCore.QSize(150, 25))
        self.wea0.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.wea0.setFont(font)
        self.wea0.setText("")
        self.wea0.setObjectName("wea0")
        self.verticalLayout.addWidget(self.wea0)
        self.tem0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tem0.sizePolicy().hasHeightForWidth())
        self.tem0.setSizePolicy(sizePolicy)
        self.tem0.setMinimumSize(QtCore.QSize(150, 50))
        self.tem0.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tem0.setFont(font)
        self.tem0.setText("")
        self.tem0.setObjectName("tem0")
        self.verticalLayout.addWidget(self.tem0)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.winp0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winp0.sizePolicy().hasHeightForWidth())
        self.winp0.setSizePolicy(sizePolicy)
        self.winp0.setMinimumSize(QtCore.QSize(50, 50))
        self.winp0.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.winp0.setFont(font)
        self.winp0.setText("")
        self.winp0.setObjectName("winp0")
        self.horizontalLayout.addWidget(self.winp0)
        self.win0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.win0.sizePolicy().hasHeightForWidth())
        self.win0.setSizePolicy(sizePolicy)
        self.win0.setMinimumSize(QtCore.QSize(100, 50))
        self.win0.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.win0.setFont(font)
        self.win0.setText("")
        self.win0.setObjectName("win0")
        self.horizontalLayout.addWidget(self.win0)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.suntime0 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suntime0.sizePolicy().hasHeightForWidth())
        self.suntime0.setSizePolicy(sizePolicy)
        self.suntime0.setMinimumSize(QtCore.QSize(150, 50))
        self.suntime0.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.suntime0.setFont(font)
        self.suntime0.setText("")
        self.suntime0.setObjectName("suntime0")
        self.verticalLayout.addWidget(self.suntime0)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.time1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time1.sizePolicy().hasHeightForWidth())
        self.time1.setSizePolicy(sizePolicy)
        self.time1.setMinimumSize(QtCore.QSize(150, 50))
        self.time1.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.time1.setFont(font)
        self.time1.setText("")
        self.time1.setObjectName("time1")
        self.verticalLayout_2.addWidget(self.time1)
        self.weap1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weap1.sizePolicy().hasHeightForWidth())
        self.weap1.setSizePolicy(sizePolicy)
        self.weap1.setMinimumSize(QtCore.QSize(150, 150))
        self.weap1.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.weap1.setFont(font)
        self.weap1.setText("")
        self.weap1.setObjectName("weap1")
        self.verticalLayout_2.addWidget(self.weap1)
        self.wea1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wea1.sizePolicy().hasHeightForWidth())
        self.wea1.setSizePolicy(sizePolicy)
        self.wea1.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.wea1.setFont(font)
        self.wea1.setText("")
        self.wea1.setObjectName("wea1")
        self.verticalLayout_2.addWidget(self.wea1)
        self.tem1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tem1.sizePolicy().hasHeightForWidth())
        self.tem1.setSizePolicy(sizePolicy)
        self.tem1.setMinimumSize(QtCore.QSize(150, 50))
        self.tem1.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tem1.setFont(font)
        self.tem1.setText("")
        self.tem1.setObjectName("tem1")
        self.verticalLayout_2.addWidget(self.tem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.winp1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winp1.sizePolicy().hasHeightForWidth())
        self.winp1.setSizePolicy(sizePolicy)
        self.winp1.setMinimumSize(QtCore.QSize(50, 50))
        self.winp1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.winp1.setFont(font)
        self.winp1.setText("")
        self.winp1.setObjectName("winp1")
        self.horizontalLayout_2.addWidget(self.winp1)
        self.win1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.win1.sizePolicy().hasHeightForWidth())
        self.win1.setSizePolicy(sizePolicy)
        self.win1.setMinimumSize(QtCore.QSize(100, 50))
        self.win1.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.win1.setFont(font)
        self.win1.setText("")
        self.win1.setObjectName("win1")
        self.horizontalLayout_2.addWidget(self.win1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.suntime1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suntime1.sizePolicy().hasHeightForWidth())
        self.suntime1.setSizePolicy(sizePolicy)
        self.suntime1.setMinimumSize(QtCore.QSize(150, 50))
        self.suntime1.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.suntime1.setFont(font)
        self.suntime1.setText("")
        self.suntime1.setObjectName("suntime1")
        self.verticalLayout_2.addWidget(self.suntime1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setMinimumSize(QtCore.QSize(0, 15))
        self.warning.setMaximumSize(QtCore.QSize(16777215, 15))
        self.warning.setText("")
        self.warning.setObjectName("warning")
        self.verticalLayout_4.addWidget(self.warning)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        weather.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(weather)
        self.statusbar.setObjectName("statusbar")
        weather.setStatusBar(self.statusbar)

        self.retranslateUi(weather)
        self.select.clicked['QModelIndex'].connect(weather.get_weather)
        self.pushButton.clicked.connect(weather.get_weather_list)
        QtCore.QMetaObject.connectSlotsByName(weather)

    def retranslateUi(self, weather):
        _translate = QtCore.QCoreApplication.translate
        weather.setWindowTitle(_translate("weather", "MainWindow"))
        self.pushButton.setText(_translate("weather", "search"))