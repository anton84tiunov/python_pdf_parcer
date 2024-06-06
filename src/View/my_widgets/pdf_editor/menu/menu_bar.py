import sys, os
from PySide6 import QtWidgets, QtGui,  QtCore 

import src.View.my_widgets.general.button.radio_buttom as radio_buttom

red_style = "background-color: rgb(255, 0, 0);"
green_style = "background-color: rgb(0, 255, 0);"
blue_style = "background-color: rgb(0, 0, 255);"

class MyMenuBar(QtWidgets.QFrame):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)

        # self.setStyleSheet(green_style)

        self.g_box = QtWidgets.QGridLayout(self)
        self.g_box.setContentsMargins(0, 0, 0, 0)

        self.btn_open_pdf = QtWidgets.QPushButton("open & convert pdf", self)
        self.g_box.addWidget(self.btn_open_pdf, 0, 0, 1, 1)

        self.spacer_menu_box = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.g_box.addItem(self.spacer_menu_box, 0, 1, 1, 1)

        self.dbl_sp_box_num_page = QtWidgets.QSpinBox(self)
        self.g_box.addWidget(self.dbl_sp_box_num_page, 1, 0, 1, 1)

        self.btn_save_qt = QtWidgets.QPushButton("save qt", self)
        self.g_box.addWidget(self.btn_save_qt, 2, 0, 1, 1)

        self.btn_open_qt = QtWidgets.QPushButton("open qt", self)
        self.g_box.addWidget(self.btn_open_qt, 3, 0, 1, 1)

        self.btn_close_qt = QtWidgets.QPushButton("close qt", self)
        self.g_box.addWidget(self.btn_close_qt, 4, 0, 1, 1)

        self.spacer_menu_box2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.g_box.addItem(self.spacer_menu_box2, 5, 0, 1, 1)



