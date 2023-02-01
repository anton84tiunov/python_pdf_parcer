import math
from PySide2 import QtWidgets, QtGui,  QtCore 
import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

# import src.View.my_window.main_window as main_window
# import src.View.my_widgets.pdf_editor.graphic.polygon.my_point_rect_pol as my_point_rect_pol
# import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
# import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_path as my_dialog_settings_path
# import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
# import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale

import src.View.my_widgets.pdf_editor.paint.polygon.my_point_ellipce_pol as my_point_ellipce_pol


class MyPolygon(QtWidgets.QGraphicsPolygonItem):
    """Класс переопределяющий QtWidgets.QGraphicsPolygonItem
        Класс предназначен для демострации формы фигуры 
        при ее отрисовке
    """
    def __init__(self, pol: QtGui.QPolygonF):
        super().__init__(pol)
        
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
        

        self.setAcceptHoverEvents(True)

