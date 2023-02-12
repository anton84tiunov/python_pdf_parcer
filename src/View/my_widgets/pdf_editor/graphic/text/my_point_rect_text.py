import copy
from PySide6 import QtWidgets, QtGui,  QtCore 

class MyPointRectText(QtWidgets.QGraphicsRectItem):
    """класс для создания точек изменения координат прямоугольников и четырехугольников графики"""

    def __init__(self, root: QtWidgets, el: QtWidgets, name_point: str, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
        self.name_point: str = name_point
        self.root: QtWidgets = root
        self.el: QtWidgets = el
        self.orig_cursor_position =  QtCore.QPointF()
        self.delete_attribute_my_point_rect: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(0, 0, 255, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        # orig_cursor_position = event.lastScenePos()
        # updated_cursor_position = event.scenePos()
         # print(self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor)
        if self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor == "hand":
 
            updated_cursor_position = self.root.tab_pdf_editor.graph_scene.point_grid_step_cursor
            # orig_cursor_position = self.root.tab_pdf_editor.graph_scene.old_point_grid_step_cursor

            if  updated_cursor_position.x() != self.orig_cursor_position.x() or updated_cursor_position.y() != self.orig_cursor_position.y():
                # print(self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor)
                if self.orig_cursor_position != QtCore.QPointF():
                    dev_x = updated_cursor_position.x() - self.orig_cursor_position.x()
                    dev_y = updated_cursor_position.y() - self.orig_cursor_position.y()
            
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
                
                self.orig_cursor_position = copy.deepcopy(updated_cursor_position)

