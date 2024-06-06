import sys
from PySide6 import QtWidgets, QtGui,  QtCore 

import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

# combo_style = """

# QComboBox::down-arrow {
#     image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);
# }
# }
# """

class MyComboBoxNum(QtWidgets.QComboBox):
    """класс для преобразования QToolButton в RadioButton,
    а то RadioButton что-то срет событиями """

    def __init__(self, parent: QtWidgets,  icon):
        super().__init__(parent)
        self.par: QtWidgets = parent 

        self.setMinimumSize(QtCore.QSize(200, 30))
        self.setBaseSize(QtCore.QSize(200, 30))
        # self.setMaximumSize(QtCore.QSize(200, 30))
        # self.combo_style = f"down-arrow::image: url({icon_svg_dir + icon});"

        self.setStyleSheet(f"image: url({icon_svg_dir + icon});")
        # self.setStyleSheet(self.combo_style)
        # self.setText("")
        # self.setCheckable(True)
        # print(self.style())
        self.setContentsMargins(0, 0, 0, 0)
        self.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "100"])
        font = QtGui.QFont()
        font.setPointSize(4)
        # font.setWeight(12)
        self.setFont(font)

    def mousePressEvent(self, event):
        # self.par.disable_checked(self)
        # print("dddddd")
        return super().mousePressEvent(event)

