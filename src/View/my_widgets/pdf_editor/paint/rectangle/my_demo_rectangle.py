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

import src.View.my_widgets.pdf_editor.paint.rectangle.my_point_ellipse_rect

class MyDemoRactangle(QtWidgets.QGraphicsRectItem):
    """Класс переопределяющий QtWidgets.QGraphicsRectItem
        Класс предназначен для демострации формы фигуры 
        при ее отрисовке
    """
    def __init__(self, rect: QtCore.QRectF):
        super().__init__( rect)
        self.list_point_rect: list[str] = ["top", "bottom", "left", "right"]
        
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)
      
        self.setBrush(QtGui.QColor.fromRgbF(0.6, 0.1, 0.1, 0.2))
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor.fromRgbF(0.9, 0.9, 0.9, 0.8 ))
        pen.setWidthF(0.5)
        pen.setDashOffset(0.7)
        pen.setDashPattern ([3, 3])
        pen.setJoinStyle(QtCore.Qt.PenJoinStyle.BevelJoin)
        pen.setCapStyle(QtCore.Qt.PenCapStyle.FlatCap)
        self.setPen(pen)
        self.setAcceptHoverEvents(True)


  