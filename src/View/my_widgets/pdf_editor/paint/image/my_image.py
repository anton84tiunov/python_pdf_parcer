import math
from PySide6 import QtWidgets, QtGui,  QtCore 
import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.paint.image.my_point_ellipse_image as my_point_ellipse_image
# import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu
# import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_path as my_dialog_settings_path
# import src.View.my_widgets.pdf_editor.dialog.my_rotate as my_rotate
# import src.View.my_widgets.pdf_editor.dialog.my_scale as my_scale




class MyDemoImage(QtWidgets.QGraphicsPixmapItem):
    """Класс переопределяющий QtWidgets.QGraphicsPixmapItem
        Класс предназначен для демострации формы фигуры 
        при ее отрисовке
    """
    def __init__(self,  pix: QtGui.QPixmap):
        super().__init__( pix)
        self.list_point_rect = ["top", "bottom", "left", "right"]
        
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges, True)
        # self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable, True)

        self.setAcceptHoverEvents(True)

