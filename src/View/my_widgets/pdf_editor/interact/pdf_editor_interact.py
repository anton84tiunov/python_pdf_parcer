import sys, re, math
from collections import OrderedDict
from PySide6 import QtWidgets, QtGui,  QtCore 
import asyncio
# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.tab.pdf_editor_tab as pdf_editor_tab
import src.Controller.pdf_editor.extract_el_from_pdf_controller as extract_el_from_pdf_controller
import src.View.my_widgets.pdf_editor.graphic.pointer_path.my_pointer_path as my_pointer_path
import src.View.my_widgets.pdf_editor.graphic.polygon.my_polygon as my_polygon
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.image.my_image as my_image
import src.View.my_widgets.pdf_editor.graphic.text.my_text_item as my_text_item
import src.Model.general.draw_model as drawModel
import src.Model.general.text_model as textModel



red_style = "background-color: rgb(255, 0, 0);"
green_style = "background-color: rgb(0, 255, 0);"
blue_style = "background-color: rgb(0, 0, 255);"

class GrIt(QtWidgets.QGraphicsItem):
    def __init__(self):
        super().__init__()


class PdfEditorInteract(pdf_editor_tab.TabPdfEditor):
    """класс для dpfbvjltqcndbt c GUI "PDF EDITOR" """

    def __init__(self, root: QtWidgets):
        super().__init__(root)
        self.root: QtWidgets = root
        self.controller = extract_el_from_pdf_controller.ExtractElFromPdfController()
        self.pdf_path = ""

        self.frame_menu.btn_open_pdf.clicked.connect(self.open_pdf_to_qt)
    
    def convert_even_odd(self, even_odd: bool) -> QtCore.Qt.FillRule:
        """функция для преобразования fitz(path.even odd) -> QtCore.Qt.FillRule"""
        if even_odd:
            return QtCore.Qt.FillRule.OddEvenFill
        else:
            return  QtCore.Qt.FillRule.WindingFill


    def convert_line_join(self, line_join: int)-> QtCore.Qt.PenJoinStyle:
        """функция для преобразования fitz(path.line join) -> QtCore.Qt.PenJoinStyle"""
        if line_join == 0:
            return QtCore.Qt.PenJoinStyle.BevelJoin
        elif line_join == 1:
            return QtCore.Qt.PenJoinStyle.RoundJoin
        else:
            return QtCore.Qt.PenJoinStyle.MiterJoin

    def convert_line_cap(self, line_cap: int) -> QtCore.Qt.PenCapStyle:
        """функция для преобразования fitz(path.line cap) -> QtCore.Qt.PenCapStyle"""
        if line_cap == 2:
            return QtCore.Qt.PenCapStyle.SquareCap
        elif line_cap == 1:
            return QtCore.Qt.PenCapStyle.RoundCap
        else:
            return QtCore.Qt.PenCapStyle.FlatCap

    def convert_dashes(self, dashes: str)-> tuple[list[float], int]:
        """функция для преобразования fitz(path.dashes) -> dashes_pattern, dashes_offset"""
        list_str_dashes_pattern = "[]"
        str_dashes_offset = "0"
        # print(type(dashes), dashes)
        if  isinstance(dashes, str):
            if "[" in dashes and "]" in dashes:
                list_str_dashes_pattern = re.search(r'^\[[ 0-9\.]*\]', dashes).group(0).replace("[ ", "").replace(" ]", "").split(' ')
            if any(map(str.isdigit, dashes)):
                str_dashes_offset_0 = re.search(r'\] [\d]*$', dashes)
                if str_dashes_offset_0 is not None:
                    str_dashes_offset = str_dashes_offset_0.group(0).replace("] ", "")
        dashes_pattern = []
        dashes_offset = 0
        if list_str_dashes_pattern is not None and any(map(str.isdigit, list_str_dashes_pattern)): 
            dashes_pattern = list(map(float, list_str_dashes_pattern))
            # for d_p in range(len(dashes_pattern)):
            if dashes_pattern[0] == 0.0:
                dashes_pattern[0] = 1.0
                dashes_pattern[1] = 1.0
        if  str_dashes_offset.isdigit():
            dashes_offset = int(str_dashes_offset)
        return dashes_pattern, dashes_offset

    def flags_decomposer(self, flags) -> list:
        """Make font flags human readable."""
        l = []
        if flags & 2 ** 0:
            l.append("superscript")
        if flags & 2 ** 1:
            l.append("italic")
        if flags & 2 ** 2:
            l.append("serifed")
        else:
            l.append("sans")
        if flags & 2 ** 3:
            l.append("monospaced")
        else:
            l.append("proportional")
        if flags & 2 ** 4:
            l.append("bold")
        # return ",".join(l)
        return l

    def rotate_decompocer(self, rot: tuple[float, float]) -> int:
        """функция для преобразования fitz(path.rotation text) -> угловые градусы"""
        if rot == (0.0, 1.0):
            return 90
        elif rot == (0.0, -1.0):
            return 270
        elif rot == (1.0, 0.0):
            return 0
        elif rot == (-1.0, 0.0):
            return 180
        else:
            return 0

    def open_pdf_to_qt(self):
        """функция для отрисовки компонентов извлеченных и преобразованных из  pdf  на сцене"""
        self.pdf_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open pdf', "",'Pdf(*.pdf);;All(*)' )[0]
        if self.pdf_path != "":
            items = self.graph_scene.items()
            for item in  items:
                
                if item != self.graph_scene.vert_line_cursor_item or item != self.graph_scene.hor_line_cursor_item:
                    # print(self.graph_scene.vert_line_cursor_item)
                    # print(item)
                    self.graph_scene.removeItem(item)
            # self.graph_scene.clear()
            el_draw, el_text, el_img = self.controller.open_pdf(self.pdf_path, 0)
            for draw in el_draw:
                # item = GrIt()
                if draw.items.draw == "re" or draw.items.draw == "qu":
                    p0 = QtCore.QPointF(*draw.items.cords[0][0])
                    p1 = QtCore.QPointF(*draw.items.cords[0][1])
                    p2 = QtCore.QPointF(*draw.items.cords[0][2])
                    p3 = QtCore.QPointF(*draw.items.cords[0][3])
                    # rect = QtCore.QRectF(p[1][0], p[1][1], p[1][2] - p[1][0], p[1][3] - p[1][1])
                    rect = QtCore.QRectF(p0,p2)
                    item = my_rectangle.MyRactangle(self.root, rect)
                    self.graph_scene.addItem(item)
                
                if draw.items.draw == "path" or draw.items.draw == "pol":
                    path = QtGui.QPainterPath()
                    start_path = 0
                    end_path = len(draw.items.cords) - 1
                    current_path = 0
                    for pp in draw.items.cords:
                        if pp[0] == "l":
                            if current_path == start_path:
                                path.moveTo(*pp[1][0])
                                path.lineTo(*pp[1][1])
                            else:
                                path.lineTo(*pp[1][1])
                        if pp[0] == "c":
                            if current_path == start_path:
                                path.moveTo(*pp[1][0])
                                path.cubicTo(*pp[1][1], *pp[1][2], *pp[1][3])
                            else:
                                path.cubicTo(*pp[1][1], *pp[1][2], *pp[1][3])
                        if pp[0] == "re":
                            # print(pp)
                            p0 = QtCore.QPointF(*pp[1][0])
                            p1 = QtCore.QPointF(*pp[1][1])
                            p2 = QtCore.QPointF(*pp[1][2])
                            p3 = QtCore.QPointF(*pp[1][3])
                            rect = QtCore.QRectF(p0, p2)
                            path.addRect(rect)
                            # path.addRect(*pp[1][1], *pp[1][2], *pp[1][3])
                        if pp[0] == "qu":
                            p0 = QtCore.QPointF(*pp[1][0])
                            p1 = QtCore.QPointF(*pp[1][1])
                            p2 = QtCore.QPointF(*pp[1][2])
                            p3 = QtCore.QPointF(*pp[1][3])
                            rect = QtCore.QRectF(p0, p2)
                            path.addRect(rect)

                        current_path += 1
                    # p_item = None
                    if draw.items.draw == "pol":
                        item = my_polygon.MyPolygon(self.root, path.toFillPolygon())
                        self.graph_scene.addItem(item)
                    if draw.items.draw == "path":
                        item = my_pointer_path.MyPainterPath(self.root, path)
                        self.graph_scene.addItem(item)
                    # if p_item is not None:
                    # item = self.graph_scene.addItem(p_item)
    
                
                if item is not None:
                    item.setZValue(draw.seqno)

                    dashes_pattern, dashes_offset = self.convert_dashes(draw.dashes)


                    if "f" in draw.type:
                        brush = QtGui.QBrush(QtGui.QColor.fromRgbF(*draw.fill, draw.fill_opacity))
                        item.setBrush(brush)

                    if "s" in draw.type:   
                        pen = QtGui.QPen()
                        pen.setColor(QtGui.QColor.fromRgbF(*draw.color, draw.stroke_opacity))
                        pen.setWidthF(draw.width)
                        pen.setDashOffset(dashes_offset)
                        pen.setDashPattern (dashes_pattern)
                        pen.setJoinStyle(self.convert_line_join(draw.lineJoin) )
                        pen.setCapStyle(self.convert_line_cap(draw.lineCap))
                        item.setPen(pen)

            # el_text = list(OrderedDict.fromkeys(el_text))
            # print(len(el_text))
            for text in el_text:
                # text = list(OrderedDict.fromkeys(text))
                for line in text.block_lines:
                    # line = list(OrderedDict.fromkeys(line))
                    for span in line.line_spans:
                        text_item = my_text_item.MyTextItem(self.root, span.span_text)
                        font_text = QtGui.QFont()
                        font_text.setFamily(span.span_font)
                        font_text.setPixelSize(int(span.span_size - abs(span.span_ascender) - abs(span.span_descender)))
                        # font_text.setPixelSize(int(span.span_origin[1] - span.span_bbox[1]))
                        # text_item.setTextWidth(span.span_size)
                        # font_text.setPointSizeF(span.span_size)
                        # text_item
                        flags = self.flags_decomposer(span.span_flags)
                        if 'italic' in flags:
                            font_text.setItalic(True)
                        if 'bold' in flags:
                            font_text.setBold(True)
                        text_item.setFont(font_text)
                       
                        text_item.setPos(span.span_bbox[0], span.span_bbox[1])
                        # text_item.setPos(span.span_origin[0], span.span_origin[1] - span.span_size)
                        text_item.setRotation(self.rotate_decompocer(line.line_dir))
                        text_item.setDefaultTextColor(QtGui.QColor(*span.span_color))
                        text_item.setZValue(text.block_number)
                        self.graph_scene.addItem(text_item)
          
            for image in el_img:
                pix = QtGui.QPixmap()
                pix.loadFromData(image.base_image.image)
                # pix = pix.scaled(image.base_image.width / image.base_image.xres, image.base_image.height / image.base_image.yres)
                pix = pix.scaled(image.bbox[2] - image.bbox[0], image.bbox[3] - image.bbox[1])
                # pix.scaledToHeight(image.base_image.yres)
                # pix.scaledToWidth(image.base_image.xres)
                img_item =  my_image.MyImage(self.root, pix)

                # img_item.setMatrix(QtGui.QMatrix(*image.matrix))
                img_item.setPos(image.bbox[0], image.bbox[1])
                # img_item.setScale
                text_item.setZValue(image.img[0])
                self.graph_scene.addItem(img_item)
        
        self.graph_scene.set_grid_cords(25)
                


















