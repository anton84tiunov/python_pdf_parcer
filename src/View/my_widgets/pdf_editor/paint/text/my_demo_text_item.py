import math
from PySide2 import QtWidgets, QtGui,  QtCore 

# import src.View.my_widgets.pdf_editor.graphic.rectangle.my_point_rect_rect as my_point_rect_rect
# import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
# import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_path as my_dialog_settings_path
# import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
# import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale
import src.View.my_widgets.pdf_editor.paint.text.my_point_ellipce_text as my_point_ellipce_text

import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg



class MyTextItem(QtWidgets.QGraphicsTextItem):
    """Класс переопределяющий QtWidgets.QGraphicsTextItem
        Класс предназначен для демострации формы фигуры 
        при ее отрисовке
    """
    def __init__(self, text: str):
        super().__init__( text)
        self.list_point_rect = ["top", "bottom", "left", "right"]
        
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

        
        self.setAcceptHoverEvents(True)

