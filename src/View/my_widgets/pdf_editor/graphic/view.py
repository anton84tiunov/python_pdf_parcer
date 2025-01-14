import sys, copy
from PySide6 import QtWidgets, QtGui,  QtCore 

import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.scene as graphics_scene

class MyGraphicsView(QtWidgets.QGraphicsView):
    """класс переопределяющий  графическую вьюху
        В классе реализован механизм масштабирования графической сцены 
        относительно окна представления.
    """

    def __init__(self, root, scene: graphics_scene.MyGraphicsScene, **kwargs):
        super().__init__( **kwargs)
        # self.setupUi(self)
        # self.root: main_window.MainWindow = root
        self.enter_event: bool = False
        
        self.scene: graphics_scene.MyGraphicsScene = scene
        self.setScene(self.scene)
        # self.updateScene()
        self.pen = QtGui.QPen(QtCore.Qt.green)
        self.greenBrush = QtGui.QBrush(QtCore.Qt.green)
        self.grayBrush = QtGui.QBrush(QtCore.Qt.gray)

        # self.mapToScene(0, 0)
        # self.addAction()
        # self.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.red))
        # self.cursor().setShape()
        # self.cursor().setPos(50, 50)
        # self.viewport().pos()
    def zoom_view(self, int_scale: int):
        """функция для масштабирования сцены"""
        
        
        scale_scene = 1
        if int_scale > 0:
            scale_scene *= 1.25
            self.scale(scale_scene, scale_scene)
            # items = self.scene.items()
            # for it in items:
            #     if hasattr(it, "delete_attribute_my_point_rect"):
            #         w = copy.deepcopy(it.rect().width())
            #         h = copy.deepcopy(it.rect().height())
            #         r = copy.deepcopy(it.rect())
            #         r.setWidth(w / scale_scene)
            #         r.setHeight(h / scale_scene)
            #         it.setRect(r)
            #         # it.rect().setWidth(w * scale_scene)
            #         # it.rect().setHeight(h * scale_scene)
            #         # it.setW(scale_scene)
                    
        elif int_scale < 0:
            scale_scene *= 0.8
            self.scale(scale_scene, scale_scene)
            # items = self.scene.items()
            # for it in items:
            #     if hasattr(it, "delete_attribute_my_point_rect"):
            #         w = copy.deepcopy(it.rect().width())
            #         h = copy.deepcopy(it.rect().height())
            #         r = copy.deepcopy(it.rect())
            #         r.setWidth(w / scale_scene)
            #         r.setHeight(h / scale_scene)
            #         it.setRect(r)
    
    def keyPressEvent(self, event):
        if event.key() == 16777249:
            self.enter_event = True
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        super().keyPressEvent(event)
        

    def keyReleaseEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == 16777249:
                self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
                self.enter_event = False
        super().keyReleaseEvent(event)

    def wheelEvent(self, event):
        int_y = event.angleDelta().y()
        scale_scene = 1
        if self.enter_event:
            if int_y > 0:
                scale_scene *= 1.25
                self.scale(scale_scene, scale_scene)
                # items = self.scene.items()
                # for it in items:
                #     if hasattr(it, "delete_attribute_my_point_rect"):
                #         w = copy.deepcopy(it.rect().width())
                #         h = copy.deepcopy(it.rect().height())
                #         r = copy.deepcopy(it.rect())
                #         r.setWidth(w / scale_scene)
                #         r.setHeight(h / scale_scene)
                #         it.setRect(r)
            if int_y < 0:
                scale_scene *= 0.8
                self.scale(scale_scene, scale_scene)
                # items = self.scene.items()
                # for it in items:
                #     if hasattr(it, "delete_attribute_my_point_rect"):
                #         w = copy.deepcopy(it.rect().width())
                #         h = copy.deepcopy(it.rect().height())
                #         r = copy.deepcopy(it.rect())
                #         r.setWidth(w / scale_scene)
                #         r.setHeight(h / scale_scene)
                #         it.setRect(r)


















