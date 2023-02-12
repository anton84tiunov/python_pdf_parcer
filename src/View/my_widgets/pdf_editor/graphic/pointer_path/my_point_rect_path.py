import copy
from PySide6 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window

class MyPointRectPath(QtWidgets.QGraphicsRectItem):
    """класс для создания точек изменения координат путей графики"""

    def __init__(self, root: QtWidgets, el: QtWidgets, num_point: int, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
        self.num_point: int = num_point
        self.root: QtWidgets = root
        self.el: QtWidgets = el
        self.orig_cursor_position =  QtCore.QPointF()
        self.delete_attribute_my_point_rect: bool = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(255, 0, 0, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)


        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
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
                    p = self.el.path()
                    # for ii in range(self.path().elementCount()):
                    x = p.elementAt(self.num_point).x
                    y = p.elementAt(self.num_point).y
                    p.setElementPositionAt(self.num_point, x + dev_x, y + dev_y)
                    self.el.setPath(p)
                self.orig_cursor_position = copy.deepcopy(updated_cursor_position)