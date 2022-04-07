#!/usr/bin/env python
# coding: utf-8

from tabnanny import check
from PyQt5.QtWidgets import QWidget, QMessageBox
from .ui_plot_widget import Ui_plot_widget

from plots.gaussian import gaussian_plot
import matplotlib.pyplot as plt


class Plot_widget(QWidget, Ui_plot_widget):

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
        """ create the plot from the input parameters """

        def check_value(inp_obj, dtype):
            """ check if input_obj is a valid input of type dtype. If input
            is empty, take placeHolder value number and
            show a QMessageBox in case of error """
            str_val = inp_obj.text() if inp_obj.text() != "" else inp_obj.placeholderText()
            try:
                val = dtype(str_val)
            except ValueError:
                QMessageBox.warning(
                    self, "Error",
                    f"Wrong value: '{str_val}'\n You must write a {str(dtype)}.",
                    QMessageBox.Ok)
                val = None

            return val

        mean = check_value(self.mean_input, float)
        std = check_value(self.std_input, float)
        npts = check_value(self.npts_input, int)

        with plt.xkcd():
            fig = gaussian_plot(mean, std, npts)
            fig.show()
