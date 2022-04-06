# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/resources/ui/isotopinator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_isotopinator(object):
    def setupUi(self, isotopinator):
        isotopinator.setObjectName("isotopinator")
        isotopinator.resize(484, 391)
        self.gridLayout_3 = QtWidgets.QGridLayout(isotopinator)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mass_split_input = QtWidgets.QLineEdit(isotopinator)
        self.mass_split_input.setObjectName("mass_split_input")
        self.gridLayout.addWidget(self.mass_split_input, 1, 0, 1, 1)
        self.search_mass_split_btn = QtWidgets.QPushButton(isotopinator)
        self.search_mass_split_btn.setObjectName("search_mass_split_btn")
        self.gridLayout.addWidget(self.search_mass_split_btn, 1, 2, 1, 1)
        self.mass_split_label = QtWidgets.QLabel(isotopinator)
        self.mass_split_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mass_split_label.setObjectName("mass_split_label")
        self.gridLayout.addWidget(self.mass_split_label, 0, 0, 1, 1)
        self.tolerance_label = QtWidgets.QLabel(isotopinator)
        self.tolerance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tolerance_label.setObjectName("tolerance_label")
        self.gridLayout.addWidget(self.tolerance_label, 0, 1, 1, 1)
        self.tolerance_input = QtWidgets.QLineEdit(isotopinator)
        self.tolerance_input.setText("")
        self.tolerance_input.setObjectName("tolerance_input")
        self.gridLayout.addWidget(self.tolerance_input, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.candidate_list = QtWidgets.QListWidget(isotopinator)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.candidate_list.setFont(font)
        self.candidate_list.setObjectName("candidate_list")
        self.gridLayout_2.addWidget(self.candidate_list, 1, 0, 1, 1)
        self.candidate_label = QtWidgets.QLabel(isotopinator)
        self.candidate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.candidate_label.setObjectName("candidate_label")
        self.gridLayout_2.addWidget(self.candidate_label, 0, 0, 1, 1)
        self.error_label = QtWidgets.QLabel(isotopinator)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.gridLayout_2.addWidget(self.error_label, 0, 2, 1, 1)
        self.error_list = QtWidgets.QListWidget(isotopinator)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        self.error_list.setFont(font)
        self.error_list.setObjectName("error_list")
        self.gridLayout_2.addWidget(self.error_list, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.isotopinator_tips_label = QtWidgets.QLabel(isotopinator)
        self.isotopinator_tips_label.setObjectName("isotopinator_tips_label")
        self.verticalLayout.addWidget(self.isotopinator_tips_label)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(isotopinator)
        QtCore.QMetaObject.connectSlotsByName(isotopinator)

    def retranslateUi(self, isotopinator):
        _translate = QtCore.QCoreApplication.translate
        isotopinator.setWindowTitle(_translate("isotopinator", "Form"))
        self.mass_split_input.setPlaceholderText(_translate("isotopinator", "1.003355"))
        self.search_mass_split_btn.setText(_translate("isotopinator", "Search split"))
        self.mass_split_label.setText(_translate("isotopinator", "Mass split (Da)"))
        self.tolerance_label.setText(_translate("isotopinator", "Tolerance (Da)"))
        self.tolerance_input.setPlaceholderText(_translate("isotopinator", "0.0001"))
        self.candidate_label.setText(_translate("isotopinator", "Candidate split"))
        self.error_label.setText(_translate("isotopinator", "Error (Da)"))
        self.isotopinator_tips_label.setText(_translate("isotopinator", "<html><head/><body><p>Tips 1 : Only the first 7 décimals of the error are displayed</p><p>Tips 2 : Results are sorted from the lowest absolute error to the largest.</p></body></html>"))

