import copy
from PySide6 import QtWidgets, QtGui,  QtCore 

import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.ellipse.my_ellopse as my_ellopse
import src.View.my_widgets.pdf_editor.graphic.my_contex_menu as my_contex_menu


class MyRectPage(QtWidgets.QGraphicsRectItem):

    
    def __init__(self, root, rect):
        super().__init__( rect)

        self.root: QtWidgets = root
        self.attribute_rect_page: bool = True

    def contextMenuEvent(self, event: QtWidgets.QGraphicsSceneContextMenuEvent) -> None:
        
        menu = my_contex_menu.MyContextMenu(self.root)

        action_paste = menu.addAction("paste")
      
        selected_action = menu.exec_(event.screenPos())

        
        if selected_action == action_paste:
            self.root.tab_pdf_editor.graph_scene.paste_el(event)
            
        return super().contextMenuEvent(event)