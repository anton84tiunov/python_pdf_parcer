from PySide2 import QtWidgets, QtGui,  QtCore 

import src.View.my_window.main_window as main_window


class MyContextMenu(QtWidgets.QMenu):
    """класс переопределяющий контекстное меню 
    для настройки графических элементов"""

    def __init__(self, root: main_window.MainWindow):
        super().__init__()
        self.root: main_window.MainWindow = root
        self.setStyleSheet(self.root.styleSheet())