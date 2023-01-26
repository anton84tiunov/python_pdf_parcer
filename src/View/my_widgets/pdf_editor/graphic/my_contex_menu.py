from PySide2 import QtWidgets, QtGui,  QtCore 


class MyContextMenu(QtWidgets.QMenu):
    """класс переопределяющий контекстное меню 
    для настройки графических элементов"""

    def __init__(self, root: QtWidgets):
        super().__init__()
        self.root: QtWidgets = root
        self.setStyleSheet(self.root.styleSheet())