import sys
import copy
from PySide2 import QtWidgets, QtGui,  QtCore 

import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.pointer_path.my_pointer_path as my_pointer_path
import src.View.my_widgets.pdf_editor.graphic.polygon.my_polygon as my_polygon
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.image.my_image as my_image
import src.View.my_widgets.pdf_editor.graphic.text.my_text_item as my_text_item
import src.View.my_widgets.pdf_editor.paint.pointer_path.my_demo_pointer_path as my_demo_pointer_path
import src.View.my_widgets.pdf_editor.paint.pointer_path.my_point_ellipce_path as my_point_ellipce_path
import src.View.my_widgets.pdf_editor.paint.polygon.my_demo_polygon as my_demo_polygon
import src.View.my_widgets.pdf_editor.paint.polygon.my_point_ellipce_pol as my_point_ellipce_pol
# import my_os_path as my_os_path

# icon_dir = my_os_path.icon



class MyGraphicsScene(QtWidgets.QGraphicsScene):
    """класс переопределяющий  графическую сцену
        В сцене реализованны методы риования графичских фигур.
        Рисование фигур зависит от выбранной фигуры рисования в 
        src.View.my_widgets.pdf_editor.graphic.tool_bar.py .
        При помощи атрибута self.tool_cursor: str = "" класса
        MyToolBar можно определить тип фигуры.
        Рисование фигур полностью построенно на событиях мыши.
    """
    
    def __init__(self, root, **kwargs):
        super().__init__( **kwargs)
        self.root: QtWidgets = root

        # self.is_mouse_pressed = False
        # # self.blockSignals(True)
        # # переменные для отрисовки путей
        # self.path = QtGui.QPainterPath()
        # self.path_pencil = QtGui.QPainterPath()
        # self.pointer_path_pencil = QtGui.QPainterPath()
        # self.path_demo_item_pencil = my_demo_pointer_path.MyDemoPainterPath(self.pointer_path_pencil)
        # # self.addItem(self.path_demo_item)
        # # кривой безье
        # self.path_curve_is_move_to: bool = False
        # self.path_curve_move_to: QtCore.QPointF = QtCore.QPointF(0.0, 0.0)
        # self.path_curve_cubic_to: list[QtCore.QPointF] = []
        # self.path_curve_num: int = 0
        # # прямой линии
        # self.path_line_is_move_to: bool = False
        # self.path_line_move_to: QtCore.QPointF = QtCore.QPointF(0.0, 0.0)
        # self.path_line_cubic_to: list[QtCore.QPointF] = []
        # self.path_line_num: int = 0
        # self.pointer_path = QtGui.QPainterPath()
        # self.path_demo_item = my_demo_pointer_path.MyDemoPainterPath(self.pointer_path)
        # # self.addItem(self.path_demo_item)
        # # pointer_path = my_pointer_path.MyPainterPath(self.root, path)
        # # переменные для отрисовки полигонов
        # self.pol_demo_item_is_append_to_scene: bool = False
        # self.pol = QtGui.QPolygonF()
        # self.pol_demo_item = my_demo_polygon.MyDemoPolygon(self.pol)
        # # polygon = my_polygon.MyPolygon(self.root, pol)
        # # переменные для отрисовки прямоугольников
        # self.rect = QtCore.QRectF()
        # self.rect_p0 = QtCore.QPointF(0.0, 0.0)
        # self.rect_p1 = QtCore.QPointF(0.0, 0.0)
        # # rectangle = my_rectangle.MyRactangle(self.root, rect)
        # # переменные для отрисовки изображений
        # self.pix = QtGui.QPixmap()
        # # image = my_image.MyImage(self.root, pix)
        # # переменные для отрисовки текста
        # self.text: str = ""
        # # text_item = my_text_item.MyTextItem(self.root, text)

        self.is_mouse_pressed = False

        self.p_path = QtGui.QPainterPath()
        self.p_path_demo = QtGui.QPainterPath()
        self.path_demo_item = my_demo_pointer_path.MyDemoPainterPath(self.p_path_demo)

        self.curve_points: list = []


    def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        button = event.button()
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        dev_x = updated_cursor_position.x() - orig_cursor_position.x()
        dev_y = updated_cursor_position.y() - orig_cursor_position.y()
        
        cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

        if button == QtCore.Qt.LeftButton:

            self.is_mouse_pressed = True
           
            if cursor == "arrow":
                ...
            elif cursor == "hand":
                ...
            elif cursor == "move":
                ...
            elif cursor == "pencil":
                ...
            elif cursor == "line":
                if self.p_path.elementCount() == 0:
                    self.p_path.moveTo(updated_cursor_position)
                    self.p_path_demo.moveTo(updated_cursor_position)
                    self.addItem(self.path_demo_item)
                else:
                    self.curve_points.clear()
                    self.p_path.lineTo(updated_cursor_position)
                    self.p_path_demo.lineTo(updated_cursor_position)
                    self.path_demo_item.setPath(self.p_path_demo)


            elif cursor == "bezier":
                if self.p_path.elementCount() == 0:
                    self.p_path.moveTo(updated_cursor_position)
                    self.p_path_demo.moveTo(updated_cursor_position)
                    self.addItem(self.path_demo_item)
                else:
                    if len(self.curve_points) == 0:
                        self.curve_points.insert(0, updated_cursor_position)
                    elif len(self.curve_points) == 1:
                        self.curve_points.insert(1, updated_cursor_position)
                    elif len(self.curve_points) == 2:
                        self.curve_points.insert(2, updated_cursor_position)
                        self.p_path.cubicTo(*self.curve_points)
                        self.p_path_demo.cubicTo(*self.curve_points)
                        self.path_demo_item.setPath(self.p_path_demo)
                        self.curve_points.clear()

            elif cursor == "polygon":
                ...
            elif cursor == "rect":
                ...
            elif cursor == "circle":
                ...
            elif cursor == "text":
                ...
            elif cursor == "ruler":
                ...
        if button == QtCore.Qt.MidButton:
            if cursor == "arrow":
                ...
            elif cursor == "hand":
                ...
            elif cursor == "move":
                ...
            elif cursor == "pencil":
                ...
            elif cursor == "line" or cursor == "bezier":
                path_item = my_pointer_path.MyPainterPath(self.root, self.p_path)
                self.addItem(path_item)
                self.p_path = QtGui.QPainterPath()
                if self.p_path_demo.elementCount() > 0:
                    self.removeItem(self.path_demo_item)
                self.p_path_demo = QtGui.QPainterPath()
                self.path_demo_item = my_demo_pointer_path.MyDemoPainterPath(self.p_path_demo)

            elif cursor == "rect":
                ...
            elif cursor == "circle":
                ...
            elif cursor == "text":
                ...
            elif cursor == "ruler":
                ...
            
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        button = event.button()
        if button == QtCore.Qt.LeftButton:

            self.is_mouse_pressed = False

            orig_cursor_position = event.lastScenePos()
            updated_cursor_position = event.scenePos()

            cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

            if cursor == "arrow":
                ...
            elif cursor == "hand":
                ...
            elif cursor == "move":
                ...
            elif cursor == "pencil":
                ...
            elif cursor == "line":
                ...
            elif cursor == "bezier":
                ...
            elif cursor == "polygon":
                ...
            elif cursor == "rect":
                ...
            elif cursor == "circle":
                ...
            elif cursor == "text":
                ...
            elif cursor == "ruler":
                ...
            return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()
        cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

        if cursor == "arrow":
            ...
        elif cursor == "hand":
            ...
        elif cursor == "move":
            ...
        elif cursor == "pencil":
            ...
        elif cursor == "line":
            ...
        elif cursor == "bezier":
            ...
        elif cursor == "polygon":
            ...
        elif cursor == "rect":
            ...
        elif cursor == "circle":
            ...
        elif cursor == "text":
            ...
        elif cursor == "ruler":
            ...
        return super().mouseMoveEvent(event)

    def contextMenuEvent(self, event: QtWidgets.QGraphicsSceneContextMenuEvent) -> None:

        updated_cursor_position = event.scenePos()
        cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

        if cursor == "arrow":
            ...
        elif cursor == "hand":
            ...
        elif cursor == "move":
            ...
        elif cursor == "pencil":
            ...
        elif cursor == "line":
            ...
        elif cursor == "bezier":
            ...
        elif cursor == "polygon":
            ...
        elif cursor == "rect":
            ...
        elif cursor == "circle":
            ...
        elif cursor == "text":
            ...
        elif cursor == "ruler":
            ...
        return super().contextMenuEvent(event)

    def mouseDoubleClickEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        
        updated_cursor_position = event.scenePos()
        cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

        if cursor == "arrow":
            ...
        elif cursor == "hand":
            ...
        elif cursor == "move":
            ...
        elif cursor == "pencil":
            ...
        elif cursor == "line":
            ...
        elif cursor == "bezier":
            ...
        elif cursor == "polygon":
            ...
        elif cursor == "rect":
            ...
        elif cursor == "circle":
            ...
        elif cursor == "text":
            ...
        elif cursor == "ruler":
            ...
        return super().mouseDoubleClickEvent(event)

















































