
import sys
from PySide2 import QtWidgets, QtGui,  QtCore 

import my_os_path as my_os_path

icon_dir = my_os_path.icon


class MyRadioButton(QtWidgets.QToolButton):
    """класс для преобразования QToolButton в RadioButton,
    а то RadioButton что-то срет событиями """

    def __init__(self, parent: QtWidgets,  icon):
        super().__init__(parent)
        self.par: QtWidgets = parent 

        self.setMinimumSize(QtCore.QSize(30, 30))
        self.setStyleSheet(f"image: url({icon_dir + icon});background-image: url({icon_dir + icon});")
        self.setText("")
        self.setCheckable(True)
        self.setContentsMargins(0, 0, 0, 0)

    def mousePressEvent(self, event):
        # self.par.disable_checked(self)
        # print("dddddd")
        return super().mousePressEvent(event)
