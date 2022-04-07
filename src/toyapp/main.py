#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication
from toyapp.gui import Toyapp

def main():
    """ Main application """
    app = QApplication([])

    myapp = Toyapp()
    myapp.show()
    sys.exit(app.exec())

