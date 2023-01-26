import sys, re , io, math
from collections.abc import Iterable
import traceback
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import Qt
from shapely.geometry import Point, LineString, Polygon
from colormap import rgb2hex
from colormap import hex2rgb
import fitz
from PIL import Image
import  View.Window.gui_wrapper as gui_wrapper



###########################################
#########################################33
class MyQGraphicsPolygonItem(QtWidgets.QGraphicsPolygonItem):

    def __init__(self, root,  path):
        super().__init__( path)
        self.root = root

        # self.polygon().

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

        self.setAcceptHoverEvents(True)


     # mouse hover event
    def hoverEnterEvent(self, event):
        if self.root.pdf_editor_cursor == "move":
            self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        else:
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

    # def hoverLeaveEvent(self, event):
    #     self.restoreOverrideCursor()

    # mouse click event
    def mousePressEvent(self, event):
        items = self.root.pdf_editor_scene.items()
        for item in items:
            if hasattr(item, "delete_attribute_my_point_rect"):
                self.root.pdf_editor_scene.removeItem(item)

    def mouseDoubleClickEvent(self, event):
        if self.root.pdf_editor_cursor == "hand":
            # print(self.root.pdf_editor_cursor)
            p = self.path()
            # g = QtWidgets.QGraphicsItemGroup()
            # g = []
            # self.setGroup
            for ii in range(self.path().elementCount()):
                x = p.elementAt(ii).x
                y = p.elementAt(ii).y
                it = QtCore.QRectF(x - 5, y - 5, 10, 10)
                # g.append(it)
                # rect_it = QtWidgets.QGraphicsRectItem()
                it_r = MyPointRect(self.root, self, ii, it)
                self.root.pdf_editor_scene.addItem(it_r)
                # p.addRect(it)
                # self.ch group().childItems
            # self.root.pdf_editor_scene.createItemGroup(g)
            # self.setGroup(g)
            # self.setPath(p)

    def contextMenuEvent(self, event):
        # event.scenePos
        menu = MyContextMenu(self.root)

        action_properties = menu.addAction("properties")
        menu.addSeparator()
        action_cut = menu.addAction("cut")
        action_copy = menu.addAction("copy")
        action_paste = menu.addAction("paste")
        action_duplicate = menu.addAction("duplicate")
        action_delete = menu.addAction("delete")
        menu.addSeparator()
        action_to_Front = menu.addAction("to Front")
        action_to_back = menu.addAction("to back")
        menu.addSeparator()
        action_rotate = menu.addAction("rotate")
        action_scale = menu.addAction("scale")
        action_flip_vertically = menu.addAction("flip vertically")
        action_flip_horizontally = menu.addAction("flip horizontally")
        menu.addSeparator()
        action_group = menu.addAction("group")
        action_ungroup = menu.addAction("ungroup")
        # menu.addSeparator()
        # action_set_parent = menu.addAction("set parent")
        # action_no_children = menu.addAction("no children")
    
        selected_action = menu.exec_(event.screenPos())

        if selected_action == action_properties:
            settings =  gui_wrapper.MyPdfEditorDialogSettingsPathItem(self.root)
            settings.exec()

        elif selected_action == action_rotate:
            rot =  gui_wrapper.MyPdfEditorDialogRotatePathItem(self.root)
            if rot.exec_():
                self.rotation_centr(rot.val_rotate)


        elif selected_action == action_scale:
            scl =  gui_wrapper.MyPdfEditorDialogScalePathItem(self.root)
            if scl.exec_():
                self.scale_centr(scl.val_scale)

        elif selected_action == action_flip_vertically:
            self.flip_vertically_centr()

        elif selected_action == action_flip_horizontally:
            self.flip_horizontally_centr()

        elif selected_action == action_cut:
            pass
        elif selected_action == action_copy:
            pass
        elif selected_action == action_paste:
            pass
        elif selected_action == action_duplicate:
            pass

        elif selected_action == action_delete:
            self.root.pdf_editor_scene.removeItem(self)

        elif selected_action == action_to_Front:
            pass
        elif selected_action == action_to_back:
            pass
        elif selected_action == action_group:
            pass
        elif selected_action == action_ungroup:
            pass


    def mouseMoveEvent(self, event):
        if self.root.pdf_editor_cursor == "move":
            # self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
            orig_cursor_position = event.lastScenePos()
            updated_cursor_position = event.scenePos()

            dev_x = updated_cursor_position.x() - orig_cursor_position.x()
            dev_y = updated_cursor_position.y() - orig_cursor_position.y()
            p = self.path()
            for ii in range(self.path().elementCount()):
                x = p.elementAt(ii).x
                y = p.elementAt(ii).y
                print(x, y)
                p.setElementPositionAt(ii, x + dev_x, y + dev_y)
            self.setPath(p)

    def mouseReleaseEvent(self, event):
        pass


    def get_centr_points(self):
        list_x = []
        list_y = []
        p = self.path()
        for ii in range(p.elementCount()):
            list_x.append(p.elementAt(ii).x)
            list_y.append(p.elementAt(ii).y)

        x_min = min(list_x)
        x_max = max(list_x)
        y_min = min(list_y)
        y_max = max(list_y)
        x_centr = x_min + (x_max - x_min) / 2
        y_centr = y_min + (y_max - y_min) / 2

        return x_centr, y_centr
 
    def rotation_centr(self, angle):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            dev_x = math.cos(math.radians(angle)) * (x-x_centr) - math.sin(math.radians(angle)) * (y-y_centr) + x_centr
            dev_y = math.sin(math.radians(angle)) * (x-x_centr) + math.cos(math.radians(angle)) * (y-y_centr) + y_centr
            p.setElementPositionAt(ii, dev_x, dev_y)
        self.setPath(p)

    def scale_centr(self, scale):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            x_to_centr = x_centr - x
            y_to_centr = y_centr - y
            dev_x = x_to_centr * scale / 100
            dev_y = y_to_centr * scale / 100
            p.setElementPositionAt(ii, x_centr - dev_x, y_centr - dev_y)
        self.setPath(p)

    def flip_vertically_centr(self):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            dev_y = y_centr - y
            p.setElementPositionAt(ii, x, y_centr + dev_y)
        self.setPath(p)

    def flip_horizontally_centr(self):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            dev_x = x_centr - x
            p.setElementPositionAt(ii, x_centr + dev_x, y)
        self.setPath(p)





