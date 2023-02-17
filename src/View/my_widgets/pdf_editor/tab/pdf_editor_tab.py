import sys
import logging


from PySide6 import QtWidgets, QtGui,  QtCore 
# import src.View.my_window.main_window as main_window
import src.View.my_widgets.general.tab.base as tab_base
import src.View.my_widgets.pdf_editor.graphic.scene as scene
import src.View.my_widgets.pdf_editor.graphic.view as view
import src.View.my_widgets.pdf_editor.graphic.left_tool_bar as left_tool_bar
import src.View.my_widgets.pdf_editor.graphic.top_tool_bar as top_tool_bar
import src.View.my_widgets.pdf_editor.menu.menu_bar as menu_bar

red_style = "background-color: rgb(255, 0, 0);"
green_style = "background-color: rgb(0, 255, 0);"
blue_style = "background-color: rgb(0, 0, 255);"

class TabPdfEditor(tab_base.TabBase):
    """класс для создания вкладки "PDF EDITOR" """

    def __init__(self, root: QtWidgets):
        super().__init__("pdf_editor")

        logger = logging.getLogger(__name__)

        try:
            self.root: QtWidgets = root

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
            self.v_box_lay_right_top_right = QtWidgets.QVBoxLayout(self.frame_right_top_right)
            self.v_box_lay_right_top_right.setContentsMargins(0, 0, 0, 0)

            
            self.graph_scene = scene.MyGraphicsScene(self.root)
            self.graph_view = view.MyGraphicsView(self.root, self.graph_scene)
            self.graph_top_tool_bar = top_tool_bar.MyTopToolBar(self.root)
            # self.graph_view.setScene(self.graph_scene)
            self.v_box_lay_right_top_right.addWidget(self.graph_top_tool_bar)
            self.v_box_lay_right_top_right.addWidget(self.graph_view)

            self.graph_left_tool_bar = left_tool_bar.MyLeftToolBar(self.root)
            self.h_box_lay_right_top_left.addWidget(self.graph_left_tool_bar)

            self.h_box_lay_right_top.addWidget(self.frame_right_top_left)
            self.h_box_lay_right_top.addWidget(self.frame_right_top_right)

            self.h_box_lay_left = QtWidgets.QHBoxLayout(self.frame_left_panel)
            self.h_box_lay_left.setContentsMargins(0, 0, 0, 0)

            self.frame_menu = menu_bar.MyMenuBar()

            self.h_box_lay_left.addWidget(self.frame_menu)

        except Exception as e:
            logger.exception(e)
            logging.basicConfig(filename='pdf_editor.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(str(e))
            self.txt_brow_log.append(f'<span style=" font-family:"MS Shell Dlg 2"; font-size:5pt;color:#ffff00;"Error: </span><span style=" font-size:18pt; text-decoration: underline; color:#3355cc;">{e}</span>')
    
        
 
           
        
