from PySide2 import QtWidgets, QtGui,  QtCore 

class MyPointRectRect(QtWidgets.QGraphicsRectItem):
    """класс для создания точек изменения координат прямоугольников и четырехугольников графики"""

    def __init__(self, root: QtWidgets, el: QtWidgets, name_point: str, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
        self.name_point: str = name_point
        self.root: QtWidgets = root
        self.el: QtWidgets = el
        self.delete_attribute_my_point_rect: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(0, 0, 255, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        dev_x = updated_cursor_position.x() - orig_cursor_position.x()
        dev_y = updated_cursor_position.y() - orig_cursor_position.y()

        self.setRect(self.rect().x() + dev_x, self.rect().y() + dev_y, self.rect().width(), self.rect().height(), )
        p = self.el.rect()
        if self.name_point == "top":
            # self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            y = p.y() + dev_y
            p.setY(y)

        if self.name_point == "bottom":
            # self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
            h = p.height() + dev_y
            p.setHeight(h)

        if self.name_point == "left":
            # self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
            x = p.x() + dev_x
            p.setX(x)

        if self.name_point == "right":
            # self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
            w = p.width() + dev_x
            p.setWidth(w)

        self.el.setRect(p)

