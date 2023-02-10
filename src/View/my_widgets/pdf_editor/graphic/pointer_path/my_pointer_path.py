import math
from PySide6 import QtWidgets, QtGui,  QtCore 
import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.pointer_path.my_point_rect_path as my_point_rect_path
import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_path as my_dialog_settings_path
import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale




class MyPainterPath(QtWidgets.QGraphicsPathItem):
    """Класс переопределяющий QtWidgets.QGraphicsPathItem
        Вклассе добавленны функции для взаимодействия пользователя с 
        отрисованными экземплярами класса на графической сцене
    """
    def __init__(self, root: QtWidgets,  path: QtGui.QPainterPath):
        super().__init__( path)
        self.root: QtWidgets = root
        
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        # self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        size_cursor = QtCore.QSize(32, 32)
        self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_pointer_payh_itemt.png")
        self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        self.setCursor(self.current_cursor)

        all_size_size_cursor = QtCore.QSize(64, 128)
        self.all_size_cursor_pix = QtGui.QPixmap(icon_svg_dir + "all_size_pointer_path_itemt.png")
        self.all_size_cursor_scaled_pix = self.all_size_cursor_pix.scaled(all_size_size_cursor, QtCore.Qt.KeepAspectRatio)
        self.all_size_cursor = QtGui.QCursor(self.all_size_cursor_scaled_pix, -1, -1)


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
                it_r = my_point_rect_path.MyPointRectPath(self.root, self, ii, it)
                self.root.tab_pdf_editor.graph_scene.addItem(it_r)
                # p.addRect(it)
                # self.ch group().childItems
            # self.root.pdf_editor_scene.createItemGroup(g)
            # self.setGroup(g)
            # self.setPath(p)

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
            settings =  my_dialog_settings_path.NyDialogSettingsPath(self.root)
            settings.exec()

        elif selected_action == action_rotate:
            rot =  my_rotate.MyDialogRotatePath(self.root)
            if rot.exec_():
                self.rotation_centr(rot.val_rotate)


        elif selected_action == action_scale:
            scl =  my_scale.MyDialogScalePath(self.root)
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
        # print(self.root.tab_pdf_editor.graph_tool_bar.tool_cursor)
        if self.root.tab_pdf_editor.graph_tool_bar.tool_cursor == "move":
            # self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
            orig_cursor_position = event.lastScenePos()
            updated_cursor_position = event.scenePos()

            dev_x = updated_cursor_position.x() - orig_cursor_position.x()
            dev_y = updated_cursor_position.y() - orig_cursor_position.y()
            p = self.path()
            for ii in range(self.path().elementCount()):
                x = p.elementAt(ii).x
                y = p.elementAt(ii).y
                # print(x, y)
                p.setElementPositionAt(ii, x + dev_x, y + dev_y)
            self.setPath(p)

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
