import copy

from PySide6 import QtCore, QtGui, QtWidgets

import src.Utility.general.comfig.config as config
import src.Utility.pdf_editor.default_pen_brush as default_pen_brush
import src.Utility.pdf_editor.get_set_default_style as get_set_default_style
import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_graph as my_dialog_settings_graph

                 
class MyDialogPropPath(QtWidgets.QDialog, my_dialog_settings_graph.Ui_dialog_settins_el):
    
    def __init__(self, root: QtWidgets, pen: QtGui.QPen, brush: QtGui.QBrush, item_z_index: float, item_opacity: float, fill_rule: QtCore.Qt.FillRule, **kwargs):
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
        # self.no_brush: bool = False
        # self.brush_color: QtGui.QColor = brush.color()
        # self.brush_sryle: QtCore.Qt.BrushStyle = brush.style()

        # if brush:
        self.no_brush: bool = True
        self.brush_color: QtGui.QColor = brush.color()
        self.brush_style: QtCore.Qt.BrushStyle = brush.style()

        self.item_z_index: float = item_z_index
        self.item_opacity: float = item_opacity
        self.fill_rule: QtCore.Qt.FillRule = fill_rule

        self.path = QtGui.QPainterPath()
        self.path.moveTo(QtCore.QPointF(5.0, 5.0))
        self.path.lineTo(QtCore.QPointF(145.0, 145.0))
        self.path.cubicTo(QtCore.QPointF(1.0, 149.0), QtCore.QPointF(1.0, 1.0), QtCore.QPointF(149.0, 10.0))
        self.item_path = QtWidgets.QGraphicsPathItem(self.path)

        self.background_brush = QtGui.QBrush( QtGui.QColor(232, 235, 232), QtCore.Qt.SolidPattern)
        self.btn_brush_color.setStyleSheet(f"background-color:{self.brush_color.name()}")
        self.btn_pen_color.setStyleSheet(f"background-color: {self.pen_color.name()}")
        self.dbl_sp_box_width.setValue(self.pen_width)
        self.dbl_sp_box_dash_offset.setValue(self.dash_offset)
        self.dbl_sp_box_opacity.setValue(self.item_opacity)
        self.dbl_sp_box_z_index.setValue(self.item_z_index)
     


        self.btn_pen_color.clicked.connect(self.get_pen_color)
        self.btn_brush_color.clicked.connect(self.get_brush_color)
        self.com_box_pen_style.currentTextChanged.connect(self.get_pen_style)
        self.com_box_pen_style.setCurrentText(str(pen.style()).replace("PenStyle.", ""))
        self.com_box_pen_cap_style.currentTextChanged.connect(self.get_pen_cap_style)
        self.com_box_pen_cap_style.setCurrentText(str(pen.capStyle()).replace("PenCapStyle.", ""))
        self.com_box_pen_join_style.currentTextChanged.connect(self.get_pen_join_style)
        self.com_box_pen_join_style.setCurrentText(str(pen.joinStyle()).replace("PenJoinStyle.", ""))
        self.com_box_brush_style.currentTextChanged.connect(self.get_brush_style)
        self.com_box_brush_style.setCurrentText(str(brush.style()).replace('BrushStyle.', ''))
        self.l_e_dash_pattern.textChanged.connect(self.get_dash_pattern)
        # self.l_e_dash_pattern.editingFinished.connect(self.get_dash_pattern)
        self.com_box_lbl_fill_rule.currentTextChanged.connect(self.get_fill_rule)
        self.com_box_lbl_fill_rule.setCurrentText(str(self.fill_rule).replace('FillRule.', ''))


        self.dbl_sp_box_width.valueChanged.connect(self.get_pen_width)
        self.dbl_sp_box_dash_offset.valueChanged.connect(self.get_dash_offset)
        # self.dbl_sp_box_.valueChanged.connect(self.get_dash_offset)
        self.dbl_sp_box_opacity.valueChanged.connect(self.get_opacity)
        self.dbl_sp_box_z_index.valueChanged.connect(self.get_z_index)
        
        
        # self.l_e_dash_pattern.setValidator(QtGui.QValidator().)
        self.scene_priview = QtWidgets.QGraphicsScene()
        self.scene_priview.setBackgroundBrush(self.background_brush)
        self.gr_view_priview.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gr_view_priview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene_priview.setSceneRect(QtCore.QRectF(0.0, 0.0, 150.0, 150.0))
        self.gr_view_priview.setScene(self.scene_priview)
        
        # self.path = QtGui.QPainterPath()
        # self.path.moveTo(QtCore.QPointF(5.0, 5.0))
        # self.path.lineTo(QtCore.QPointF(145.0, 145.0))
        # self.path.cubicTo(QtCore.QPointF(1.0, 149.0), QtCore.QPointF(1.0, 1.0), QtCore.QPointF(149.0, 10.0))
        # self.item_path = QtWidgets.QGraphicsPathItem(self.path)
        self.item_path.setPen(pen)
        self.item_path.setBrush(brush)
        self.scene_priview.addItem(self.item_path)
        
        self.btn_ok.clicked.connect(self.get_value)
        self.btn_cancel.clicked.connect(self.get_exit)
        self.btn_default.clicked.connect(self.set_default)
        self.btn_save_to_file.clicked.connect(self.save_to_file)
    
    def set_default(self):
        conf_path = "configs/default_style_el_config.INI"
        
        config.update_setting(conf_path, "path", "pen_color",str( self.pen_color.getRgb()))
        config.update_setting(conf_path, "path", "pen_width",str( self.pen_width))
        config.update_setting(conf_path, "path", "pen_style",str( self.pen_sryle).replace("PenStyle.", ""))
        config.update_setting(conf_path, "path", "pen_cap_style",str( self.pen_cap_style).replace("PenCapStyle.", ""))
        config.update_setting(conf_path, "path", "pen_join_style",str( self.pen_join_style).replace("PenJoinStyle.", ""))
        config.update_setting(conf_path, "path", "pen_dash_offset",str( self.dash_offset))
        config.update_setting(conf_path, "path", "pen_dash_pattern",str( self.dash_pattern))
        config.update_setting(conf_path, "path", "brush_style",str( self.brush_style).replace("BrushStyle.", ""))
        config.update_setting(conf_path, "path", "brush_color",str( self.brush_color.getRgb()))
        # print(conf.sections())
       

    def get_value(self):

        self.accept()

    def get_exit(self):
        self.reject()

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
        self.btn_pen_color.setStyleSheet(f"background-color: {self.pen_color.name()}")
        self.item_path.setPen(self.pen)

    def get_brush_color(self):
        color_dialog = QtWidgets.QColorDialog()
        self.brush_color = color_dialog.getColor()
        self.brush.setColor(self.brush_color)
        # QtWidgets.QStyle = copy.deepcopy(color)
        # print(type(color.getRgb()), color.getRgb())
        self.btn_brush_color.setStyleSheet(f"background-color:{self.brush_color.name()}")
        self.item_path.setBrush(self.brush)

    def get_pen_style(self, str_style):
        pen_style = QtCore.Qt.PenStyle()
        if str_style == "NoPen":
            self.pen.setStyle(pen_style.NoPen)
            self.pen_sryle = pen_style.NoPen
        elif str_style == "SolidLine":
            self.pen.setStyle(pen_style.SolidLine)
            self.pen_sryle = pen_style.SolidLine
        elif str_style == "DashLine":
            self.pen.setStyle(pen_style.DashLine)
            self.pen_sryle = pen_style.DashLine
        elif str_style == "DotLine":
            self.pen.setStyle(pen_style.DotLine)
            self.pen_sryle = pen_style.DotLine
        elif str_style == "DashDotLine":
            self.pen.setStyle(pen_style.DashDotLine)
            self.pen_sryle = pen_style.DashDotLine
        elif str_style == "DashDotDotLine":
            self.pen.setStyle(pen_style.DashDotDotLine)
            self.pen_sryle = pen_style.DashDotDotLine
        elif str_style == "CustomDashLine":
           self.pen.setStyle(pen_style.CustomDashLine)
           self.pen_sryle = pen_style.CustomDashLine
        elif str_style == "MPenStyle":
            self.pen.setStyle(pen_style.MPenStyle)
            self.pen_sryle = pen_style.MPenStyle
        self.item_path.setPen(self.pen)

    def get_pen_cap_style(self, str_style):
        pen_cap_style = QtCore.Qt.PenCapStyle()
        if  str_style == "FlatCap":
            self.pen.setCapStyle(pen_cap_style.FlatCap)
            self.pen_cap_style = pen_cap_style.FlatCap
        elif  str_style == "SquareCap":
           self.pen.setCapStyle(pen_cap_style.SquareCap)
           self.pen_cap_style = pen_cap_style.SquareCap
        elif  str_style == "RoundCap":
            self.pen.setCapStyle(pen_cap_style.RoundCap)
            self.pen_cap_style = pen_cap_style.RoundCap
        elif  str_style == "MPenCapStyle":
            self.pen.setCapStyle(pen_cap_style.MPenCapStyle)
            self.pen_cap_style = pen_cap_style.MPenCapStyle
        self.item_path.setPen(self.pen)

    def get_pen_join_style(self, str_style):
        pen_join_style = QtCore.Qt.PenJoinStyle()
        if  str_style == "MiterJoin":
            self.pen.setJoinStyle(pen_join_style.MiterJoin)
            self.pen_join_style = pen_join_style.MiterJoin
        elif  str_style == "BevelJoin":
            self.pen.setJoinStyle(pen_join_style.BevelJoin)
            self.pen_join_style = pen_join_style.BevelJoin
        elif  str_style == "RoundJoin":
            self.pen.setJoinStyle(pen_join_style.RoundJoin)
            self.pen_join_style = pen_join_style.RoundJoin
        elif  str_style == "SvgMiterJoin":
            self.pen.setJoinStyle(pen_join_style.SvgMiterJoin)
            self.pen_join_style = pen_join_style.SvgMiterJoin
        elif  str_style == "MPenJoinStyle":
            self.pen.setJoinStyle(pen_join_style.MPenJoinStyle)
            self.pen_join_style = pen_join_style.MPenJoinStyle
        self.item_path.setPen(self.pen)              

    def get_brush_style(self, str_style):
        brush_style = QtCore.Qt.BrushStyle()

        if str_style == "NoBrush":
            self.brush.setStyle(brush_style.NoBrush)
            self.brush_style = brush_style.NoBrush
        elif str_style == "SolidPattern":
            self.brush.setStyle(brush_style.SolidPattern)
            self.brush_style = brush_style.SolidPattern
        elif str_style == "Dense1Pattern":
            self.brush.setStyle(brush_style.Dense1Pattern)
            self.brush_style = brush_style.Dense1Pattern
        elif str_style == "Dense2Pattern":
            self.brush.setStyle(brush_style.Dense2Pattern)
            self.brush_style = brush_style.Dense2Pattern
        elif str_style == "Dense3Pattern":
            self.brush.setStyle(brush_style.Dense3Pattern)
            self.brush_style = brush_style.Dense3Pattern
        elif str_style == "Dense4Pattern":
            self.brush.setStyle(brush_style.Dense4Pattern)
            self.brush_style = brush_style.Dense4Pattern
        elif str_style == "Dense5Pattern":
            self.brush.setStyle(brush_style.Dense5Pattern)
            self.brush_style = brush_style.Dense5Pattern
        elif str_style == "Dense6Pattern":
           self.brush.setStyle(brush_style.Dense6Pattern)
           self.brush_style = brush_style.Dense6Pattern
        elif str_style == "Dense7Pattern":
            self.brush.setStyle(brush_style.Dense7Pattern)
            self.brush_style = brush_style.Dense7Pattern
        elif str_style == "HorPattern":
            self.brush.setStyle(brush_style.HorPattern)
            self.brush_style = brush_style.HorPattern
        elif str_style == "VerPattern":
            self.brush.setStyle(brush_style.VerPattern)
            self.brush_style = brush_style.VerPattern
        elif str_style == "CrossPattern":
            self.brush.setStyle(brush_style.CrossPattern)
            self.brush_style = brush_style.CrossPattern
        elif str_style == "BDiagPattern":
            self.brush.setStyle(brush_style.BDiagPattern)
            self.brush_style = brush_style.NoBrush
        elif str_style == "FDiagPattern":
            self.brush.setStyle(brush_style.FDiagPattern)
            self.brush_style = brush_style.FDiagPattern
        elif str_style == "DiagCrossPattern":
            self.brush.setStyle(brush_style.DiagCrossPattern)
            self.brush_style = brush_style.DiagCrossPattern
        elif str_style == "LinearGradientPattern":
            self.brush.setStyle(brush_style.LinearGradientPattern)
            self.brush_style = brush_style.LinearGradientPattern
        elif str_style == "RadialGradientPattern":
            self.brush.setStyle(brush_style.RadialGradientPattern)
            self.brush_style = brush_style.RadialGradientPattern
        elif str_style == "ConicalGradientPattern":
            self.brush.setStyle(brush_style.ConicalGradientPattern)
            self.brush_style = brush_style.ConicalGradientPattern
        elif str_style == "TexturePattern":
            self.brush.setStyle(brush_style.TexturePattern)
            self.brush_style = brush_style.TexturePattern
        self.item_path.setBrush(self.brush)

    def get_dash_pattern(self, text: str):

        try:
            float_list = list(map(float, text.split()))
            if len(float_list) % 2 == 0 or len(float_list) == 0:
                self.dash_pattern = float_list
        except Exception as e:
            print(e)
        self.pen.setDashPattern(self.dash_pattern)
        self.item_path.setPen(self.pen)

    def get_dash_offset(self, val):
        self.dash_offset = val
        self.pen.setDashOffset(self.dash_offset)
        self.item_path.setPen(self.pen)      

    def get_pen_width(self, val):
        self.pen_width = val
        self.pen.setWidth(self.pen_width)
        self.item_path.setPen(self.pen)     

    def get_opacity(self, val):
        self.item_opacity = val    

    def get_z_index(self, val):
        self.item_z_index = val
       
    def eventFilter(self, arg__1: QtCore.QObject, arg__2:QtCore.QEvent) -> bool:
        if arg__2.type() == QtCore.QEvent.KeyPress:
            print(arg__2.__dir__())
        return super().eventFilter(arg__1, arg__2)

    def get_fill_rule(self, fill_rule: str):
        f_rule = QtCore.Qt.FillRule

        if fill_rule == "OddEvenFill":
            self.fill_rule =  f_rule.OddEvenFill
        elif fill_rule == "WindingFill":
            self.fill_rule =  f_rule.WindingFill  
              
    def save_to_file(self):
        print("save_to_file")
            # if data['items'][num_it]['fill_r'] == "OddEvenFill":
#                             pol_item.setFillRule(QtCore.Qt.FillRule.OddEvenFill)
#                         if data['items'][num_it]['fill_r'] == "WindingFill":
#                             pol_item.setFillRule(QtCore.Qt.FillRule.WindingFill)
       
        
                 