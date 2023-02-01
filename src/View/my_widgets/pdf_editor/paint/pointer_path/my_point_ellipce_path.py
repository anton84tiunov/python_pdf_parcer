from PySide2 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window

class MyPointRectPath(QtWidgets.QGraphicsEllipseItem):
    """класс для создания точек изменения координат путей графики"""

    def __init__(self, root: QtWidgets, el: QtWidgets, num_point: int, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
        self.num_point: int = num_point
        self.root: QtWidgets = root
        self.el: QtWidgets = el
        self.delete_attribute_my_point_ellipce: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(255, 0, 0, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)


        self.setAcceptHoverEvents(True)

  