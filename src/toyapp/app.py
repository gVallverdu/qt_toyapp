#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication
from .gui import Toyapp


def main():
    """ Main application """
    app = QApplication([])

    myapp = Toyapp()
    myapp.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
