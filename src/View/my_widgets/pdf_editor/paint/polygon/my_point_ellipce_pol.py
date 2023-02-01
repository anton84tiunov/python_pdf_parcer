from PySide2 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window

class MyPointRectPol(QtWidgets.QGraphicsEllipseItem):
    """класс для создания точек изменения координат полегонов графики"""

    def __init__(self, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
       
        self.delete_attribute_my_point_rect: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(0, 255, 0, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
      

        self.setAcceptHoverEvents(True)

   