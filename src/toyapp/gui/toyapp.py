#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtWidgets import QMainWindow
from .ui_main import Ui_main

# load widgets
from .isotopinator import Isotopinator
from .plot_widget import Plot_widget
from .last_widget import Last_widget


class Toyapp(QMainWindow, Ui_main):
    """ This class is the main application """

    # USERDATA_ROLE = QtCore.Qt.UserRole

    def __init__(self, parent=None):
        """ Set up the class from ... """

        # initialize from super class
        super().__init__(parent)
        self.setupUi(self)

        self.assign_widget()

        self.connect_signals_slots()

        self.show()

    def assign_widget(self):
        self.stackedWidget.addWidget(Isotopinator(self))
        self.stackedWidget.addWidget(Plot_widget(self))
        self.stackedWidget.addWidget(Last_widget(self))

    def connect_signals_slots(self):
        self.select_isotopinator.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))
        self.select_plot_widget.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1))
        self.select_last_widget.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2))

        # connection ui <=> functions
        # self.pushButton_start_isotopinator.clicked.connect(self.star_button_function)
        # self.push_plot_random.clicked.connect(self.plot_random)
        # self.list_split_name.clicked.connect(self.select_change_split)
        # self.list_range.clicked.connect(self.select_change_range)

    def show_widget(self, name):
        """ set up isotopinator widget """
        current_name = self.stackedWidget.currentWidget().objectName()

        # if name != current_name:
        #     self.widget_index[name])
