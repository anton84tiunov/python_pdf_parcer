from PySide6 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window

class MyPointellipsePath(QtWidgets.QGraphicsEllipseItem):
    """класс для создания точек изменения координат путей графики"""

    def __init__(self, pointF: QtCore.QPointF):
        rectF = QtCore.QRectF(pointF, QtCore.QSize(5, 5))
        super().__init__(rectF)
        # self.rectF = rectF
        self.delete_attribute_my_point_ellipse: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(255, 0, 0, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)


        self.setAcceptHoverEvents(True)

  