# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resources/ui/last_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_last_widget(object):
    def setupUi(self, last_widget):
        last_widget.setObjectName("last_widget")
        last_widget.resize(441, 272)
        self.gridLayout = QtWidgets.QGridLayout(last_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_blue = QtWidgets.QRadioButton(last_widget)
        self.radio_blue.setChecked(True)
        self.radio_blue.setObjectName("radio_blue")
        self.horizontalLayout.addWidget(self.radio_blue)
        self.radio_red = QtWidgets.QRadioButton(last_widget)
        self.radio_red.setObjectName("radio_red")
        self.horizontalLayout.addWidget(self.radio_red)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plot_btn = QtWidgets.QPushButton(last_widget)
        self.plot_btn.setObjectName("plot_btn")
        self.verticalLayout.addWidget(self.plot_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(last_widget)
        QtCore.QMetaObject.connectSlotsByName(last_widget)

    def retranslateUi(self, last_widget):
        _translate = QtCore.QCoreApplication.translate
        last_widget.setWindowTitle(_translate("last_widget", "Form"))
        self.radio_blue.setText(_translate("last_widget", "Blue"))
        self.radio_red.setText(_translate("last_widget", "Red"))
        self.plot_btn.setText(_translate("last_widget", "Plot"))

