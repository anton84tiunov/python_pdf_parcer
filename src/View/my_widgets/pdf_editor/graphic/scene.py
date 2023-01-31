import sys
from PySide2 import QtWidgets, QtGui,  QtCore 

import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.my_pointer_path as my_pointer_path
import src.View.my_widgets.pdf_editor.graphic.my_polygon as my_polygon
import src.View.my_widgets.pdf_editor.graphic.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.my_image as my_image
import src.View.my_widgets.pdf_editor.text.my_text_item as my_text_item

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
        # self.blockSignals(True)
        # переменные для отрисовки путей
        self.path = QtGui.QPainterPath()
        # кривой безье
        self.path_curve_is_move_to: bool = False
        self.path_curve_move_to: QtCore.QPointF = QtCore.QPointF(0.0, 0.0)
        self.path_curve_cubic_to: list[QtCore.QPointF] = []
        self.path_curve_num: int = 0
        # прямой линии
        self.path_line_is_move_to: bool = False
        self.path_line_move_to: QtCore.QPointF = QtCore.QPointF(0.0, 0.0)
        self.path_line_cubic_to: list[QtCore.QPointF] = []
        self.path_line_num: int = 0

        # pointer_path = my_pointer_path.MyPainterPath(self.root, path)
        # переменные для отрисовки полигонов
        self.pol = QtGui.QPolygonF()
        # polygon = my_polygon.MyPolygon(self.root, pol)
        # переменные для отрисовки прямоугольников
        self.rect = QtCore.QRectF()
        self.rect_p0 = QtCore.QPointF(0.0, 0.0)
        self.rect_p1 = QtCore.QPointF(0.0, 0.0)
        # rectangle = my_rectangle.MyRactangle(self.root, rect)
        # переменные для отрисовки изображений
        self.pix = QtGui.QPixmap()
        # image = my_image.MyImage(self.root, pix)
        # переменные для отрисовки текста
        self.text: str = ""
        # text_item = my_text_item.MyTextItem(self.root, text)



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
            # self.cursor_pix = QtGui.QPixmap(icon_dir + "298869_sign_out_icon.png")
            # self.cursor_scaled_pix = self.cursor_pix.scaled(QtCore.QSize(20, 20), QtCore.Qt.KeepAspectRatio)
            # self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, -1, -1)
            # self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        return super().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        button = event.button()
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        dev_x = updated_cursor_position.x() - orig_cursor_position.x()
        dev_y = updated_cursor_position.y() - orig_cursor_position.y()
        
        cursor = self.root.tab_pdf_editor.graph_tool_bar.tool_cursor

        if button == QtCore.Qt.LeftButton:
           
            if cursor == "arrow":
                ...
            elif cursor == "hand":
                ...
            elif cursor == "move":
                ...
            elif cursor == "pencil":
                ...
            elif cursor == "line":
                if not self.path_line_is_move_to:
                    # self.path_curve_move_to = updated_cursor_position
                    self.path.moveTo(updated_cursor_position)
                    self.path_line_is_move_to = True
                else:
                    self.path.lineTo(updated_cursor_position)

            elif cursor == "bezier":
                # rext_item = my_rectangle.MyRactangle(self.root, QtCore.QRectF(updated_cursor_position.x(), updated_cursor_position.y(), 10.0, 10.0))
                # # rext_item.unsetCursor()
                # self.addItem(rext_item)
                if not self.path_curve_is_move_to:
                    # self.path_curve_move_to = updated_cursor_position
                    self.path.moveTo(updated_cursor_position)
                    self.path_curve_is_move_to = True
                else:

                    if self.path_curve_num == 0:
                        self.path_curve_cubic_to.insert(0, updated_cursor_position)
                        self.path_curve_num = 1
                    elif self.path_curve_num == 1:
                        self.path_curve_cubic_to.insert(1, updated_cursor_position)
                        self.path_curve_num = 2
                    elif self.path_curve_num == 2:
                        self.path_curve_cubic_to.insert(2, updated_cursor_position)
                        # self.path.moveTo(self.path_curve_move_to)
                        print(len(self.path_curve_cubic_to))
                        # if len(self.path_curve_cubic_to) == 3:
                        self.path.cubicTo(*self.path_curve_cubic_to)
                        self.path_curve_cubic_to.clear()
                        # self.path_curve_move_to = updated_cursor_position
                        self.path_curve_num = 0

            elif cursor == "polygon":
                self.pol.append(updated_cursor_position)
            elif cursor == "rect":
                # self.rect.setTopLeft(updated_cursor_position)
                self.rect_p0 = updated_cursor_position
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
            elif cursor == "line":
                path_item = my_pointer_path.MyPainterPath(self.root, self.path)
                path_item.unsetCursor()
                self.addItem(path_item)
                self.path.clear()
                self.path_line_is_move_to = False
            elif cursor == "bezier":
                # self.path.closeSubpath()
                # if len(self.path_curve_cubic_to) == 3:
                path_item = my_pointer_path.MyPainterPath(self.root, self.path)
                path_item.unsetCursor()
                self.addItem(path_item)
                self.path.clear()
                self.path_curve_cubic_to.clear()
                self.path_curve_is_move_to = False
                self.path_curve_num = 2
            elif cursor == "polygon":
                pol_item = my_polygon.MyPolygon(self.root, self.pol)
                pol_item.unsetCursor()
                self.addItem(pol_item)
                self.pol.clear()
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
                self.rect_p1 = updated_cursor_position

                if self.rect_p0.x() > self.rect_p1.x():
                    if self.rect_p0.y() > self.rect_p1.y():
                        self.rect.setBottomRight(self.rect_p0)
                        self.rect.setTopLeft(self.rect_p1)
                    elif self.rect_p0.y() < self.rect_p1.y():
                        self.rect.setTopRight(self.rect_p0)
                        self.rect.setBottomLeft(self.rect_p1)
                elif self.rect_p0.x() < self.rect_p1.x():
                    if self.rect_p0.y() > self.rect_p1.y():
                        self.rect.setBottomLeft(self.rect_p0)
                        self.rect.setTopRight(self.rect_p1)
                    elif self.rect_p0.y() < self.rect_p1.y():
                        self.rect.setBottomRight(self.rect_p1)
                        self.rect.setTopLeft(self.rect_p0)
                rext_item = my_rectangle.MyRactangle(self.root, self.rect)
                rext_item.unsetCursor()
                self.addItem(rext_item)
            elif cursor == "circle":
                ...
            elif cursor == "text":
                ...
            elif cursor == "ruler":
                ...
            return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:

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











