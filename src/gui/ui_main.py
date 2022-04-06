# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resources/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(536, 634)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")
        self.select_isotopinator = QtWidgets.QPushButton(self.centralwidget)
        self.select_isotopinator.setObjectName("select_isotopinator")
        self.gridLayout.addWidget(self.select_isotopinator, 0, 0, 1, 1)
        self.select_plot_widget = QtWidgets.QPushButton(self.centralwidget)
        self.select_plot_widget.setObjectName("select_plot_widget")
        self.gridLayout.addWidget(self.select_plot_widget, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.select_last_widget = QtWidgets.QPushButton(self.centralwidget)
        self.select_last_widget.setObjectName("select_last_widget")
        self.gridLayout.addWidget(self.select_last_widget, 0, 2, 1, 1)
        self.label_institute = QtWidgets.QLabel(self.centralwidget)
        self.label_institute.setObjectName("label_institute")
        self.gridLayout.addWidget(self.label_institute, 2, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)
        self.actionquit = QtWidgets.QAction(main)
        self.actionquit.setObjectName("actionquit")
        self.menuFile.addAction(self.actionquit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(main)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Application Test"))
        self.select_isotopinator.setText(_translate("main", "Isotopinator"))
        self.select_plot_widget.setText(_translate("main", "Gaussian plot"))
        self.label.setText(_translate("main", "Total Energies / UPPA / Rouen / MagLab"))
        self.select_last_widget.setText(_translate("main", "Last widget"))
        self.label_institute.setText(_translate("main", "iC2MC"))
        self.menuFile.setTitle(_translate("main", "File"))
        self.actionquit.setText(_translate("main", "quit"))