# ///////////////////////////////////////////
    #     self.is_mouse_pressed = False
    #     # self.blockSignals(True)
    #     # переменные для отрисовки путей
    #     self.path = QtGui.QPainterPath()
    #     self.path_pencil = QtGui.QPainterPath()
    #     self.pointer_path_pencil = QtGui.QPainterPath()
    #     self.path_demo_item_pencil = my_demo_pointer_path.MyDemoPainterPath(self.pointer_path_pencil)
    #     # self.addItem(self.path_demo_item)
    #     # кривой безье
    #     self.path_curve_is_move_to: bool = False
    #     self.path_curve_move_to: QtCore.QPointF = QtCore.QPointF(0.0, 0.0)
    #     self.path_curve_cubic_to: list[QtCore.QPointF] = []
    #     self.path_curve_num: int = 0
    #     # прямой линии
    #     self.path_line_is_move_to: bool = False
    #     self.path_line_move_to: QtCore.QPointF = QtCore.QPointF(0.0, 0.0)
    #     self.path_line_cubic_to: list[QtCore.QPointF] = []
    #     self.path_line_num: int = 0
    #     self.pointer_path = QtGui.QPainterPath()
    #     self.path_demo_item = my_demo_pointer_path.MyDemoPainterPath(self.pointer_path)
    #     # self.addItem(self.path_demo_item)
    #     # pointer_path = my_pointer_path.MyPainterPath(self.root, path)
    #     # переменные для отрисовки полигонов
    #     self.pol_demo_item_is_append_to_scene: bool = False
    #     self.pol = QtGui.QPolygonF()
    #     self.pol_demo_item = my_demo_polygon.MyDemoPolygon(self.pol)
    #     # polygon = my_polygon.MyPolygon(self.root, pol)
    #     # переменные для отрисовки прямоугольников
    #     self.rect = QtCore.QRectF()
    #     self.rect_p0 = QtCore.QPointF(0.0, 0.0)
    #     self.rect_p1 = QtCore.QPointF(0.0, 0.0)
    #     # rectangle = my_rectangle.MyRactangle(self.root, rect)
    #     # переменные для отрисовки изображений
    #     self.pix = QtGui.QPixmap()
    #     # image = my_image.MyImage(self.root, pix)
    #     # переменные для отрисовки текста
    #     self.text: str = ""
    #     # text_item = my_text_item.MyTextItem(self.root, text)



    # def mouseDoubleClickEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        
    #     updated_cursor_position = event.scenePos()
    #     cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

    #     if cursor == "arrow":
    #         ...
    #     elif cursor == "hand":
    #         ...
    #     elif cursor == "move":
    #         ...
    #     elif cursor == "pencil":
    #         ...
    #     elif cursor == "line":
    #         ...
    #     elif cursor == "bezier":
    #         ...
    #     elif cursor == "polygon":
    #         ...
    #     elif cursor == "rect":
    #         ...
    #     elif cursor == "circle":
    #         ...
    #     elif cursor == "text":
    #         ...
    #     elif cursor == "ruler":
    #         ...
    #         # self.cursor_pix = QtGui.QPixmap(icon_dir + "298869_sign_out_icon.png")
    #         # self.cursor_scaled_pix = self.cursor_pix.scaled(QtCore.QSize(20, 20), QtCore.Qt.KeepAspectRatio)
    #         # self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, -1, -1)
    #         # self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

    #     return super().mouseDoubleClickEvent(event)

    # def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
    #     button = event.button()
    #     orig_cursor_position = event.lastScenePos()
    #     updated_cursor_position = event.scenePos()

    #     dev_x = updated_cursor_position.x() - orig_cursor_position.x()
    #     dev_y = updated_cursor_position.y() - orig_cursor_position.y()
        
    #     cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

    #     if button == QtCore.Qt.LeftButton:

    #         self.is_mouse_pressed = True
           
    #         if cursor == "arrow":
    #             ...
    #         elif cursor == "hand":
    #             ...
    #         elif cursor == "move":
    #             ...
    #         elif cursor == "pencil":
    #             self.pointer_path_pencil.clear()
    #             self.path_pencil.clear()
    #             self.path_pencil.moveTo(updated_cursor_position)
    #             self.pointer_path_pencil.moveTo(updated_cursor_position)
    #             self.path_demo_item_pencil.setPath(self.pointer_path_pencil)
    #             # if  not self.path_curve_is_move_to or not self.path_line_is_move_to:
    #             #     self.removeItem(self.path_demo_item)
    #             self.addItem(self.path_demo_item_pencil)
    #         elif cursor == "line":
    #             self.path_curve_cubic_to.clear()
    #             self.path_curve_num = 0
    #             if not self.path_line_is_move_to:
    #                 self.pointer_path.clear()
    #                 self.path.moveTo(updated_cursor_position)
    #                 self.pointer_path.moveTo(updated_cursor_position)
    #                 item_ellipse_point = my_point_ellipce_path.MyPointEllipcePath(updated_cursor_position)
    #                 self.addItem(item_ellipse_point)
    #                 self.path_line_is_move_to = True
    #                 self.path_curve_is_move_to = True
    #                 self.path_demo_item.setPath(self.pointer_path)
    #                 self.addItem(self.path_demo_item)
    #             else:
    #                 # self.collidingItems
    #                 self.removeItem(self.path_demo_item)
    #                 self.path.lineTo(updated_cursor_position)
    #                 self.pointer_path.lineTo(updated_cursor_position)
    #                 self.path_demo_item.setPath(self.pointer_path)
    #                 self.addItem(self.path_demo_item)
    #                 item_ellipse_point = my_point_ellipce_path.MyPointEllipcePath(updated_cursor_position)
    #                 self.addItem(item_ellipse_point)

    #         elif cursor == "bezier":

    #             if not self.path_curve_is_move_to:
    #                 self.pointer_path.clear()        
    #                 self.path.moveTo(updated_cursor_position)
    #                 self.pointer_path.moveTo(updated_cursor_position)
    #                 item_ellipse_point = my_point_ellipce_path.MyPointEllipcePath(updated_cursor_position)
    #                 self.addItem(item_ellipse_point)
    #                 self.path_curve_is_move_to = True
    #                 self.path_line_is_move_to = True
    #                 self.path_demo_item.setPath(self.pointer_path)
    #                 self.addItem(self.path_demo_item)
    #             else:

    #                 if self.path_curve_num == 0:
    #                     self.path_curve_cubic_to.insert(0, updated_cursor_position)
    #                     item_ellipse_point = my_point_ellipce_path.MyPointEllipcePath(updated_cursor_position)
    #                     self.addItem(item_ellipse_point)
    #                     self.path_curve_num = 1
    #                 elif self.path_curve_num == 1:
    #                     self.path_curve_cubic_to.insert(1, updated_cursor_position)
    #                     item_ellipse_point = my_point_ellipce_path.MyPointEllipcePath(updated_cursor_position)
    #                     self.addItem(item_ellipse_point)
    #                     self.path_curve_num = 2
    #                 elif self.path_curve_num == 2:
    #                     self.path_curve_cubic_to.insert(2, updated_cursor_position)
    #                     self.removeItem(self.path_demo_item)
    #                     if len(self.path_curve_cubic_to) == 3:
    #                         self.path.cubicTo(*self.path_curve_cubic_to)
    #                         self.pointer_path.cubicTo(*self.path_curve_cubic_to)
    #                         item_ellipse_point = my_point_ellipce_path.MyPointEllipcePath(updated_cursor_position)
    #                         self.addItem(item_ellipse_point)
    #                         self.path_demo_item.setPath(self.pointer_path)
    #                         self.addItem(self.path_demo_item)
    #                     self.path_curve_cubic_to.clear()
    #                     self.path_curve_num = 0

    #         elif cursor == "polygon":
    #             self.pol.append(updated_cursor_position)
    #             item_ellipse_point = my_point_ellipce_pol.MyPointEllipcePol(updated_cursor_position)
    #             self.addItem(item_ellipse_point)
    #             if self.pol_demo_item_is_append_to_scene:
    #                 self.removeItem(self.pol_demo_item)
    #             self.pol_demo_item.setPolygon(self.pol)
    #             self.pol_demo_item.isActive()
    #             self.addItem(self.pol_demo_item)
    #             self.pol_demo_item_is_append_to_scene = True

    #         elif cursor == "rect":
    #             # self.rect.setTopLeft(updated_cursor_position)
    #             self.rect_p0 = updated_cursor_position
    #         elif cursor == "circle":
    #             ...
    #         elif cursor == "text":
    #             ...
    #         elif cursor == "ruler":
    #             ...
    #     if button == QtCore.Qt.MidButton:
    #         if cursor == "arrow":
    #             ...
    #         elif cursor == "hand":
    #             ...
    #         elif cursor == "move":
    #             ...
    #         elif cursor == "pencil":
    #             ...
    #         elif cursor == "line":
    #             path_item = my_pointer_path.MyPainterPath(self.root, self.path)
    #             path_item.unsetCursor()
    #             self.removeItem(self.path_demo_item)
    #             self.addItem(path_item)
    #             self.path.clear()
    #             self.pointer_path.clear()
    #             self.path_line_is_move_to = False
    #             self.path_line_is_move_to = False
    #             self.path_curve_cubic_to.clear()
    #             items = self.items()
    #             for item in items:
    #                 if hasattr(item, "delete_attribute_my_point_ellipce"):
    #                     self.removeItem(item)
    #         elif cursor == "bezier":
    #             # path_item = my_pointer_path.MyPainterPath(self.root, self.path)
    #             # path_item.unsetCursor()
    #             if self.path_curve_cubic_to == 0:
    #                 self.removeItem(self.path_demo_item)
        
    #             path_item = my_pointer_path.MyPainterPath(self.root, self.path)
    #             path_item.unsetCursor()
    #             self.addItem(path_item)
    #             self.path.clear()
    #             self.path_curve_cubic_to.clear()
    #             self.path_line_is_move_to = False
    #             self.path_line_is_move_to = False
    #             self.path_curve_num = 0
    #             self.pointer_path.clear()
    #             items = self.items()
    #             for item in items:
    #                 if hasattr(item, "delete_attribute_my_point_ellipce"):
    #                     self.removeItem(item)
    #         elif cursor == "polygon":
    #             pol_item = my_polygon.MyPolygon(self.root, self.pol)
    #             pol_item.unsetCursor()
    #             self.addItem(pol_item)
    #             self.pol_demo_item_is_append_to_scene = False
    #             self.removeItem(self.pol_demo_item)
    #             self.pol.clear()
    #             items = self.items()
    #             for item in items:
    #                 if hasattr(item, "delete_attribute_my_point_ellipce"):
    #                     self.removeItem(item)
    #         elif cursor == "rect":
    #             ...
    #         elif cursor == "circle":
    #             ...
    #         elif cursor == "text":
    #             ...
    #         elif cursor == "ruler":
    #             ...
            
    #     return super().mousePressEvent(event)

    # def mouseReleaseEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
    #     button = event.button()
    #     if button == QtCore.Qt.LeftButton:

    #         self.is_mouse_pressed = False

    #         orig_cursor_position = event.lastScenePos()
    #         updated_cursor_position = event.scenePos()

    #         cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

    #         if cursor == "arrow":
    #             ...
    #         elif cursor == "hand":
    #             ...
    #         elif cursor == "move":
    #             ...
    #         elif cursor == "pencil":
    #             path_item = my_pointer_path.MyPainterPath(self.root, self.path_pencil)
    #             path_item.unsetCursor()
    #             self.removeItem(self.path_demo_item_pencil)
    #             self.addItem(path_item)
    #             self.path_pencil.clear()
    #             self.pointer_path_pencil.clear()
    #             # self.path_line_is_move_to = False
    #             # self.path_line_is_move_to = False
    #             # self.path_curve_cubic_to.clear()
    #             items = self.items()
    #             for item in items:
    #                 if hasattr(item, "delete_attribute_my_point_ellipce"):
    #                     self.removeItem(item)
    #         elif cursor == "line":
    #             ...
    #         elif cursor == "bezier":
    #             ...
    #         elif cursor == "polygon":
    #             ...
    #         elif cursor == "rect":
    #             self.rect_p1 = updated_cursor_position

    #             if self.rect_p0.x() > self.rect_p1.x():
    #                 if self.rect_p0.y() > self.rect_p1.y():
    #                     self.rect.setBottomRight(self.rect_p0)
    #                     self.rect.setTopLeft(self.rect_p1)
    #                 elif self.rect_p0.y() < self.rect_p1.y():
    #                     self.rect.setTopRight(self.rect_p0)
    #                     self.rect.setBottomLeft(self.rect_p1)
    #             elif self.rect_p0.x() < self.rect_p1.x():
    #                 if self.rect_p0.y() > self.rect_p1.y():
    #                     self.rect.setBottomLeft(self.rect_p0)
    #                     self.rect.setTopRight(self.rect_p1)
    #                 elif self.rect_p0.y() < self.rect_p1.y():
    #                     self.rect.setBottomRight(self.rect_p1)
    #                     self.rect.setTopLeft(self.rect_p0)
    #             rext_item = my_rectangle.MyRactangle(self.root, self.rect)
    #             rext_item.unsetCursor()
    #             self.addItem(rext_item)
    #         elif cursor == "circle":
    #             ...
    #         elif cursor == "text":
    #             ...
    #         elif cursor == "ruler":
    #             ...
    #         return super().mouseReleaseEvent(event)

    # def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
    #     orig_cursor_position = event.lastScenePos()
    #     updated_cursor_position = event.scenePos()
    #     cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

    #     if cursor == "arrow":
    #         ...
    #     elif cursor == "hand":
    #         ...
    #     elif cursor == "move":
    #         ...
    #     elif cursor == "pencil":
    #         if self.is_mouse_pressed:
    #             self.removeItem(self.path_demo_item)
    #             self.path.lineTo(updated_cursor_position)
    #             self.pointer_path.lineTo(updated_cursor_position)
    #             self.path_demo_item.setPath(self.pointer_path)
    #             self.addItem(self.path_demo_item)

    #     elif cursor == "line":
    #         if self.path_line_is_move_to:

    #             # self.collidingItems
    #             # self.removeItem(self.path_demo_item)
    #             # self.path.lineTo(updated_cursor_position)
    #             # self.pointer_path.lineTo(updated_cursor_position)
    #             # demo_item = copy.deepcopy(self.path_demo_item)
    #             # demo_path = copy.deepcopy(self.pointer_path)
    #             # demo_path.lineTo(updated_cursor_position)
    #             # demo_item.setPath(demo_path)
    #             # self.addItem(demo_item)
    #             ...

    #     elif cursor == "bezier":
    #         ...
    #     elif cursor == "polygon":
    #         ...
    #     elif cursor == "rect":
    #         ...
    #     elif cursor == "circle":
    #         ...
    #     elif cursor == "text":
    #         ...
    #     elif cursor == "ruler":
    #         ...
    #     return super().mouseMoveEvent(event)

    # def contextMenuEvent(self, event: QtWidgets.QGraphicsSceneContextMenuEvent) -> None:

    #     updated_cursor_position = event.scenePos()
    #     cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

    #     if cursor == "arrow":
    #         ...
    #     elif cursor == "hand":
    #         ...
    #     elif cursor == "move":
    #         ...
    #     elif cursor == "pencil":
    #         ...
    #     elif cursor == "line":
    #         ...
    #     elif cursor == "bezier":
    #         ...
    #     elif cursor == "polygon":
    #         ...
    #     elif cursor == "rect":
    #         ...
    #     elif cursor == "circle":
    #         ...
    #     elif cursor == "text":
    #         ...
    #     elif cursor == "ruler":
    #         ...
    #     return super().contextMenuEvent(event)











