import sys
from PySide2 import QtWidgets, QtGui,  QtCore 
import src.View.my_window.main_window as main_window
import src.View.my_widgets.general.tab.base as tab_base
import src.View.my_widgets.pdf_editor.graphic.scene as scene
import src.View.my_widgets.pdf_editor.graphic.view as view
import src.View.my_widgets.pdf_editor.graphic.tool_bar as tool_bar
import src.View.my_widgets.pdf_editor.menu.menu_bar as menu_bar

red_style = "background-color: rgb(255, 0, 0);"
green_style = "background-color: rgb(0, 255, 0);"
blue_style = "background-color: rgb(0, 0, 255);"

class TabPdfEditor(tab_base.TabBase):
    """класс для создания вкладки "PDF EDITOR" """

    def __init__(self, root: main_window.MainWindow):
        super().__init__("pdf_editor")
        self.root: main_window.MainWindow = root

        self.h_box_lay_right_bottom = QtWidgets.QHBoxLayout(self.frame_right_bottom_panel)
        self.h_box_lay_right_bottom.setContentsMargins(0, 0, 0, 0)
        self.txt_brow_log = QtWidgets.QTextBrowser(self.frame_right_bottom_panel)
        self.txt_brow_log.setContentsMargins(0, 0, 0, 0)
        self.txt_brow_log.setHtml("hello world")
        self.h_box_lay_right_bottom.addWidget(self.txt_brow_log)


        self.h_box_lay_right_top = QtWidgets.QHBoxLayout(self.frame_right_top_panel)
        self.h_box_lay_right_top.setContentsMargins(0, 0, 0, 0)

        self.frame_right_top_left = QtWidgets.QFrame()
        self.frame_right_top_left.setContentsMargins(0, 0, 0, 0)
        self.frame_right_top_right = QtWidgets.QFrame()
        self.frame_right_top_right.setContentsMargins(0, 0, 0, 0)

# tool_bar.MyToolBar()
        self.h_box_lay_right_top_left = QtWidgets.QHBoxLayout(self.frame_right_top_left)
        self.h_box_lay_right_top_left.setContentsMargins(0, 0, 0, 0)
        self.h_box_lay_right_top_right = QtWidgets.QHBoxLayout(self.frame_right_top_right)
        self.h_box_lay_right_top_right.setContentsMargins(0, 0, 0, 0)

        
        self.graph_scene = scene.MyGraphicsScene()
        self.graph_view = view.MyGraphicsView(self.rect, self.graph_scene)
        # self.graph_view.setScene(self.graph_scene)
        self.h_box_lay_right_top_right.addWidget(self.graph_view)

        self.graph_tool_bar = tool_bar.MyToolBar(self.root)
        self.h_box_lay_right_top_left.addWidget(self.graph_tool_bar)

        self.h_box_lay_right_top.addWidget(self.frame_right_top_left)
        self.h_box_lay_right_top.addWidget(self.frame_right_top_right)

        self.h_box_lay_left = QtWidgets.QHBoxLayout(self.frame_left_panel)
        self.h_box_lay_left.setContentsMargins(0, 0, 0, 0)

        self.frame_menu = menu_bar.MyMenuBar()

        self.h_box_lay_left.addWidget(self.frame_menu)

       
    
        
 
           
        
