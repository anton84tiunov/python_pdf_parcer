from PySide6 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window


class MyContextMenu(QtWidgets.QMenu):
    """класс переопределяющий контекстное меню 
    для настройки графических элементов"""

    def __init__(self, root: QtWidgets):
        super().__init__()
        self.root: QtWidgets = root
        self.setStyleSheet(self.root.styleSheet())