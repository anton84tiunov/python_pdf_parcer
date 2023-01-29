import sys
import src.View.my_window.main_window as main_window
from PySide2 import QtWidgets, QtGui,  QtCore 




class MyGraphicsScene(QtWidgets.QGraphicsScene):
    """класс переопределяющий  графическую сцену"""
    
    def __init__(self, root, **kwargs):
        super().__init__( **kwargs)
        # self.root: main_window.MainWindow = root

















