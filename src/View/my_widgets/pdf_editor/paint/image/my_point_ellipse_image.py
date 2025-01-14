from PySide6 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window

class MyPointellipseImage(QtWidgets.QGraphicsEllipseItem):
    """класс для создания точек определяющих точки рисоания фигуры"""

    def __init__(self, root: QtWidgets, el: QtWidgets, name_point: str, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
        self.name_point: str = name_point
        self.root: QtWidgets = root
        self.el: QtWidgets = el
        self.delete_attribute_my_point_ellipse: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(0, 0, 255, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.setAcceptHoverEvents(True)

   