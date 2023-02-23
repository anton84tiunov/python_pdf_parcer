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
            if isinstance(self.root.tab_pdf_editor.graph_scene.buffer_copy_item, my_rectangle.MyRactangle):
                rect_f = self.root.tab_pdf_editor.graph_scene.buffer_copy_item.rect()
                w = copy.deepcopy(rect_f.width())
                h = copy.deepcopy(rect_f.height())

                rect_f.setX(copy.deepcopy(event.scenePos().x()))
                rect_f.setY(copy.deepcopy(event.scenePos().y()))
                rect_f.setWidth(w)
                rect_f.setHeight(h)

                rect_item = my_rectangle.MyRactangle(self.root, rect_f)
                rect_item.setPen(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.pen())
                rect_item.setBrush(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.brush())
                rect_item.setZValue(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.zValue())
                self.root.tab_pdf_editor.graph_scene.addItem(rect_item)
            
            elif isinstance(self.root.tab_pdf_editor.graph_scene.buffer_copy_item, my_ellopse.MyEllipse):
                rect_f = self.root.tab_pdf_editor.graph_scene.buffer_copy_item.rect()
                w = copy.deepcopy(rect_f.width())
                h = copy.deepcopy(rect_f.height())

                rect_f.setX(copy.deepcopy(event.scenePos().x()))
                rect_f.setY(copy.deepcopy(event.scenePos().y()))
                rect_f.setWidth(w)
                rect_f.setHeight(h)

                ellipse_item = my_ellopse.MyEllipse(self.root, rect_f)
                ellipse_item.setPen(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.pen())
                ellipse_item.setBrush(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.brush())
                ellipse_item.setZValue(self.root.tab_pdf_editor.graph_scene.buffer_copy_item.zValue())
                self.root.tab_pdf_editor.graph_scene.addItem(ellipse_item)
        
            return super().contextMenuEvent(event)