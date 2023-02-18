import sys
import copy
import typing
import random
import asyncio
from PySide6 import QtWidgets, QtGui,  QtCore 
from PySide6.QtSvgWidgets import QGraphicsSvgItem

from matplotlib.figure import Figure                                              # +++
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  # +++

import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.pointer_path.my_pointer_path as my_pointer_path
import src.View.my_widgets.pdf_editor.graphic.polygon.my_polygon as my_polygon
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.image.my_image as my_image
import src.View.my_widgets.pdf_editor.graphic.text.my_text_item as my_text_item
import src.View.my_widgets.pdf_editor.graphic.ellipse.my_ellopse as my_ellopse
import src.View.my_widgets.pdf_editor.paint.pointer_path.my_demo_pointer_path as my_demo_pointer_path
import src.View.my_widgets.pdf_editor.paint.pointer_path.my_point_ellipse_path as my_point_ellipse_path
import src.View.my_widgets.pdf_editor.paint.polygon.my_demo_polygon as my_demo_polygon
import src.View.my_widgets.pdf_editor.paint.polygon.my_point_ellipse_pol as my_point_ellipse_pol
import src.View.my_widgets.pdf_editor.paint.rectangle.my_demo_rectangle as my_demo_rectangle
import src.View.my_widgets.pdf_editor.paint.ellipse.my_demo_ellipse as my_demo_ellipse
import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
import src.View.my_widgets.pdf_editor.graphic.scene_rect_item as scene_rect_item
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
        self.point_grid_step_cursor = QtCore.QPointF()
        self.old_point_grid_step_cursor = QtCore.QPointF()
        self.buffer_copy_item = QtWidgets.QWidget()


        # self.setSceneRect(0.0, 0.0, 200.0, 200.0)
        # self.is_0_open_file = True
        # self.setSceneRect(0.0, 0.0, 10000.0, 10000.0)
        self.grid_step = 1
        self.grid_pen = QtGui.QPen(QtGui.QColor(0, 0, 0))
        self.grid_pen.setCosmetic(True)
        self.background_brush = QtGui.QBrush( QtGui.QColor(232, 235, 232), QtCore.Qt.SolidPattern)
        


        
        # self.cursor_rect = QtCore.QRectF(1.0, 1.0, 5.0, 5.0)
        # # self.cursor_rect.transposed()
        # self.cursor_item = QtWidgets.QGraphicsEllipseItem(self.cursor_rect)
        # self.cursor_item.setZValue(999999999)
        # # self.cursor_item.setPen(self.grid_pen)
        # self.cursor_item.setBrush(QtGui.QColor(0, 0, 0, 255))
        # self.cursor_item.setTransform(QtGui.QTransform.fromTranslate(-2.5, -2.5))
        # self.addItem(self.cursor_item)

        # self.vert_line_cursor = QtCore.QLineF(0.0, 0.0, 0.0, 100.0)
        self.vert_line_cursor_item = QtWidgets.QGraphicsLineItem(0.0, 0.0, 0.0, 0.0)
        self.vert_line_cursor_item.setZValue(999999999)
        self.vert_line_cursor_item.setPen(self.grid_pen)
        # self.vert_line_cursor.setBrush(QtGui.QColor(0, 0, 0, 255))
        # self.vert_line_cursor_item.setTransform(QtGui.QTransform.fromTranslate(-0.0, -50.0))
        # self.hor_line_cursor = QtCore.QLineF(0.0, 0.0, 100.0, 0.0)
        self.hor_line_cursor_item = QtWidgets.QGraphicsLineItem(0.0, 0.0, 0.0, 0.0)
        self.hor_line_cursor_item.setZValue(999999999)
        self.hor_line_cursor_item.setPen(self.grid_pen)
        # self.hor_line_cursor.setBrush(QtGui.QColor(0, 0, 0, 255))
        # self.hor_line_cursor_item.setTransform(QtGui.QTransform.fromTranslate(-50.0, -0.0))
        self.rect_page = scene_rect_item.MyRectPage(self.root, QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.rect_page.setBrush(self.background_brush)
        self.rect_page.setZValue(-999999999)
        # self.addItem(self.vert_line_cursor_item)
        # self.addItem(self.hor_line_cursor_item)
        # self.addItem(self.rect_page)

        # self.grid_cords = QtWidgets.QGraphicsItemGroup()
        # self.grid_cords = QtWidgets.QGraphicsItemGroup()
        # self.addItem(self.grid_cords)


        # # переменные для отрисовки изображений
        # self.pix = QtGui.QPixmap()
        # # image = my_image.MyImage(self.root, pix)
        # # переменные для отрисовки текста
        # self.text: str = ""
        # # text_item = my_text_item.MyTextItem(self.root, text)

        self.is_mouse_left_pressed = False

        self.p_path_pen = QtGui.QPainterPath()
        self.p_path_pen_demo = QtGui.QPainterPath()
        self.path_pen_demo_item = my_demo_pointer_path.MyDemoPainterPath(self.p_path_pen_demo)


        self.p_path_lc = QtGui.QPainterPath()
        self.p_path_lc_demo = QtGui.QPainterPath()
        self.path_lc_demo_item = my_demo_pointer_path.MyDemoPainterPath(self.p_path_lc_demo)
        self.curve_points: list = []

        self.pol_demo_item_is_append_to_scene: bool = False
        self.pol = QtGui.QPolygonF()
        self.pol_demo_item = my_demo_polygon.MyDemoPolygon(self.pol)
        # polygon = my_polygon.MyPolygon(self.root, pol)


        self.rect = QtCore.QRectF()
        self.rect_demo = QtCore.QRectF()
        self.rect_p0 = QtCore.QPointF(0.0, 0.0)
        self.rect_p1 = QtCore.QPointF(0.0, 0.0)
        self.rect_demo_item = my_demo_rectangle.MyDemoRactangle(self.rect_demo)


        self.ellopse = QtCore.QRectF()
        self.ellopse_demo = QtCore.QRectF()
        self.ellopse_p0 = QtCore.QPointF(0.0, 0.0)
        self.ellopse_p1 = QtCore.QPointF(0.0, 0.0)
        self.ellopse_demo_item = my_demo_ellipse.MyDemoEllipse(self.ellopse_demo)

    def round_step(sel, num, step):
        return round(num / step) * step

    def set_grid_cords(self):
        # self.grid_step = StopAsyncIteration
        # self.grid_step = step
        # fon = QGraphicsSvgItem("assets/image/fon_1.SVG")
        # fon.setPos(1.0, 1.0)
        # self.addItem(fon);
        # if self.grid_cords.em
        # self.removeItem(self.grid_cords)
        # if not self.is_0_open_file:
        #     # self.removeItem(self.cursor_item)
        #     self.removeItem(self.vert_line_cursor_item)
        #     self.removeItem(self.hor_line_cursor_item)
        #     self.is_0_open_file = False
        # self.BackgroundLayer
        # self.sce
        # self.root.tab_pdf_editor.graph_view.se
        # self.root.tab_pdf_editor.graph_view.updateSceneRect(QtCore.QRectF(0.0, 0.0, self.width(), self.height()))
        # self.setSceneRect(0.0, 0.0, self.width(), self.height())
        # self.setSceneRect(0.0, 0.0, self.width() * 2, self.height() * 2)
        # self.sceneRect().
       
        # self.addItem(self.cursor_item)
        self.vert_line_cursor_item.setLine(0.0, 0.0, 0.0, self.height())
        self.hor_line_cursor_item.setLine(0.0, 0.0, self.width(), 0.0)
        self.addItem(self.vert_line_cursor_item)
        self.addItem(self.hor_line_cursor_item)
        self.rect_page.setRect(0.0, 0.0, self.width(), self.height())
        self.addItem(self.rect_page)

    def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        button = event.button()
       
        cursor = self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor

        if button == QtCore.Qt.MouseButton.LeftButton:

            self.is_mouse_left_pressed = True
           
            if cursor == "arrow":
                ...
            elif cursor == "hand":
                ...
            elif cursor == "move":
                ...
            elif cursor == "pencil":
                self.p_path_pen.moveTo(self.point_grid_step_cursor)
                self.p_path_pen_demo.moveTo(self.point_grid_step_cursor)
                self.path_pen_demo_item.setPath(self.p_path_pen_demo)
                self.addItem(self.path_pen_demo_item)

            elif cursor == "line":
                if self.p_path_lc.elementCount() == 0:
                    self.p_path_lc.moveTo(self.point_grid_step_cursor)
                    self.p_path_lc_demo.moveTo(self.point_grid_step_cursor)
                    self.addItem(self.path_lc_demo_item)
                else:
                    self.curve_points.clear()
                    self.p_path_lc.lineTo(self.point_grid_step_cursor)
                    self.p_path_lc_demo.lineTo(self.point_grid_step_cursor)
                    self.path_lc_demo_item.setPath(self.p_path_lc_demo)


            elif cursor == "bezier":
                if self.p_path_lc.elementCount() == 0:
                    self.p_path_lc.moveTo(copy.deepcopy(self.point_grid_step_cursor))
                    self.p_path_lc_demo.moveTo(copy.deepcopy(self.point_grid_step_cursor))
                    self.addItem(self.path_lc_demo_item)
                else:
                    if len(self.curve_points) == 0:
                        self.curve_points.insert(0, copy.deepcopy(self.point_grid_step_cursor))
                    elif len(self.curve_points) == 1:
                        self.curve_points.insert(1, copy.deepcopy(self.point_grid_step_cursor))
                    elif len(self.curve_points) == 2:
                        self.curve_points.insert(2, copy.deepcopy(self.point_grid_step_cursor))
                        self.p_path_lc.cubicTo(*self.curve_points)
                        self.p_path_lc_demo.cubicTo(*self.curve_points)
                        self.path_lc_demo_item.setPath(self.p_path_lc_demo)
                        self.curve_points.clear()

            elif cursor == "polygon":
                self.pol.append(self.point_grid_step_cursor)
                if self.pol_demo_item_is_append_to_scene:
                    self.removeItem(self.pol_demo_item)
                self.pol_demo_item.setPolygon(self.pol)
                self.addItem(self.pol_demo_item)
                self.pol_demo_item_is_append_to_scene = True
            elif cursor == "rect":
                # self.rect.setTopLeft(updated_cursor_position)
                self.rect_p0 = copy.deepcopy(self.point_grid_step_cursor)
                self.rect_demo = QtCore.QRectF()
                self.rect_demo_item = my_demo_rectangle.MyDemoRactangle(self.rect_demo)

                self.addItem(self.rect_demo_item)
            elif cursor == "circle":
                self.ellopse_p0 = copy.deepcopy(self.point_grid_step_cursor)
                self.ellopse_demo = QtCore.QRectF()
                self.ellopse_demo_item = my_demo_ellipse.MyDemoEllipse(self.ellopse_demo)

                self.addItem(self.ellopse_demo_item)
            elif cursor == "text":
                pos = copy.deepcopy(self.point_grid_step_cursor)
                text, ok = QtWidgets.QInputDialog.getText(None,  'text','Enter text')

                if ok:
                    text_item = my_text_item.MyTextItem(self.root, text)
                    # font_text = QtGui.QFont()
                    # font_text.setFamily(span.span_font)
                    # font_text.setPixelSize(int(span.span_size - abs(span.span_ascender) - abs(span.span_descender)))
                    # font_text.setPixelSize(int(span.span_origin[1] - span.span_bbox[1]))
                    # text_item.setTextWidth(span.span_size)
                    # font_text.setPointSizeF(span.span_size)
                    # text_item
                    # flags = self.flags_decomposer(span.span_flags)
                    # if 'italic' in flags:
                    #     font_text.setItalic(True)
                    # if 'bold' in flags:
                    #     font_text.setBold(True)
                    # text_item.setFont(font_text)
                    
                    text_item.setPos(pos)
                    # text_item.setPos(span.span_origin[0], span.span_origin[1] - span.span_size)
                    # text_item.setRotation(self.rotate_decompocer(line.line_dir))
                    # text_item.setDefaultTextColor(QtGui.QColor(*span.span_color))
                    # text_item.setZValue(text.block_number)
                    self.addItem(text_item)
          

            elif cursor == "img":
                img_path = QtWidgets.QFileDialog.getOpenFileName(self.root.tab_pdf_editor.graph_view, 'select image', "",'JPG(*.jpg);;PNG(*.png);;All(*)' )[0]
                if img_path != "":
                    pix = QtGui.QPixmap(img_path)
                    # pix.loadFromData(image.base_image.image)
                    # pix = pix.scaled(image.base_image.width / image.base_image.xres, image.base_image.height / image.base_image.yres)
                    # pix = pix.scaled(image.bbox[2] - image.bbox[0], image.bbox[3] - image.bbox[1])
                    # pix.scaledToHeight(image.base_image.yres)
                    # pix.scaledToWidth(image.base_image.xres)
                    img_item =  my_image.MyImage(self.root, pix)

                    # img_item.setMatrix(QtGui.QMatrix(*image.matrix))
                    img_item.setPos(event.pos())
                    # img_item.setScale
                    # text_item.setZValue(image.img[0])
                    self.addItem(img_item)

            elif cursor == "ruler":
                ...
        if button == QtCore.Qt.MouseButton.MiddleButton:
            if cursor == "arrow":
                ...
            elif cursor == "hand":
                ...
            elif cursor == "move":
                ...
            elif cursor == "pencil":
                ...
            elif cursor == "line" or cursor == "bezier":
                path_item = my_pointer_path.MyPainterPath(self.root, self.p_path_lc)
                self.addItem(path_item)
                self.p_path_lc = QtGui.QPainterPath()
                if self.p_path_lc_demo.elementCount() > 0:
                    self.removeItem(self.path_lc_demo_item)
                self.p_path_lc_demo = QtGui.QPainterPath()
                self.path_lc_demo_item = my_demo_pointer_path.MyDemoPainterPath(self.p_path_lc_demo)

            elif cursor == "polygon":       
                pol_item = my_polygon.MyPolygon(self.root, self.pol)
                pol_item.unsetCursor()
                self.addItem(pol_item)
                self.pol_demo_item_is_append_to_scene = False
                self.removeItem(self.pol_demo_item)
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
        if button == QtCore.Qt.MouseButton.LeftButton:

            self.is_mouse_left_pressed = False

            cursor = self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor

            if cursor == "arrow":
                ...
            elif cursor == "hand":
                ...
            elif cursor == "move":
                ...
            elif cursor == "pencil":
                self.p_path_pen_demo = QtGui.QPainterPath()
                # if self.p_path_lc_demo.elementCount() > 0:
                self.removeItem(self.path_pen_demo_item)
                path_item = my_pointer_path.MyPainterPath(self.root, self.p_path_pen)
                path_item.unsetCursor()
                self.p_path_pen = QtGui.QPainterPath()
                self.addItem(path_item)

            elif cursor == "line":
                ...
            elif cursor == "bezier":
                ...
            elif cursor == "polygon":
                ...
            elif cursor == "rect":
                # self.rect_demo = QtCore.QRectF()
                # self.rect_demo_item = my_demo_rectangle.MyDemoRactangle(self.rect_demo)

                self.removeItem(self.rect_demo_item)
                self.rect_p1 = copy.deepcopy(self.point_grid_step_cursor)
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
                self.removeItem(self.ellopse_demo_item)
                self.ellopse_p1 = copy.deepcopy(self.point_grid_step_cursor)
                if self.ellopse_p0.x() > self.ellopse_p1.x():
                    if self.ellopse_p0.y() > self.ellopse_p1.y():
                        self.ellopse.setBottomRight(self.ellopse_p0)
                        self.ellopse.setTopLeft(self.ellopse_p1)
                    elif self.ellopse_p0.y() < self.ellopse_p1.y():
                        self.ellopse.setTopRight(self.ellopse_p0)
                        self.ellopse.setBottomLeft(self.ellopse_p1)
                elif self.ellopse_p0.x() < self.ellopse_p1.x():
                    if self.ellopse_p0.y() > self.ellopse_p1.y():
                        self.ellopse.setBottomLeft(self.ellopse_p0)
                        self.ellopse.setTopRight(self.ellopse_p1)
                    elif self.ellopse_p0.y() < self.ellopse_p1.y():
                        self.ellopse.setBottomRight(self.ellopse_p1)
                        self.ellopse.setTopLeft(self.ellopse_p0)
                ellopse_item = my_ellopse.MyEllipseRactangle(self.root, self.ellopse)
                ellopse_item.unsetCursor()
                self.addItem(ellopse_item)
            elif cursor == "text":
                ...
            elif cursor == "ruler":
                ...
            return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None:
        
        updated_cursor_position = event.scenePos()
        cursor = self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor

        # self.point_grid_step_cursor.setY(self.round_step(updated_cursor_position.y(), self.grid_step))
        # self.point_grid_step_cursor.setX(self.round_step(updated_cursor_position.x(), self.grid_step))
            
        if updated_cursor_position.x() < 0 or updated_cursor_position.x() > self.width() or updated_cursor_position.y() < 0 or updated_cursor_position.y() > self.height():
            self.hor_line_cursor_item.hide()
            self.vert_line_cursor_item.hide()
        elif updated_cursor_position.x() >= 0 or updated_cursor_position.x() <= self.width() or updated_cursor_position.y() >= 0 or updated_cursor_position.y() <= self.height():
            self.hor_line_cursor_item.show()
            self.vert_line_cursor_item.show()
            self.point_grid_step_cursor.setY(self.round_step(updated_cursor_position.y(), self.grid_step))
            self.point_grid_step_cursor.setX(self.round_step(updated_cursor_position.x(), self.grid_step))
            
            if  self.point_grid_step_cursor.x() != self.old_point_grid_step_cursor.x() or self.point_grid_step_cursor.y() != self.old_point_grid_step_cursor.y():
                
               
                self.hor_line_cursor_item.setY(self.point_grid_step_cursor.y())
                self.vert_line_cursor_item.setX(self.point_grid_step_cursor.x())
                
                if cursor == "arrow":
                    ...
                elif cursor == "hand":
                    ...
                elif cursor == "move":
                    ...
                elif cursor == "pencil":
                    if self.is_mouse_left_pressed:
                        self.p_path_pen.lineTo(self.point_grid_step_cursor)
                        self.p_path_pen_demo.lineTo(self.point_grid_step_cursor)
                        self.path_pen_demo_item.setPath(self.p_path_pen_demo)
                elif cursor == "line":
                    ...
                elif cursor == "bezier":
                    ...
                elif cursor == "polygon":
                    ...
                elif cursor == "rect":

                    if self.rect_p0.x() > self.point_grid_step_cursor.x():
                        if self.rect_p0.y() > self.point_grid_step_cursor.y():
                            self.rect_demo.setBottomRight(self.rect_p0)
                            self.rect_demo.setTopLeft(self.point_grid_step_cursor)
                        elif self.rect_p0.y() < self.point_grid_step_cursor.y():
                            self.rect_demo.setTopRight(self.rect_p0)
                            self.rect_demo.setBottomLeft(self.point_grid_step_cursor)
                    elif self.rect_p0.x() < self.point_grid_step_cursor.x():
                        if self.rect_p0.y() > self.point_grid_step_cursor.y():
                            self.rect_demo.setBottomLeft(self.rect_p0)
                            self.rect_demo.setTopRight(self.point_grid_step_cursor)
                        elif self.rect_p0.y() < self.point_grid_step_cursor.y():
                            self.rect_demo.setBottomRight(self.point_grid_step_cursor)
                            self.rect_demo.setTopLeft(self.rect_p0)
                    self.rect_demo_item.setRect(self.rect_demo)
                elif cursor == "circle":
                    if self.ellopse_p0.x() > self.point_grid_step_cursor.x():
                        if self.ellopse_p0.y() > self.point_grid_step_cursor.y():
                            self.ellopse_demo.setBottomRight(self.ellopse_p0)
                            self.ellopse_demo.setTopLeft(self.point_grid_step_cursor)
                        elif self.ellopse_p0.y() < self.point_grid_step_cursor.y():
                            self.ellopse_demo.setTopRight(self.ellopse_p0)
                            self.ellopse_demo.setBottomLeft(self.point_grid_step_cursor)
                    elif self.ellopse_p0.x() < self.point_grid_step_cursor.x():
                        if self.ellopse_p0.y() > self.point_grid_step_cursor.y():
                            self.ellopse_demo.setBottomLeft(self.ellopse_p0)
                            self.ellopse_demo.setTopRight(self.point_grid_step_cursor)
                        elif self.ellopse_p0.y() < self.point_grid_step_cursor.y():
                            self.ellopse_demo.setBottomRight(self.point_grid_step_cursor)
                            self.ellopse_demo.setTopLeft(self.ellopse_p0)
                    self.ellopse_demo_item.setRect(self.ellopse_demo)
                elif cursor == "text":
                    ...
                elif cursor == "ruler":
                    ...

                self.old_point_grid_step_cursor = copy.deepcopy(self.point_grid_step_cursor)
        return super().mouseMoveEvent(event)

    def contextMenuEvent(self, event: QtWidgets.QGraphicsSceneContextMenuEvent) -> None:

        updated_cursor_position = event.scenePos()
        cursor = self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor

       
            
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
        cursor = self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor

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



















#     def drawBackground(self, painter: QtGui.QPainter, rect: typing.Union[QtCore.QRectF, QtCore.QRect]) -> None:
#         svg_data = '''
# <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
#     <rect width="100%" height="100%" fill="#434343" fill-opacity="1" />
#     <g fill-rule="evenodd">
#         <g fill="#979797" fill-opacity="1">
#             <path opacity=".5" d="M96 95h4v1h-4v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4h-9v4h-1v-4H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15v-9H0v-1h15V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h9V0h1v15h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9h4v1h-4v9zm-1 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm9-10v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-10 0v-9h-9v9h9zm-9-10h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9zm10 0h9v-9h-9v9z" />
#             <path d="M6 5V0H5v5H0v1h5v94h1V6h94V5H6z" />
#         </g>
#     </g>
# </svg>
#         '''.encode('utf8')

#         renderer = QSvgRenderer(svg_data)

#         renderer.render(painter, rect)


    # def drawBackground(self, qp, rect):
        # qp.translate(.5, .5)
        # self.grid_pen.setDashOffset(0.0)
        # self.grid_pen.setCosmetic(True)
        # self.grid_pen.setDashPattern([1, self.grid_step - 1])
        # qp.setPen(self.grid_pen)
        # qp.fillRect(rect, self.background_brush)

        # x, y, right, bottom = rect.toRect().getCoords()
        # x = int(x)
        # y = int(y)
        # right = int(right)
        # bottom = int(bottom)

        # top = y
        # left = x
        # step = self.grid_step
        # print(isinstance(step, int))
        # if isinstance(step, int):
        #     yrest = y % step
        #     if yrest:
        #         y += step - yrest
        #     for y in range(y, bottom, step):
        #         qp.drawLine(left, y, right, y)

        #     xrest = x % step
        #     if xrest:
        #         x += step - xrest
        #     for x in range(x, right, step):
        #         qp.drawLine(x, top, x, bottom)

























