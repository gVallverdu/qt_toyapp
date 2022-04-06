#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtWidgets import QWidget, QMessageBox
from .ui_last_widget import Ui_last_widget

from plots.color import color_plot

class Last_widget(QWidget, Ui_last_widget):

    def __init__(self, parent=None):
        """ Set up the class from ... """

        # initialize from super class
        super().__init__(parent)
        self.setupUi(self)

        self.connect_signals_slots()
    
    def connect_signals_slots(self):
        """ set up actions """
        self.plot_btn.clicked.connect(self.plot)

    def plot(self):
        if self.radio_blue.isChecked():
            color = "C0"
        elif self.radio_red.isChecked():
            color = "C3"
        else:
            QMessageBox.warning(self, "Error", 
                    f"Need a color, set blue",
                    QMessageBox.Ok)
            color = "C0"
            self.radio_blue.setChecked()

        fig = color_plot(color)
        fig.show()
        

