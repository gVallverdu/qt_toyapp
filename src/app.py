#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication
from gui import Toyapp

if __name__ == "__main__":
    app = QApplication([])

    myapp = Toyapp()
    myapp.show()
    sys.exit(app.exec())
    