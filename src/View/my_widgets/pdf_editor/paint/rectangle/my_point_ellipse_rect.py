from PySide2 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window

class MyPointRectRect(QtWidgets.QGraphicsRectItem):
    """класс для создания точек изменения координат прямоугольников и четырехугольников графики"""

    def __init__(self, el: QtWidgets, name_point: str, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
        self.name_point: str = name_point
        self.el: QtWidgets = el
        self.delete_attribute_my_point_rect: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(0, 0, 255, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.setAcceptHoverEvents(True)

   