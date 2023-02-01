import math
from PySide2 import QtWidgets, QtGui,  QtCore 
import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

# import src.View.my_window.main_window as main_window
# import src.View.my_widgets.pdf_editor.graphic.rectangle.my_point_rect_rect as my_point_rect_rect
# import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
# import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_path as my_dialog_settings_path
# import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
# import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale

import src.View.my_widgets.pdf_editor.paint.rectangle.my_point_ellipce_rect


class MyRactangle(QtWidgets.QGraphicsRectItem):
    """Класс переопределяющий QtWidgets.QGraphicsRectItem
        Класс предназначен для демострации формы фигуры 
        при ее отрисовке
    """
    def __init__(self, rect: QtCore.QRectF):
        super().__init__( rect)
        self.list_point_rect: list[str] = ["top", "bottom", "left", "right"]
        
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
      
        self.setAcceptHoverEvents(True)


  