class MyContextMenu(QtWidgets.QMenu):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setStyleSheet(self.root.styleSheet())

class MyPointRect(QtWidgets.QGraphicsRectItem):
    
    def __init__(self, root, el, num_point, rectF):
        super().__init__(rectF)
        # self.rectF = rectF
        self.num_point = num_point
        self.root = root
        self.el = el
        self.delete_attribute_my_point_rect = True
        self.setZValue(999999999)
        self.setBrush(QtGui.QColor(255, 255, 255, 255))
        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)


        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()

        dev_x = updated_cursor_position.x() - orig_cursor_position.x()
        dev_y = updated_cursor_position.y() - orig_cursor_position.y()

        self.setRect(self.rect().x() + dev_x, self.rect().y() + dev_y, self.rect().width(), self.rect().height(), )
        p = self.el.path()
        # for ii in range(self.path().elementCount()):
        x = p.elementAt(self.num_point).x
        y = p.elementAt(self.num_point).y
        p.setElementPositionAt(self.num_point, x + dev_x, y + dev_y)
        self.el.setPath(p)


    


class MyPainterPath(QtWidgets.QGraphicsPathItem):

    def __init__(self, root,  path):
        super().__init__( path)
        self.root = root
        
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

        self.setAcceptHoverEvents(True)


     # mouse hover event
    def hoverEnterEvent(self, event):
        if self.root.pdf_editor_cursor == "move":
            self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        else:
            self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

    # def hoverLeaveEvent(self, event):
    #     self.restoreOverrideCursor()

    # mouse click event
    def mousePressEvent(self, event):
        items = self.root.pdf_editor_scene.items()
        for item in items:
            if hasattr(item, "delete_attribute_my_point_rect"):
                self.root.pdf_editor_scene.removeItem(item)

    def mouseDoubleClickEvent(self, event):
        if self.root.pdf_editor_cursor == "hand":
            # print(self.root.pdf_editor_cursor)
            p = self.path()
            # g = QtWidgets.QGraphicsItemGroup()
            # g = []
            # self.setGroup
            for ii in range(self.path().elementCount()):
                x = p.elementAt(ii).x
                y = p.elementAt(ii).y
                it = QtCore.QRectF(x - 5, y - 5, 10, 10)
                # g.append(it)
                # rect_it = QtWidgets.QGraphicsRectItem()
                it_r = MyPointRect(self.root, self, ii, it)
                self.root.pdf_editor_scene.addItem(it_r)
                # p.addRect(it)
                # self.ch group().childItems
            # self.root.pdf_editor_scene.createItemGroup(g)
            # self.setGroup(g)
            # self.setPath(p)

    def contextMenuEvent(self, event):
        # event.scenePos
        menu = MyContextMenu(self.root)

        action_properties = menu.addAction("properties")
        menu.addSeparator()
        action_cut = menu.addAction("cut")
        action_copy = menu.addAction("copy")
        action_paste = menu.addAction("paste")
        action_duplicate = menu.addAction("duplicate")
        action_delete = menu.addAction("delete")
        menu.addSeparator()
        action_to_Front = menu.addAction("to Front")
        action_to_back = menu.addAction("to back")
        menu.addSeparator()
        action_rotate = menu.addAction("rotate")
        action_scale = menu.addAction("scale")
        action_flip_vertically = menu.addAction("flip vertically")
        action_flip_horizontally = menu.addAction("flip horizontally")
        menu.addSeparator()
        action_group = menu.addAction("group")
        action_ungroup = menu.addAction("ungroup")
        # menu.addSeparator()
        # action_set_parent = menu.addAction("set parent")
        # action_no_children = menu.addAction("no children")
    
        selected_action = menu.exec_(event.screenPos())

        if selected_action == action_properties:
            settings =  gui_wrapper.MyPdfEditorDialogSettingsPathItem(self.root)
            settings.exec()

        elif selected_action == action_rotate:
            rot =  gui_wrapper.MyPdfEditorDialogRotatePathItem(self.root)
            if rot.exec_():
                self.rotation_centr(rot.val_rotate)


        elif selected_action == action_scale:
            scl =  gui_wrapper.MyPdfEditorDialogScalePathItem(self.root)
            if scl.exec_():
                self.scale_centr(scl.val_scale)

        elif selected_action == action_flip_vertically:
            self.flip_vertically_centr()

        elif selected_action == action_flip_horizontally:
            self.flip_horizontally_centr()

        elif selected_action == action_cut:
            pass
        elif selected_action == action_copy:
            pass
        elif selected_action == action_paste:
            pass
        elif selected_action == action_duplicate:
            pass

        elif selected_action == action_delete:
            self.root.pdf_editor_scene.removeItem(self)

        elif selected_action == action_to_Front:
            pass
        elif selected_action == action_to_back:
            pass
        elif selected_action == action_group:
            pass
        elif selected_action == action_ungroup:
            pass


    def mouseMoveEvent(self, event):
        if self.root.pdf_editor_cursor == "move":
            # self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
            orig_cursor_position = event.lastScenePos()
            updated_cursor_position = event.scenePos()

            dev_x = updated_cursor_position.x() - orig_cursor_position.x()
            dev_y = updated_cursor_position.y() - orig_cursor_position.y()
            p = self.path()
            for ii in range(self.path().elementCount()):
                x = p.elementAt(ii).x
                y = p.elementAt(ii).y
                print(x, y)
                p.setElementPositionAt(ii, x + dev_x, y + dev_y)
            self.setPath(p)

    def mouseReleaseEvent(self, event):
        pass


    def get_centr_points(self):
        list_x = []
        list_y = []
        p = self.path()
        for ii in range(p.elementCount()):
            list_x.append(p.elementAt(ii).x)
            list_y.append(p.elementAt(ii).y)

        x_min = min(list_x)
        x_max = max(list_x)
        y_min = min(list_y)
        y_max = max(list_y)
        x_centr = x_min + (x_max - x_min) / 2
        y_centr = y_min + (y_max - y_min) / 2

        return x_centr, y_centr
 
    def rotation_centr(self, angle):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            dev_x = math.cos(math.radians(angle)) * (x-x_centr) - math.sin(math.radians(angle)) * (y-y_centr) + x_centr
            dev_y = math.sin(math.radians(angle)) * (x-x_centr) + math.cos(math.radians(angle)) * (y-y_centr) + y_centr
            p.setElementPositionAt(ii, dev_x, dev_y)
        self.setPath(p)

    def scale_centr(self, scale):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            x_to_centr = x_centr - x
            y_to_centr = y_centr - y
            dev_x = x_to_centr * scale / 100
            dev_y = y_to_centr * scale / 100
            p.setElementPositionAt(ii, x_centr - dev_x, y_centr - dev_y)
        self.setPath(p)

    def flip_vertically_centr(self):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            dev_y = y_centr - y
            p.setElementPositionAt(ii, x, y_centr + dev_y)
        self.setPath(p)

    def flip_horizontally_centr(self):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            dev_x = x_centr - x
            p.setElementPositionAt(ii, x_centr + dev_x, y)
        self.setPath(p)












