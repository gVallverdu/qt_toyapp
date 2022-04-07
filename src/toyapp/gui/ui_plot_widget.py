# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resources/ui/plot_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plot_widget(object):
    def setupUi(self, plot_widget):
        plot_widget.setObjectName("plot_widget")
        plot_widget.resize(582, 585)
        self.gridLayout = QtWidgets.QGridLayout(plot_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(plot_widget)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mean_label = QtWidgets.QLabel(plot_widget)
        self.mean_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mean_label.setObjectName("mean_label")
        self.horizontalLayout_2.addWidget(self.mean_label)
        self.std_label = QtWidgets.QLabel(plot_widget)
        self.std_label.setAlignment(QtCore.Qt.AlignCenter)
        self.std_label.setObjectName("std_label")
        self.horizontalLayout_2.addWidget(self.std_label)
        self.npts_label = QtWidgets.QLabel(plot_widget)
        self.npts_label.setAlignment(QtCore.Qt.AlignCenter)
        self.npts_label.setObjectName("npts_label")
        self.horizontalLayout_2.addWidget(self.npts_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mean_input = QtWidgets.QLineEdit(plot_widget)
        self.mean_input.setObjectName("mean_input")
        self.horizontalLayout.addWidget(self.mean_input)
        self.std_input = QtWidgets.QLineEdit(plot_widget)
        self.std_input.setObjectName("std_input")
        self.horizontalLayout.addWidget(self.std_input)
        self.npts_input = QtWidgets.QLineEdit(plot_widget)
        self.npts_input.setObjectName("npts_input")
        self.horizontalLayout.addWidget(self.npts_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plot_btn = QtWidgets.QPushButton(plot_widget)
        self.plot_btn.setObjectName("plot_btn")
        self.verticalLayout.addWidget(self.plot_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(plot_widget)
        QtCore.QMetaObject.connectSlotsByName(plot_widget)

    def retranslateUi(self, plot_widget):
        _translate = QtCore.QCoreApplication.translate
        plot_widget.setWindowTitle(_translate("plot_widget", "Form"))
        self.title.setText(_translate("plot_widget", "A so nice plot"))
        self.mean_label.setText(_translate("plot_widget", "Mean"))
        self.std_label.setText(_translate("plot_widget", "std"))
        self.npts_label.setText(_translate("plot_widget", "npts"))
        self.mean_input.setPlaceholderText(_translate("plot_widget", "0"))
        self.std_input.setPlaceholderText(_translate("plot_widget", "1"))
        self.npts_input.setPlaceholderText(_translate("plot_widget", "100"))
        self.plot_btn.setText(_translate("plot_widget", "plot"))

