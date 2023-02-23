import copy
from PySide6 import QtCore, QtGui, QtWidgets

import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_graph as my_dialog_settings_graph


class MyDialogPropPath(QtWidgets.QDialog, my_dialog_settings_graph.Ui_dialog_settins_el):
    
    def __init__(self, root: QtWidgets, pen: QtGui.QPen, brush: QtGui.QBrush, item_z_index: float, item_opacity: float, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.root: QtWidgets = root
        self.setStyleSheet(self.root.styleSheet())
        self.pen = pen
        self.no_pen: bool = True
        self.pen_color: QtGui.QColor = pen.color()
        self.pen_width: float = pen.widthF()
        self.pen_sryle: QtCore.Qt.PenStyle = pen.style()
        self.pen_cap_style: QtCore.Qt.PenCapStyle = pen.capStyle()
        self.pen_join_style: QtCore.Qt.PenJoinStyle = pen.joinStyle()
        self.dash_pattern: list[float] = pen.dashPattern()
        self.dash_offset: float = pen.dashOffset()

        self.brush = brush
        self.no_brush: bool = False
        self.brush_color: QtGui.QColor = brush.color()
        self.brush_sryle: QtCore.Qt.BrushStyle = brush.style()

        if brush:
            self.no_brush: bool = True
            self.brush_color: QtGui.QColor = brush.color()
            self.brush_sryle: QtCore.Qt.BrushStyle = brush.style()

        self.item_z_index: float = item_z_index
        self.item_opacity: float = item_opacity

        self.background_brush = QtGui.QBrush( QtGui.QColor(232, 235, 232), QtCore.Qt.SolidPattern)
        
        self.btn_pen_color.clicked.connect(self.get_pen_color)




        self.scene_priview = QtWidgets.QGraphicsScene()
        self.scene_priview.setBackgroundBrush(self.background_brush)
        self.gr_view_priview.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gr_view_priview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene_priview.setSceneRect(QtCore.QRectF(0.0, 0.0, 100.0, 100.0))
        self.gr_view_priview.setScene(self.scene_priview)
        
        self.path = QtGui.QPainterPath()
        self.path.moveTo(QtCore.QPointF(10.0, 10.0))
        self.path.lineTo(QtCore.QPointF(90.0, 90.0))
        self.path.cubicTo(QtCore.QPointF(1.0, 99.0), QtCore.QPointF(1.0, 1.0), QtCore.QPointF(90.0, 10.0))
        self.item_path = QtWidgets.QGraphicsPathItem(self.path)
        self.item_path.setPen(pen)
        self.item_path.setBrush(brush)
        self.scene_priview.addItem(self.item_path)
        self.btn_ok.clicked.connect(self.get_value)
        
    def get_value(self):
        ...
        # self.val = self.l_e_dash_pattern.text()
        # self.accept()

    def set_value(self):
        ...
        # self.val = self.l_e_dash_pattern.text()

    def update_priview(self):
        ...

    # def go_end(self):       
    #     self.hide()
    def get_pen_color(self):
        color_dialog = QtWidgets.QColorDialog()
        self.pen_color = color_dialog.getColor()
        self.pen.setColor(self.pen_color)
        # QtWidgets.QStyle = copy.deepcopy(color)
        # print(type(color.getRgb()), color.getRgb())
        # self.btn_pen_color.setStyleSheet(f'background: rgb({color.getRgb()[0], color.getRgb()[1], color.getRgb()[2]});')
        self.item_path.setPen(self.pen)