class ConvertDraw():


    # start_line = [0, 0]
    # end_line = [0, 0]
    # start_curve = [0, 0]
    # end_curve = [0, 0]

    def __init__(self, root):
        self.root = root


    def convert_even_odd(self, even_odd):
        if even_odd:
            return Qt.FillRule.OddEvenFill
        else:
            return  Qt.FillRule.WindingFill


    def convert_line_join(self, line_join):
        if line_join == 0:
            return Qt.PenJoinStyle.BevelJoin
        elif line_join == 1:
            return Qt.PenJoinStyle.RoundJoin
        else:
            return Qt.PenJoinStyle.MiterJoin

    def convert_line_cap(self, line_cap):
        if line_cap == 2:
            return Qt.PenCapStyle.SquareCap
        elif line_cap == 1:
            return Qt.PenCapStyle.RoundCap
        else:
            return Qt.PenCapStyle.FlatCap

    def convert_dashes(self, dashes: str):
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



    def convert_path(self, path, scene):
        start_path = 0
        end_path = len(path["items"]) - 1
        current_path = 0
        path_l_c = QtGui.QPainterPath()
        path_pol = QtGui.QPainterPathStroker()
        
        p_start = QtCore.QPointF(0.0, 0.0)
        p_end = QtCore.QPointF(0.0, 0.0)

        for p in path["items"]:

            if p[0] == "l":
                p0 = QtCore.QPointF(p[1].x, p[1].y)
                p1 = QtCore.QPointF(p[2].x, p[2].y)
                if current_path == start_path:
                    p_start = p0
                    path_l_c.moveTo(p0)
                    path_l_c.lineTo(p1)
                # elif current_path == end_path:
                #     pass
                else:
                    # path_l_c.moveTo(p0)
                    path_l_c.lineTo(p1)

                if current_path == end_path:
                    p_end = p1

            if p[0] == "c":
                
                p0 = QtCore.QPointF(p[1].x, p[1].y)
                p1 = QtCore.QPointF(p[2].x, p[2].y)
                p2 = QtCore.QPointF(p[3].x, p[3].y)
                p3 = QtCore.QPointF(p[4].x, p[4].y)
                if current_path == start_path:
                    p_start = p0
                    path_l_c.moveTo(p0)
                    # path_l_c.cubicTo(p1, p2, p3)
                    path_l_c.cubicTo(p1, p2, p3)
     
                # elif current_path == end_path:
                #     pass
                else:
                    # path_l_c.moveTo(p0)
                    path_l_c.cubicTo(p1, p2, p3)

                if current_path == end_path:
                    p_end = p3
            
                
            if p[0] == "re":
                # rect = QtCore.QRectF(QtCore.QPointF(p[1][0], p[1][1]), QtCore.QPointF(p[1][2], p[1][3]))
                # path_l_c.addRect(p[1][0], p[1][1], p[1][2] - p[1][0], p[1][3] - p[1][1])
                rect = QtCore.QRectF(p[1][0], p[1][1], p[1][2] - p[1][0], p[1][3] - p[1][1])
                path_l_c.addRect(rect)
                # p0 = QtCore.QPointF(p[1][0], p[1][1])
                # p1 = QtCore.QPointF(p[1][2], p[1][1])
                # p2 = QtCore.QPointF(p[1][2], p[1][3])
                # p3 = QtCore.QPointF(p[1][0], p[1][3])
                if current_path == start_path:
                    p_start = QtCore.QPointF(p[1][0], p[1][1])
                #     path_l_c.moveTo(p0)
                #     path_l_c.lineTo(p1)
                #     path_l_c.lineTo(p2)
                #     path_l_c.lineTo(p3)
                #     # path_l_c.lineTo(p0)
                # # elif current_path == end_path:
                # #     pass
                # else:
                #     path_l_c.lineTo(p0)
                #     path_l_c.lineTo(p1)
                #     path_l_c.lineTo(p2)
                #     path_l_c.lineTo(p3)
                    # path_l_c.lineTo(p0)
                # if current_path == end_path:
                #     p_end = p0

            if p[0] == "qun":
                # quad = QtCore.
                
                p0 = QtCore.QPointF(p[1][0][0], p[1][0][1])
                p1 = QtCore.QPointF(p[1][1][0], p[1][1][1])
                p2 = QtCore.QPointF(p[1][2][0], p[1][2][1])
                p3 = QtCore.QPointF(p[1][3][0], p[1][3][1])
                # rect = QtCore.QRectF(p0, p2)
                # path_l_c.addRect(rect)
                if current_path == start_path:
                    p_start = p0
                    path_l_c.moveTo(p0)
                    path_l_c.lineTo(p1)
                    path_l_c.lineTo(p3)
                    path_l_c.lineTo(p2)
                    path_l_c.lineTo(p0)
                # elif current_path == end_path:
                #     pass
                else:
                    path_l_c.moveTo(p0)
                    path_l_c.lineTo(p1)
                    path_l_c.lineTo(p3)
                    path_l_c.lineTo(p2)
                    path_l_c.lineTo(p0)

                # if current_path == end_path:
                #     p_end = p0
                # if current_path == end_path:
                #     path_l_c.lineTo(p_start)

            # if path["closePath"]:
            #     path_l_c.lineTo(p_start)
            # path_l_c.toFillPolygon()
            # path_l_c.closeSubpath()

            current_path += 1
        if path["closePath"]:
            path_l_c.lineTo(p_start)
            # path_l_c.toFillPolygon()

        path_l_c.setFillRule(self.convert_even_odd(path["even_odd"]))
        # path_l_c.addEllipse()
        # path_l_c.addPolygon()
        # path_l_c.addRect()
        # path_l_c.addRegion()
        # path_l_c.addRoundedRect()
        # path_l_c.addText()
     
            # path_l_c.closeSubpath()


        dashes_pattern, dashes_offset = self.convert_dashes(path["dashes"])
        # print(dashes_pattern, dashes_offset, path["dashes"])
        # 'type': 'fs', 'stroke_opacity': 1.0, 'color': (1.0, 0.0, 0.0), 'width': 1.5, 'lineCap': (2, 2, 2), 'lineJoin': 0.0, 'dashes': '[ 0 3 ] 0', 'rect': Rect(600.0, 15.0, 667.5, 82.5), 'seqno': 8, 'even_odd': False, 'fill_opacity': 1.0, 'closePath': False, 'fill': (0.0, 0.0, 1.0)
        
        # path_item = scene.addPath(path_l_c)
        point_pol = []
        p = path_l_c
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            point_pol.append(QtCore.QPointF(x, y))

        path_item = MyPainterPath(self.root, path_l_c)
        pol_item = QtWidgets.QGraphicsPolygonItem(QtGui.QPolygonF(point_pol))
        scene.addItem(path_item)
        path_item.setZValue(path["seqno"])
        scene.addItem(pol_item)
        pol_item.setZValue(path["seqno"])

    
        # path_brush = QtGui.QBrush(QtGui.QColor(*list(map(lambda x: 255 - int(x * 255) , path["fill"]))))
        if "f" in path["type"]:
            # path_brush = QtGui.QBrush()
            # path_brush.colo setColor(QtGui.QColor.fromRgbF(*path["fill"], path["fill_opacity"]))
            path_brush = QtGui.QBrush(QtGui.QColor.fromRgbF(*path["fill"], path["fill_opacity"]))
            path_item.setBrush(path_brush)
            pol_item.setBrush(path_brush)


        if "s" in path["type"]:   
            path_pen = QtGui.QPen()
            path_pen.setColor(QtGui.QColor.fromRgbF(*path["color"], path["stroke_opacity"]))
            path_pen.setWidthF(path["width"])
            path_pen.setDashOffset(dashes_offset)
            path_pen.setDashPattern (dashes_pattern)
            path_pen.setJoinStyle(self.convert_line_join(path["lineJoin"]) )
            path_pen.setCapStyle(self.convert_line_cap(path["lineCap"]))
            path_item.setPen(path_pen)
            pol_item.setPen(path_pen)

            # path_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable , True)
            # path_item.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable , True)
            # path_item.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
            # if path["closePath"]:
            #     # path_l_c.lineTo(p_start)
            #     pol_item = QtWidgets.QGraphicsPolygonItem(path_l_c.toFillPolygon())
            #     scene.addItem(pol_item)


               



        

       # print(type(rect_item.pen()), rect_item.pen().__dir__())
                # print(type(rect_item.brush()), rect_item.brush().__dir__())
                # rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
                # rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
                # rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)

