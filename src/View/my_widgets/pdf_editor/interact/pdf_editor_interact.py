import sys, re, math, json
from collections import OrderedDict
import pickle
from PySide6 import QtWidgets, QtGui,  QtCore 
import asyncio
# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.tab.pdf_editor_tab as pdf_editor_tab
import src.Controller.pdf_editor.extract_el_from_pdf_controller as extract_el_from_pdf_controller
import src.View.my_widgets.pdf_editor.graphic.pointer_path.my_pointer_path as my_pointer_path
import src.View.my_widgets.pdf_editor.graphic.polygon.my_polygon as my_polygon
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.ellipse.my_ellopse as my_ellopse
import src.View.my_widgets.pdf_editor.graphic.image.my_image as my_image
import src.View.my_widgets.pdf_editor.graphic.text.my_text_item as my_text_item
import src.Model.general.draw_model as drawModel
import src.Model.general.text_model as textModel
import src.View.my_widgets.pdf_editor.graphic.my_cross_line as my_cross_line



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
        self.controller = extract_el_from_pdf_controller.ExtractElFromPdfController(self.root)
        self.pdf_path = ""
        self.pdf_editor_path_save_pdf_file = ''
        self.pdf_editor_path_save_qt_file = ''
        self.pdf_editor_path_open_qt_file = ''

        self.frame_menu.btn_open_pdf.clicked.connect(self.open_pdf_to_qt)
        self.frame_menu.dbl_sp_box_num_page.valueChanged.connect(lambda: self.open_pdf_to_qt_num_page(self.frame_menu.dbl_sp_box_num_page.value()))
        self.frame_menu.btn_save_qt.clicked.connect(self.save_qt)
        self.frame_menu.btn_open_qt.clicked.connect(self.open_qt_file)

        self.frame_menu.btn_close_qt.clicked.connect(lambda: print(sys.getsizeof(self.graph_scene.items())))


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

    def create_update_scene(self, el_rect, el_draw, el_text, el_img):

        items = self.graph_scene.items()
        for item in  items:
            
            if not hasattr(item, "attribute_cross_line"):
     
                self.graph_scene.removeItem(item)
        # self.graph_scene.clear()
        # self.graph_view.update(0, 0, 0, 0)
        # self.graph_scene.clear()
        # self.graph_scene.addItem(self.graph_scene.vert_line_cursor_item)
        # self.graph_scene.addItem(self.graph_scene.hor_line_cursor_item)
        self.graph_view.updateSceneRect(QtCore.QRectF(*el_rect))
        self.graph_scene.setSceneRect(QtCore.QRectF(*el_rect))
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
            img_item.setZValue(image.img[0])
            # img_item.pixmap()
            self.graph_scene.addItem(img_item)
    
        self.graph_scene.set_grid_cords()

    def open_pdf_to_qt(self):
        """функция для отрисовки компонентов извлеченных и преобразованных из  pdf  на сцене"""

        self.pdf_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open pdf', "",'Pdf(*.pdf);;All(*)' )[0]
        if self.pdf_path != "":
            
            page_count = self.controller.page_count(self.pdf_path)

            self.frame_menu.dbl_sp_box_num_page.setMaximum(page_count - 1)
            self.frame_menu.dbl_sp_box_num_page.setValue(0)
       
            el_rect, el_draw, el_text, el_img = self.controller.open_pdf(self.pdf_path, 0)
            self.create_update_scene(el_rect, el_draw, el_text, el_img)
                
    def open_pdf_to_qt_num_page(self, num_page):
        """функция для отрисовки компонентов извлеченных и преобразованных из  pdf  на сцене"""
        
        if self.pdf_path != "": 
            el_rect, el_draw, el_text, el_img = self.controller.open_pdf(self.pdf_path, num_page)
            self.create_update_scene(el_rect, el_draw, el_text, el_img)
                

    def save_qt(self):
        self.pdf_editor_path_save_pdf_file = QtWidgets.QFileDialog.getSaveFileName(self, 'Open pdf_ex', "",'Pdf_ex(*.pdf_ex);;All(*)' )[0]
        if self.pdf_editor_path_save_pdf_file != '':
            page_items = {}
            page_items['items'] = []

            items: QtWidgets.QGraphicsScene.items = self.graph_scene.items()

            for itm  in items:

                item: QtWidgets.QGraphicsItem = itm

                page_item = {}
        
                page_item['z_val'] = item.zValue()
                page_item['opacity'] = item.opacity()
                
                if not isinstance(item, (my_image.MyImage, my_text_item.MyTextItem)):

                    pen: QtGui.QPen = item.pen()

                    page_item['pen_c'] = pen.color().getRgbF()
                    page_item['pen_w'] = pen.widthF()
                    page_item['pen_d_o'] = pen.dashOffset()
                    page_item['pen_d_p'] = pen.dashPattern()
                    page_item['pen_j_s'] = str(pen.joinStyle()).replace("PenJoinStyle.", "")
                    page_item['pen_c_s'] = str(pen.capStyle()).replace("PenCapStyle.", "")
                    page_item['pen_m_l'] = pen.miterLimit()
                    page_item['pen_s'] = str(pen.style()).replace("PenStyle.", "")
                        

                    if not isinstance(item, (QtWidgets.QGraphicsLineItem)):
                        brush: QtGui.QBrush = item.brush()

                        page_item['brush_s'] = str(brush.style()).replace('BrushStyle.', '')
                        page_item['brush_c'] = brush.color().getRgbF()

                if isinstance(item, my_pointer_path.MyPainterPath):
        
                    page_item['i_type'] = "path"

                    # close_path = False
                    path_el_group = []
                    path = item.path()

                    for ii in range(path.elementCount()):
                        path_el = {}
                        elem = path.elementAt(ii)
                  
                        type_sub_el = ""
                        if elem.type == QtGui.QPainterPath.ElementType.MoveToElement:
                            type_sub_el = "m"
                        if elem.type == QtGui.QPainterPath.ElementType.LineToElement:
                            type_sub_el = "l"
                        if elem.type == QtGui.QPainterPath.ElementType.CurveToElement:
                            type_sub_el = "c"
                        if elem.type == QtGui.QPainterPath.ElementType.CurveToDataElement:
                            type_sub_el = "cd"

                        path_el["type"] = type_sub_el
                        path_el["x"] = elem.x
                        path_el["y"] = elem.y
                        path_el_group.append(path_el)

                    # if len(path_el_group) > 1:
                    #     if path_el_group[0] == path_el_group[-1]:
                    #         close_path = True
                    #         path_el_group.pop()
                    
                    
                    page_item['fill_r'] = str(path.fillRule()).replace("FillRule.", "")
                    # page_item['cl_path'] = close_path
                    page_item['path'] = path_el_group

                    page_items['items'].insert(0, page_item)


                elif isinstance(item, my_polygon.MyPolygon):
                    
                    page_item['i_type'] = "pol"

                    pol_el_group = []
                    pol = item.polygon()

                    for ii in range(pol.count()):
                        pol_el = {}
                        elem = pol.at(ii)

                        pol_el["x"] = elem.x()
                        pol_el["y"] = elem.y()
                        pol_el_group.append(pol_el)

                    # page_item['fill_rule'] = str(pol.fillRule()).replace("FillRule.", "")
                    # page_item['close_path'] = close_path
                    page_item['pol'] = pol_el_group

                    page_items['items'].insert(0, page_item)

                elif isinstance(item, my_rectangle.MyRactangle):
                    
                    page_item['i_type'] = "rect"

                    rect_el = {}
                    rect = item.rect()
                        
                    rect_el["x"] = rect.x()
                    rect_el["y"] = rect.y()
                    rect_el["w"] = rect.width()
                    rect_el["h"] = rect.height()

                    page_item['rect'] = rect_el

                    page_items['items'].insert(0, page_item)

                elif isinstance(item, my_ellopse.MyEllipse):
                    
                    page_item['i_type'] = "ell"

                    ell_el = {}
                    ell_rect = item.rect()
                        
                    ell_el["x"] = ell_rect.x()
                    ell_el["y"] = ell_rect.y()
                    ell_el["w"] = ell_rect.width()
                    ell_el["h"] = ell_rect.height()

                    page_item['rect'] = ell_el

                    page_items['items'].insert(0, page_item)

                elif isinstance(item, my_image.MyImage):
                    
                    page_item['i_type'] = "img"

                    pixmap = item.pixmap()
                    # convert QPixmap to bytes
                    ba = QtCore.QByteArray()
                    buff = QtCore.QBuffer(ba)
                    buff.open(QtCore.QIODevice.WriteOnly) 
                    ok = pixmap.save(buff, "PNG")
                    assert ok
                    pixmap_bytes = ba.data()
                    # print(type(pixmap_bytes))
                    str_img = pixmap_bytes.decode("ISO-8859-1")
                    # print(type(str_img))

                    # print(type(str_img.encode('ISO-8859-1')))
                    # # convert bytes to QPixmap
                    # ba = QtCore.QByteArray(pixmap_bytes)
                    # pixmap = QtGui.QPixmap()
                    # ok = pixmap.loadFromData(ba, "PNG")
                    # assert ok
                    # print(type(pixmap))

                    page_item['img'] = str_img
                    rect = {}
                    b_rect = item.boundingRect()
                    p_rect = item.pos()
                    rect["x"] = p_rect.x()
                    rect["y"] = p_rect.y()
                    rect["w"] = b_rect.width()
                    rect["h"] = b_rect.height()
                    page_item['rect'] = rect

                    page_items['items'].insert(0, page_item)

                elif isinstance(item, my_text_item.MyTextItem):
                    
                    page_item['i_type'] = "txt"

                    page_item['text'] = item.text
                    font_text = item.font()
                    page_item['f_family'] = font_text.family()
                    page_item['f_size'] = font_text.pixelSize()
                    page_item['f_bold'] = font_text.bold()
                    page_item['f_italic'] = font_text.italic()
                    page_item['pos'] = {}
                    page_item['pos']['x'] = item.pos().x()
                    page_item['pos']['y'] = item.pos().y()
                    page_item['rot'] = item.rotation()
                    page_item['color'] = item.defaultTextColor().getRgb()
                    # print("page_item['color']", type(page_item['color']), page_item['color'])
                    page_items['items'].insert(0, page_item)

            rect_page = self.graph_scene.sceneRect()
            page_items['rect_page'] = {}
            page_items['rect_page']['x'] = rect_page.x()
            page_items['rect_page']['y'] = rect_page.y()
            page_items['rect_page']['w'] = rect_page.width()
            page_items['rect_page']['h'] = rect_page.height()

            with open(self.pdf_editor_path_save_pdf_file, 'w') as outfile:
                json.dump(page_items, outfile)
                outfile.close()
            # print(page_items)


    def open_qt_file(self):
        self.pdf_editor_path_open_qt_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open pdf_ex', "",'Pdf_ex(*.pdf_ex);;All(*)' )[0]
        if self.pdf_editor_path_open_qt_file != '':
            # self.pdf_editor_scene.clear()

            with open(self.pdf_editor_path_open_qt_file) as json_file:
                data = json.load(json_file)

                items = self.graph_scene.items()
                for item in  items:
                    
                    if not hasattr(item, "attribute_cross_line"):
            
                        self.graph_scene.removeItem(item)
                
                # self.graph_scene.addItem(self.graph_scene.vert_line_cursor_item)
                # self.graph_scene.addItem(self.graph_scene.hor_line_cursor_item)

                rect_page = data['rect_page']
                self.graph_view.updateSceneRect(QtCore.QRectF(rect_page['x'], rect_page['y'], rect_page['w'], rect_page['h']))
                self.graph_scene.setSceneRect(QtCore.QRectF(rect_page['x'], rect_page['y'], rect_page['w'], rect_page['h']))
                self.graph_scene.set_grid_cords()

                pen =  QtGui.QPen()
                brush = QtGui.QBrush()

                for num_it in range(len(data['items'])):
                    
                    if "pen_c" in data['items'][num_it]:
             

                        pen.setColor(QtGui.QColor.fromRgbF(*data['items'][num_it]['pen_c']))
                        pen.setWidthF(data['items'][num_it]['pen_w'])
                        pen.setDashOffset(data['items'][num_it]['pen_d_o'])
                        pen.setDashPattern(data['items'][num_it]['pen_d_p'])
                        
                        pen_join_style = QtCore.Qt.PenJoinStyle()
                        p_j_s =  data['items'][num_it]['pen_j_s']
                        if  p_j_s == "MiterJoin":
                            pen.setJoinStyle(pen_join_style.MiterJoin)
                        elif  p_j_s == "BevelJoin":
                            pen.setJoinStyle(pen_join_style.BevelJoin)
                        elif  p_j_s == "RoundJoin":
                            pen.setJoinStyle(pen_join_style.RoundJoin)
                        elif  p_j_s == "SvgMiterJoin":
                            pen.setJoinStyle(pen_join_style.SvgMiterJoin)
                        elif  p_j_s == "MPenJoinStyle":
                            pen.setJoinStyle(pen_join_style.MPenJoinStyle)
                       
                        pen_cap_style = QtCore.Qt.PenCapStyle()
                        p_c_s =  data['items'][num_it]['pen_c_s']
                        if  p_c_s == "FlatCap":
                            pen.setCapStyle(pen_cap_style.FlatCap)
                        elif  p_c_s == "SquareCap":
                            pen.setCapStyle(pen_cap_style.SquareCap)
                        elif  p_c_s == "RoundCap":
                            pen.setCapStyle(pen_cap_style.RoundCap)
                        elif  p_c_s == "MPenCapStyle":
                            pen.setCapStyle(pen_cap_style.MPenCapStyle)

                        pen.setMiterLimit(data['items'][num_it]['pen_m_l'])
                        
                        pen_style = QtCore.Qt.PenStyle()
                        p_s =  data['items'][num_it]['pen_s']
                        if p_s == "NoPen":
                            pen.setStyle(pen_style.NoPen)
                        elif p_s == "SolidLine":
                            pen.setStyle(pen_style.SolidLine)
                        elif p_s == "DashLine":
                            pen.setStyle(pen_style.DashLine)
                        elif p_s == "DotLine":
                            pen.setStyle(pen_style.DotLine)
                        elif p_s == "DashDotLine":
                            pen.setStyle(pen_style.DashDotLine)
                        elif p_s == "DashDotDotLine":
                            pen.setStyle(pen_style.DashDotDotLine)
                        elif p_s == "CustomDashLine":
                            pen.setStyle(pen_style.CustomDashLine)
                        elif p_s == "MPenStyle":
                            pen.setStyle(pen_style.MPenStyle)
                    
                    if "brush_c" in data['items'][num_it]:

                        brush.setColor(QtGui.QColor.fromRgbF(*data['items'][num_it]['brush_c']))
                        brush_style = QtCore.Qt.BrushStyle()
                        b_s =  data['items'][num_it]['brush_s']

                        if b_s == "NoBrush":
                            brush.setStyle(brush_style.NoBrush)
                        elif b_s == "SolidPattern":
                            brush.setStyle(brush_style.SolidPattern)
                        elif b_s == "Dense1Pattern":
                            brush.setStyle(brush_style.Dense1Pattern)
                        elif b_s == "Dense2Pattern":
                            brush.setStyle(brush_style.Dense2Pattern)
                        elif b_s == "Dense3Pattern":
                            brush.setStyle(brush_style.Dense3Pattern)
                        elif b_s == "Dense4Pattern":
                            brush.setStyle(brush_style.Dense4Pattern)
                        elif b_s == "Dense5Pattern":
                            brush.setStyle(brush_style.Dense5Pattern)
                        elif b_s == "Dense6Pattern":
                            brush.setStyle(brush_style.Dense6Pattern)
                        elif b_s == "Dense7Pattern":
                            brush.setStyle(brush_style.Dense7Pattern)
                        elif b_s == "HorPattern":
                            brush.setStyle(brush_style.HorPattern)
                        elif b_s == "VerPattern":
                            brush.setStyle(brush_style.VerPattern)
                        elif b_s == "CrossPattern":
                            brush.setStyle(brush_style.CrossPattern)
                        elif b_s == "BDiagPattern":
                            brush.setStyle(brush_style.BDiagPattern)
                        elif b_s == "FDiagPattern":
                            brush.setStyle(brush_style.FDiagPattern)
                        elif b_s == "DiagCrossPattern":
                            brush.setStyle(brush_style.DiagCrossPattern)
                        elif b_s == "LinearGradientPattern":
                            brush.setStyle(brush_style.LinearGradientPattern)
                        elif b_s == "RadialGradientPattern":
                            brush.setStyle(brush_style.RadialGradientPattern)
                        elif b_s == "ConicalGradientPattern":
                            brush.setStyle(brush_style.ConicalGradientPattern)
                        elif b_s == "TexturePattern":
                            brush.setStyle(brush_style.TexturePattern)
         
                    if data['items'][num_it]["i_type"] == "path":
             
                        path_el_group = data['items'][num_it]['path']

                        path = QtGui.QPainterPath()

                        for i in range(len(path_el_group)):
                            pt = path_el_group[i]

                            if pt['type'] == "m":
                                path.moveTo(QtCore.QPointF(pt['x'], pt['y']))
                            if pt['type'] == "l":
                                path.lineTo(QtCore.QPointF(pt['x'], pt['y']))
                            if pt['type'] == "c":
                                c = QtCore.QPointF(pt['x'], pt['y'])
                                cd1 = QtCore.QPointF(path_el_group[i + 1]['x'], path_el_group[i + 1]['y'])
                                cd2 = QtCore.QPointF(path_el_group[i + 2]['x'], path_el_group[i + 2]['y'])
                                path.cubicTo(c, cd1, cd2)

                        path_item = my_pointer_path.MyPainterPath(self.root, path)
                        path_item.setPen(pen)
                        if brush.color() :
                            path_item.setBrush(brush)
                        self.graph_scene.addItem(path_item)

                    if data['items'][num_it]["i_type"] == "pol":
                        
                        pol_el_group = data['items'][num_it]['pol']

                        pol = QtGui.QPolygon()

                        for i in range(len(pol_el_group)):
                            pt = pol_el_group[i]
                            pol.append(QtCore.QPoint(pt['x'], pt['y']))

            
                        pol_item = my_polygon.MyPolygon(self.root, pol)
                        pol_item.setPen(pen)
                        pol_item.setBrush(brush)
                        self.graph_scene.addItem(pol_item)

                    if data['items'][num_it]["i_type"] == "rect":
                        rect_el_group = data['items'][num_it]['rect']

                        rect = QtCore.QRectF()
                        rect.setX(rect_el_group['x'])
                        rect.setY(rect_el_group['y'])
                        rect.setWidth(rect_el_group['w'])
                        rect.setHeight(rect_el_group['h'])

                        rect_item = my_rectangle.MyRactangle(self.root, rect)
                        rect_item.setPen(pen)
                        rect_item.setBrush(brush)
                        self.graph_scene.addItem(rect_item)

                    if data['items'][num_it]["i_type"] == "ell":
                        ell_el_group = data['items'][num_it]['rect']

                        ell = QtCore.QRectF()
                        ell.setX(rect_el_group['x'])
                        ell.setY(rect_el_group['y'])
                        ell.setWidth(rect_el_group['w'])
                        ell.setHeight(rect_el_group['h'])

                        ell_item = my_rectangle.MyRactangle(self.root, ell)
                        ell_item.setPen(pen)
                        ell_item.setBrush(brush)
                        self.graph_scene.addItem(ell_item)

                    if data['items'][num_it]["i_type"] == "txt":

                        text_item = my_text_item.MyTextItem(self.root, data['items'][num_it]['text'])

                        font_text = QtGui.QFont()
                        font_text.setFamily(data['items'][num_it]['f_family'])
                        font_text.setPixelSize(data['items'][num_it]['f_size'])
                        font_text.setBold(data['items'][num_it]['f_bold'])
                        font_text.setItalic(data['items'][num_it]['f_italic'])
                        text_item.setFont(font_text)
                        pos = data['items'][num_it]['pos']
                        text_item.setPos(QtCore.QPoint(pos['x'], pos['y']))
                        text_item.setRotation(data['items'][num_it]['rot'])
                        text_item.setDefaultTextColor(QtGui.QColor(*data['items'][num_it]['color']))
                        # print("data['items'][num_it]['color']", type(data['items'][num_it]['color']), data['items'][num_it]['color'])
                        # print(data['items'][num_it]['color'])
                        
                        self.graph_scene.addItem(text_item)

                    if data['items'][num_it]["i_type"] == "img":
                        
                        pixmap_bytes = data['items'][num_it]['img'].encode('ISO-8859-1')
                        # convert bytes to QPixmap
                        ba = QtCore.QByteArray(pixmap_bytes)
                        pixmap = QtGui.QPixmap()
                        ok = pixmap.loadFromData(ba, "PNG")
                        assert ok
                        img_item = my_image.MyImage(self.root, pixmap)
                        rect = data['items'][num_it]['rect']
                        img_item.setPos(QtCore.QPointF(rect["x"], rect["y"]))
                        self.graph_scene.addItem(img_item)

         
                    # if not isinstance(item, (my_pointer_path.MyPainterPath , QtWidgets.QGraphicsLineItem)):
                    #     brush: QtGui.QBrush = item.brush()

                    #     page_item['brush_s'] = str(brush.style()).replace('BrushStyle.', '')
                    #     page_item['brush_c'] = brush.color().getRgbF()


        # items = self.graph_scene.items()
        # for item in  items:
        #     self.graph_scene.removeItem(item)
        # self.graph_view.updateSceneRect(QtCore.QRectF(*el_rect))
        # self.graph_scene.setSceneRect(QtCore.QRectF(*el_rect))




