import math
import copy
from PySide6 import QtWidgets, QtGui,  QtCore 
import my_os_path as my_os_path
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_point_rect_rect as my_point_rect_rect
import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_path as my_dialog_settings_path
import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale




class MyEllipseRactangle(QtWidgets.QGraphicsEllipseItem):
    """Класс переопределяющий QtWidgets.QGraphicsEllipseItem
        Вклассе добавленны функции для взаимодействия пользователя с 
        отрисованными экземплярами класса на графической сцене
    """
    def __init__(self, root: QtWidgets,  rect: QtCore.QRectF):
        super().__init__( rect)
        self.root: QtWidgets = root
        self.list_point_rect: list[str] = ["top", "bottom", "left", "right"]
        self.orig_cursor_position =  QtCore.QPointF()
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        # self.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        size_cursor = QtCore.QSize(32, 32)
        self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_rectangle_itemt.png")
        self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        self.setCursor(self.current_cursor)

        all_size_size_cursor = QtCore.QSize(64, 128)
        self.all_size_cursor_pix = QtGui.QPixmap(icon_svg_dir + "all_size_rect_item.png")
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
            p = self.rect()
            x = p.x() 
            y = p.y()
            w = p.width()
            h = p.height()
            for ii in self.list_point_rect:
                if ii == "top":
                    x0 = x + w/2
                    y0 = y
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_top = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
                    self.root.tab_pdf_editor.graph_scene.addItem(rect_top)
                if ii == "bottom":
                    x0 = x + w/2
                    y0 = y + h
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_bottom = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
                    self.root.tab_pdf_editor.graph_scene.addItem(rect_bottom)
                if ii == "left":
                    x0 = x
                    y0 = y + h/2
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_left = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
                    self.root.tab_pdf_editor.graph_scene.addItem(rect_left)
                if ii == "right":
                    x0 = x + w
                    y0 = y + h/2
                    it = QtCore.QRectF(x0 - 5, y0 - 5, 10, 10)
                    rect_right = my_point_rect_rect.MyPointRectRect(self.root, self, ii, it)
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
        # action_rotate = menu.addAction("rotate")
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
            settings =  my_dialog_settings_path.MyDialogSettingsPath(self.root)
            settings.exec()

        # elif selected_action == action_rotate:
        #     rot =  my_rotate.MyDialogRotatePath(self.root)
        #     if rot.exec_():
        #         self.rotation_centr(rot.val_rotate)


        elif selected_action == action_scale:
            scl =  my_scale.MyDialogScalePath(self.root)
            if scl.exec_():
                self.scale_centr(scl.val_scale)

        elif selected_action == action_cut:
            pass
        elif selected_action == action_copy:
            self.root.tab_pdf_editor.graph_scene.buffer_copy_item =  MyEllipseRactangle(self.root, self.rect())
            self.root.tab_pdf_editor.graph_scene.buffer_copy_item.setPen(self.pen())
            self.root.tab_pdf_editor.graph_scene.buffer_copy_item.setBrush(self.brush())
            self.root.tab_pdf_editor.graph_scene.buffer_copy_item.setZValue(self.zValue() + 0.000001)
        
        elif selected_action == action_paste:
            if isinstance(self.root.tab_pdf_editor.graph_scene.buffer_copy_item, my_rectangle.MyRactangle):
                rect_f = self.root.tab_pdf_editor.graph_scene.buffer_copy_item.rect()
                w = copy.deepcopy(rect_f.width())
                h = copy.deepcopy(rect_f.height())

                rect_f.setX(copy.deepcopy(event.scenePos().x()))
                rect_f.setY(copy.deepcopy(event.scenePos().y()))
                rect_f.setWidth(w)
                rect_f.setHeight(h)

                rect_item = my_rectangle.MyRactangle(self.root, rect_f)
                rect_item.setPen(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.pen())
                rect_item.setBrush(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.brush())
                rect_item.setZValue(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.zValue())
                self.root.tab_pdf_editor.graph_scene.addItem(rect_item)
            
            elif isinstance(self.root.tab_pdf_editor.graph_scene.buffer_copy_item, MyEllipseRactangle):
                rect_f = self.root.tab_pdf_editor.graph_scene.buffer_copy_item.rect()
                w = copy.deepcopy(rect_f.width())
                h = copy.deepcopy(rect_f.height())

                rect_f.setX(copy.deepcopy(event.scenePos().x()))
                rect_f.setY(copy.deepcopy(event.scenePos().y()))
                rect_f.setWidth(w)
                rect_f.setHeight(h)

                ellipse_item = MyEllipseRactangle(self.root, rect_f)
                ellipse_item.setPen(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.pen())
                ellipse_item.setBrush(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.brush())
                ellipse_item.setZValue(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.zValue())
                self.root.tab_pdf_editor.graph_scene.addItem(ellipse_item)
        
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
            
                    p = self.rect()
                    x = p.x() + dev_x
                    y = p.y() + dev_y
                    w = p.width()
                    h = p.height()
                    p.setX(x)
                    p.setY(y)
                    p.setWidth(w)
                    p.setHeight(h)
                    self.setRect(p)
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
        p = self.rect()
        pc = p.center()
        return pc.x(), pc.y()
 
    # def rotation_centr(self, angle: int):
    #     x_centr, y_centr = self.get_centr_points()
    #     p = self.path()
    #     for ii in range(p.elementCount()):
    #         x = p.elementAt(ii).x
    #         y = p.elementAt(ii).y
    #         dev_x = math.cos(math.radians(angle)) * (x-x_centr) - math.sin(math.radians(angle)) * (y-y_centr) + x_centr
    #         dev_y = math.sin(math.radians(angle)) * (x-x_centr) + math.cos(math.radians(angle)) * (y-y_centr) + y_centr
    #         p.setElementPositionAt(ii, dev_x, dev_y)
    #     self.setPath(p)

    def scale_centr(self, scale: float):
        x_centr, y_centr = self.get_centr_points()
        p = self.rect()
        w2 = p.width() / 2
        h2 = p.height() / 2
        p2 = QtCore.QRectF()
        p2.setTopLeft(QtCore.QPointF(x_centr - w2 * scale, y_centr - h2 * scale))
        p2.setBottomRight(QtCore.QPointF(x_centr + w2 * scale, y_centr + h2 * scale))
        self.setRect(p2)

 