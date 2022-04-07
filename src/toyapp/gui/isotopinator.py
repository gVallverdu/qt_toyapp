#!/usr/bin/env python
# coding: utf-8

from PyQt5.QtWidgets import QWidget, QMessageBox, QListWidgetItem
from isotopes import Isotope

from .ui_isotopinator import Ui_isotopinator


class Isotopinator(QWidget, Ui_isotopinator):

    def __init__(self, parent=None):
        """ Set up the class from ... """

        # initialize from super class
        super().__init__(parent)
        self.setupUi(self)

        self.connect_signals_slots()

    def connect_signals_slots(self):
        """ set up actions """
        self.search_mass_split_btn.clicked.connect(self.search_mass_split)
        self.candidate_list.clicked.connect(self.select_candidate)
        self.error_list.clicked.connect(self.select_error)

    def search_mass_split(self):
        """ Look for mass split and show the list """

        # get requested split value or placeholder value
        requested_split = self.mass_split_input.text()
        if requested_split == "":
            requested_split = self.mass_split_input.placeholderText()
            self.mass_split_input.setText(requested_split)

        # get tolerance value or placeholder value
        tolerance = self.tolerance_input.text()
        if tolerance == "":
            tolerance = self.tolerance_input.placeholderText()
            self.tolerance_input.setText(tolerance)

        # check entered values
        valid = True
        try:
            requested_split = float(requested_split)
        except ValueError:
            QMessageBox.warning(
                self, "Error",
                f"Wrong mass split value: '{requested_split}'",
                QMessageBox.Ok)
            valid = False

        try:
            tolerance = float(tolerance)
        except ValueError:
            QMessageBox.warning(
                self, "Error", f"Wrong mass split value: '{tolerance}'",
                QMessageBox.Ok)
            valid = False

        if valid:
            # look for split mass values
            candidates = Isotope.find_mass_split(
                requested_split, tolerance, sort=True, superscript=False)
        else:
            candidates = []

        if len(candidates) >= 1:
            # clear current list
            self.candidate_list.clear()
            self.error_list.clear()

            for name, error in candidates:
                self.candidate_list.addItem(QListWidgetItem(name))
                self.error_list.addItem(QListWidgetItem(f"{error: .7f}"))

    def select_candidate(self):
        i = self.candidate_list.currentRow()
        self.error_list.item(i).setSelected(True)

    def select_error(self):
        i = self.error_list.currentRow()
        self.candidate_list.item(i).setSelected(True)
