import math
import copy
from PySide6 import QtWidgets, QtGui,  QtCore 

import src.View.my_widgets.pdf_editor.graphic.rectangle.my_point_rect_rect as my_point_rect_rect
import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
import src.View.my_widgets.pdf_editor.dialog.my_dialog_prop_text as my_dialog_prop_text
import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale
import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg



class MyTextItem(QtWidgets.QGraphicsTextItem):
    """Класс переопределяющий QtWidgets.QGraphicsTextItem
        В классе добавленны функции для взаимодействия пользователя с 
        отрисованными экземплярами класса на графической сцене
    """
    def __init__(self, root: QtWidgets,  text: str):
        super().__init__( text)
        self.text = text
        self.root = root
        self.list_point_rect = ["top", "bottom", "left", "right"]
        self.orig_cursor_position =  QtCore.QPointF()

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

        # self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        size_cursor = QtCore.QSize(32, 32)
        self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_text_itemt.png")
        self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        self.setCursor(self.current_cursor)

        all_size_size_cursor = QtCore.QSize(64, 128)
        self.all_size_cursor_pix = QtGui.QPixmap(icon_svg_dir + "all_size_text_item.png")
        self.all_size_cursor_scaled_pix = self.all_size_cursor_pix.scaled(all_size_size_cursor, QtCore.Qt.KeepAspectRatio)
        self.all_size_cursor = QtGui.QCursor(self.all_size_cursor_scaled_pix, -1, -1)

        self.setAcceptHoverEvents(True)

        # self.font().te

    def setPlainText(self, p_text: str) -> None:
        self.text = p_text
        return super().setPlainText(p_text)


     # mouse hover event
    def hoverEnterEvent(self, event):
        pass
        # if self.root.pdf_editor_cursor == "move":
        #     self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        # else:
        #     self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

    # def hoverLeaveEvent(self, event):
    #     self.restoreOverrideCursor()

    # mouse click event
    def mousePressEvent(self, event):
        items = self.root.tab_pdf_editor.graph_scene.items()
        for item in items:
            if hasattr(item, "delete_attribute_my_point_rect"):
                self.root.tab_pdf_editor.graph_scene.removeItem(item)

    def mouseDoubleClickEvent(self, event):
        if self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor == "hand":
        # if True:
            # print(self.root.pdf_editor_cursor)
      
            x = self.x() 
            y = self.y()
            # w = self.width()
            # h = self.height()
            # for ii in self.list_point_rect:
            #     if ii == "top":
            #         x0 = x + w/2
            #         y0 = y
            #         it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
            #         rect_top = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
            #         self.root.tab_pdf_editor.graph_scene.addItem(rect_top)
            #     if ii == "bottom":
            #         x0 = x + w/2
            #         y0 = y + h
            #         it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
            #         rect_bottom = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
            #         self.root.tab_pdf_editor.graph_scene.addItem(rect_bottom)
            #     if ii == "left":
            #         x0 = x
            #         y0 = y + h/2
            #         it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
            #         rect_left = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
            #         self.root.tab_pdf_editor.graph_scene.addItem(rect_left)
            #     if ii == "right":
            #         x0 = x + w
            #         y0 = y + h/2
            #         it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
            #         rect_right = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
            #         self.root.tab_pdf_editor.graph_scene.addItem(rect_right)

                
     

    def contextMenuEvent(self, event):
        # event.scenePos
        menu = my_contex_menu.MyContextMenu(self.root)

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
            settings =  my_dialog_prop_text.MyDialogPropText(self.root,self.text, self.font(), self.defaultTextColor(), self.zValue(), self.opacity())
            if settings.exec():
                self.setFont(settings.m_font)
                self.setDefaultTextColor(settings.color)
                self.setPlainText(settings.text)
                self.setZValue(settings.item_z_index)
                self.setOpacity(settings.item_opacity)


        elif selected_action == action_rotate:
            rot =  my_rotate.MyDialogRotatePath(self.root)
            if rot.exec_():
                self.rotation_centr(rot.val_rotate)


        elif selected_action == action_scale:
            scl =  my_scale.MyDialogScalePath(self.root)
            if scl.exec_():
                self.scale_centr(scl.val_scale)

        elif selected_action == action_cut:
            pass
        elif selected_action == action_copy:
            pass
        elif selected_action == action_paste:
            self.root.tab_pdf_editor.graph_scene.paste_el(event)
            
        elif selected_action == action_duplicate:
            pass

        elif selected_action == action_delete:
            self.root.tab_pdf_editor.graph_scene.removeItem(self)

        elif selected_action == action_to_Front:
            pass
        elif selected_action == action_to_back:
            pass
        elif selected_action == action_group:
            pass
        elif selected_action == action_ungroup:
            pass


    def mouseMoveEvent(self, event):
        # print(self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor)
        if self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor == "move":
 
            updated_cursor_position = self.root.tab_pdf_editor.graph_scene.point_grid_step_cursor
            # orig_cursor_position = self.root.tab_pdf_editor.graph_scene.old_point_grid_step_cursor

            if  updated_cursor_position.x() != self.orig_cursor_position.x() or updated_cursor_position.y() != self.orig_cursor_position.y():
                # print(self.root.tab_pdf_editor.graph_left_tool_bar.tool_cursor)
                if self.orig_cursor_position != QtCore.QPointF():
                    dev_x = updated_cursor_position.x() - self.orig_cursor_position.x()
                    dev_y = updated_cursor_position.y() - self.orig_cursor_position.y()
                    # p = self.rect()
                    x = self.x() + dev_x
                    y = self.y() + dev_y
                    # w = p.width()
                    # h = p.height()
                    self.setX(x)
                    self.setY(y)
                    # p.setWidth(w)
                    # p.setHeight(h)
                    # self.setRect(p)
                    # for ii in range(self.path().elementCount()):
                    #     x = p.elementAt(ii).x
                    #     y = p.elementAt(ii).y
                    #     # print(x, y)
                    #     p.setElementPositionAt(ii, x + dev_x, y + dev_y)
                    # self.setPath(p)
                self.orig_cursor_position = copy.deepcopy(updated_cursor_position)
    
    
    def mouseReleaseEvent(self, event):
        self.orig_cursor_position =  QtCore.QPointF()


    def get_centr_points(self) -> tuple[float, float]:
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
        x_centr: float = x_min + (x_max - x_min) / 2
        y_centr: float = y_min + (y_max - y_min) / 2

        return x_centr, y_centr
 
    def rotation_centr(self, angle: int):
        x_centr, y_centr = self.get_centr_points()
        p = self.path()
        for ii in range(p.elementCount()):
            x = p.elementAt(ii).x
            y = p.elementAt(ii).y
            dev_x = math.cos(math.radians(angle)) * (x-x_centr) - math.sin(math.radians(angle)) * (y-y_centr) + x_centr
            dev_y = math.sin(math.radians(angle)) * (x-x_centr) + math.cos(math.radians(angle)) * (y-y_centr) + y_centr
            p.setElementPositionAt(ii, dev_x, dev_y)
        self.setPath(p)

    def scale_centr(self, scale: float):
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

 