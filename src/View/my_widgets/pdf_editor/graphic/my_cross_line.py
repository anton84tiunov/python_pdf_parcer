from PySide6 import QtWidgets, QtGui,  QtCore 

class MyCrossLine(QtWidgets.QGraphicsLineItem):
    """
    """
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.attribute_cross_line = True







