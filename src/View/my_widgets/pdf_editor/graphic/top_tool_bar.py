import sys, os
from PySide6 import QtWidgets, QtGui,  QtCore 
# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.pointer_path.my_pointer_path as my_pointer_path
import src.View.my_widgets.pdf_editor.graphic.polygon.my_polygon as my_polygon
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.image.my_image as my_image
import src.View.my_widgets.pdf_editor.graphic.text.my_text_item as my_text_item

import src.View.my_widgets.general.button.radio_buttom as radio_buttom
import src.View.my_widgets.general.button.combo_box_num as combo_box_num
import src.View.my_widgets.general.button.spin_box as spin_box

import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

red_style = "background-color: rgb(255, 0, 0);"
green_style = "background-color: rgb(0, 255, 0);"
blue_style = "background-color: rgb(0, 0, 255);"

class MyTopToolBar(QtWidgets.QFrame):
    """класс для выбора способа взаимодействия с элементами 
        графической сцены и ей самой."""
        
    def __init__(self, root: QtWidgets, **kwargs):
        super().__init__( **kwargs)
        self.root: QtWidgets = root
        self.tool_cursor: str = ""

        self.v_box = QtWidgets.QHBoxLayout(self)

        self.v_box.setContentsMargins(0, 0, 0, 0)

        self.c_box_grid_cords= spin_box.MySpineBox(self, 'grid_cords.png')
        self.v_box.addWidget(self.c_box_grid_cords)
        self.c_box_grid_cords.valueChanged.connect(self.text_changed) # works, but reacts on every new character typed in textbox of spinbox

    def text_changed(self, s):
        self.root.tab_pdf_editor.graph_scene.grid_step = int(s)
        print(int(s))
