import sys
import logging

from PySide6 import QtWidgets, QtGui,  QtCore 
import src.View.my_widgets.general.tab.base as tab_base
import src.View.my_widgets.pdf_el.menu.menu_bar as menu_bar

class TabPdfEl(tab_base.TabBase):
    """класс для создания вкладки "PDF EL" """

    def __init__(self, root: QtWidgets):
        super().__init__("pdf_el")


        logger = logging.getLogger('app.pdf_el_tab')

        # try:
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

        
        # self.graph_scene = scene.MyGraphicsScene(self.root)
        # self.graph_view = view.MyGraphicsView(self.root, self.graph_scene)
        # self.graph_top_tool_bar = top_tool_bar.MyTopToolBar(self.root)
        # # self.graph_view.setScene(self.graph_scene)
        # self.v_box_lay_right_top_right.addWidget(self.graph_top_tool_bar)
        # self.v_box_lay_right_top_right.addWidget(self.graph_view)

        # self.graph_left_tool_bar = left_tool_bar.MyLeftToolBar(self.root)
        # self.h_box_lay_right_top_left.addWidget(self.graph_left_tool_bar)

        self.list_widgets_graph_el = QtWidgets.QListWidget()
        # self.protocol_listbox.insertItems(0, ["1", "2", "3", "4"])
        self.h_box_lay_right_top_left.addWidget(self.list_widgets_graph_el)

        # self.protocol_listbox.currentItemChanged.connect(self.protocol_changed)





        self.h_box_lay_right_top.addWidget(self.frame_right_top_left)
        self.h_box_lay_right_top.addWidget(self.frame_right_top_right)

        self.h_box_lay_left = QtWidgets.QHBoxLayout(self.frame_left_panel)
        self.h_box_lay_left.setContentsMargins(0, 0, 0, 0)

        self.frame_menu = menu_bar.MyMenuBar()

        self.h_box_lay_left.addWidget(self.frame_menu)

        # except Exception as e:
        #     logger.exception(e)
        #     self.txt_brow_log.append(f'<span style=" font-family:"MS Shell Dlg 2"; font-size:5pt;color:#ff0000;"Error: </span><span style=" font-size:18pt; text-decoration: underline; color:#ffaa00;">{e}</span>')
    