import copy
from PySide6 import QtWidgets, QtGui,  QtCore 

# import src.View.my_window.main_window as main_window

class MyPointRectImage(QtWidgets.QGraphicsRectItem):
    """класс для создания точек изменения координат прямоугольников и четырехугольников графики"""

    def __init__(self, root: QtWidgets, el: QtWidgets, rectF: QtCore.QRectF):
        super().__init__(rectF)
        # self.rectF = rectF
        # self.name_point: str = name_point
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
         # print(self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor)
        if self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor == "hand":
 
            updated_cursor_position = self.root.tab_pdf_editor.graph_scene.point_grid_step_cursor
            # self.orig_cursor_position = self.root.tab_pdf_editor.graph_scene.old_point_grid_step_cursor

            if  updated_cursor_position.x() != self.orig_cursor_position.x() or updated_cursor_position.y() != self.orig_cursor_position.y():
                # print(self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor)
                if self.orig_cursor_position != QtCore.QPointF():
                    dev_x = updated_cursor_position.x() - self.orig_cursor_position.x()
                    dev_y = updated_cursor_position.y() - self.orig_cursor_position.y()
        
                    # self.setRect(self.rect().x() + dev_x, self.rect().y() + dev_y, self.rect().width(), self.rect().height(), )
                    self.setRect(updated_cursor_position.x(), updated_cursor_position.y(), self.rect().width(), self.rect().height(), )
                    r = self.el.boundingRect()
                    p = self.el.pos()
                    
                    x = copy.deepcopy(p.x()) 
                    y = copy.deepcopy(p.y())

                    w = copy.deepcopy(r.width())
                    h = copy.deepcopy(r.height())



                    # scale = (self.orig_cursor_position.x() / updated_cursor_position.x()) * (self.orig_cursor_position.y() / updated_cursor_position.y())
                    scale_x = int(self.orig_cursor_position.x() - x)
                    scale_y = int(self.orig_cursor_position.y() - y)
                    # print(scale_x)
                    # print(scale_y)
                    pix = self.el.orig_pix.scaled(QtCore.QSize(scale_x, scale_y),  QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
                    # pix = pix.scaledToWidth(scale_x)
                    self.el.setPixmap(pix)
                    # self.el.setScale(scale)
                self.orig_cursor_position = copy.deepcopy(updated_cursor_position)