# Qt.NoBrush Нет рисунка кистью.
# Qt.SolidPattern Однородный цвет.
# Qt.Dense1Pattern Чрезвычайно плотный рисунок кисти.
# Qt.Dense2Patternv Очень плотный рисунок кисти.

# Qt.Dense3Pattern  Несколько плотный рисунок кисти.

# Qt.Dense4Pattern Наполовину плотный рисунок кисти.

# Qt.Dense5Pattern Несколько скудный рисунок кисти.

# Qt.Dense6Pattern Очень редкий рисунок кисти.

# Qt.Dense7Pattern  Чрезвычайно редкий рисунок кисти.

# Qt.HorPattern Горизонтальные линии.

# Qt.VerPattern Вертикальные линии.

# Qt.CrossPattern Пересечение горизонтальных и вертикальных линий.

# Qt.BDiagPattern Обратная диагональная линия.

# Qt.FDiagPattern Диагональные линии вперед.

# Qt.DiagCrossPattern Пересечение диагональных линий.

# Qt.LinearGradientPattern Линейный градиент (устанавливается с помощью специального QBrushконструктора).

# Qt.ConicalGradientPattern  Конический градиент (устанавливается с помощью специального QBrushконструктора).

# Qt.RadialGradientPattern Радиальный градиент (устанавливается с помощью специального QBrushконструктора).
# Qt.TexturePattern Пользовательский шаблон (см setTexture(). ).

