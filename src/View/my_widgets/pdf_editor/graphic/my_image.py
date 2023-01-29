import math
from PySide2 import QtWidgets, QtGui,  QtCore 

import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.my_point_rect_image as my_point_rect_image
import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_path as my_dialog_settings_path
import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale




class MyImage(QtWidgets.QGraphicsPixmapItem):

    def __init__(self, root: main_window.MainWindow,  pix: QtGui.QPixmap):
        super().__init__( pix)
        self.root: main_window.MainWindow = root
        self.list_point_rect = ["top", "bottom", "left", "right"]
        
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

        self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        self.setAcceptHoverEvents(True)


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
        # if self.root.pdf_editor_cursor == "hand":
        if True:
            # print(self.root.pdf_editor_cursor)
            p = self.boundingRect()
            x = p.x() 
            y = p.y()
            w = p.width()
            h = p.height()
            for ii in self.list_point_rect:
                if ii == "top":
                    x0 = x + w/2
                    y0 = y
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_top = my_point_rect_image.MyPointRectImage(self.root, self, ii, it)
                    self.root.tab_pdf_editor.graph_scene.addItem(rect_top)
                if ii == "bottom":
                    x0 = x + w/2
                    y0 = y + h
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_bottom = my_point_rect_image.MyPointRectImage(self.root, self, ii, it)
                    self.root.tab_pdf_editor.graph_scene.addItem(rect_bottom)
                if ii == "left":
                    x0 = x
                    y0 = y + h/2
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_left = my_point_rect_image.MyPointRectImage(self.root, self, ii, it)
                    self.root.tab_pdf_editor.graph_scene.addItem(rect_left)
                if ii == "right":
                    x0 = x + w
                    y0 = y + h/2
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_right = my_point_rect_image.MyPointRectImage(self.root, self, ii, it)
                    self.root.tab_pdf_editor.graph_scene.addItem(rect_right)

                
     

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
            settings =  my_dialog_settings_path.DialogSettingsPath(self.root)
            settings.exec()

        elif selected_action == action_rotate:
            rot =  my_rotate.DialogRotatePath(self.root)
            if rot.exec_():
                self.rotation_centr(rot.val_rotate)


        elif selected_action == action_scale:
            scl =  my_scale.DialogScalePath(self.root)
            if scl.exec_():
                self.scale_centr(scl.val_scale)

        elif selected_action == action_cut:
            pass
        elif selected_action == action_copy:
            pass
        elif selected_action == action_paste:
            pass
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
        if self.root.tab_pdf_editor.graph_tool_bar.tool_cursor == "move":
            # self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
            orig_cursor_position = event.lastScenePos()
            updated_cursor_position = event.scenePos()

            dev_x = updated_cursor_position.x() - orig_cursor_position.x()
            dev_y = updated_cursor_position.y() - orig_cursor_position.y()
            p = self.pos()
            x = p.x() + dev_x
            y = p.y() + dev_y
            # w = p.width()
            # h = p.height()
            # p.setX(x)
            # p.setY(y)
            # p.setWidth(w)
            # p.setHeight(h)
            self.setPos(x, y)
            # self.setW
            # for ii in range(self.path().elementCount()):
            #     x = p.elementAt(ii).x
            #     y = p.elementAt(ii).y
            #     # print(x, y)
            #     p.setElementPositionAt(ii, x + dev_x, y + dev_y)
            # self.setPath(p)

    def mouseReleaseEvent(self, event):
        pass


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

 