# closePath



# color



# dashes



# even_odd



# fill



# items



# lineCap



# lineJoin



# fill_opacity



# stroke_opacity



# rect



# seqno



# type



# width


                # path_item = scene.addPath(path_curve)
                # path_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
                # path_item.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
                # path_item.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
                # print(type(path_item.pen().color()), path_item.pen().color())
                # print(type(path_item.pen().widthF()), path_item.pen().widthF())
                # print(type(path_item.pen().capStyle()), path_item.pen().capStyle())
                # print(type(path_item.pen().joinStyle()), path_item.pen().joinStyle())
                # print(type(path_item.pen().style()), path_item.pen().style())
                # print(type(path_item.pen().dashOffset()), path_item.pen().dashOffset())
                # print(type(path_item.pen().dashPattern()), path_item.pen().dashPattern())
                # print(type(path_item.brush()), path_item.brush().__dir__())
                # if path["color"] is not None and path["width"] is not None:
                #     path_item.setPen(QtGui.QPen(QtGui.QColor(*list(map(lambda x: 255 - int(x * 255) , path["color"]))), path["width"]))
                # if path["lineCap"][0] is not None:
                #     path_item.pen().setCapStyle(QtCore.Qt.PenCapStyle(path["lineCap"][0]))
                # if path["lineJoin"] is not None:
                #     path_item.pen().setJoinStyle(QtCore.Qt.PenJoinStyle(path["lineJoin"]))

     
#  class GraphicsItemFlag(int):
#         ItemIsMovable = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemIsSelectable = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemIsFocusable = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemClipsToShape = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemClipsChildrenToShape = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemIgnoresTransformations = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemIgnoresParentOpacity = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemDoesntPropagateOpacityToChildren = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemStacksBehindParent = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemUsesExtendedStyleOption = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemHasNoContents = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemSendsGeometryChanges = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemAcceptsInputMethod = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemNegativeZStacksBehindParent = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemIsPanel = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemSendsScenePositionChanges = ... # type: QGraphicsItem.GraphicsItemFlag
#         ItemContainsChildrenInShape = ... # type: QGraphicsItem.GraphicsItemFlag

#     class GraphicsItemChange(int):
#         ItemPositionChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemMatrixChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemVisibleChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemEnabledChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemSelectedChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemParentChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemChildAddedChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemChildRemovedChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemTransformChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemPositionHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemTransformHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemSceneChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemVisibleHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemEnabledHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemSelectedHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemParentHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemSceneHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemCursorChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemCursorHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemToolTipChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemToolTipHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemFlagsChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemFlagsHaveChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemZValueChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemZValueHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemOpacityChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemOpacityHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemScenePositionHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemRotationChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemRotationHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemScaleChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemScaleHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemTransformOriginPointChange = ... # type: QGraphicsItem.GraphicsItemChange
#         ItemTransformOriginPointHasChanged = ... # type: QGraphicsItem.GraphicsItemChange
