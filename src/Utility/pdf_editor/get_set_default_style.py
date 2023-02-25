from PySide6 import QtCore, QtGui, QtWidgets

import src.Utility.general.comfig.config as config


conf_path = "configs/default_style_el_config.INI"
        

def get_pen_brush(el: str):
    pen = QtGui.QPen()
    brush = QtGui.QBrush()
    str_pen_color =         config.get_setting(conf_path, el, "pen_color")
    str_pen_width =         config.get_setting(conf_path, el, "pen_width")
    str_pen_style =         config.get_setting(conf_path, el, "pen_style")
    str_pen_cap_style =     config.get_setting(conf_path, el, "pen_cap_style")
    str_pen_join_style =    config.get_setting(conf_path, el, "pen_join_style")
    str_pen_dash_offset =   config.get_setting(conf_path, el, "pen_dash_offset")
    str_pen_dash_pattern =  config.get_setting(conf_path, el, "pen_dash_pattern")
    str_brush_style =       config.get_setting(conf_path, el, "brush_style")
    str_brush_color =       config.get_setting(conf_path, el, "brush_color")

    pen.setColor(QtGui.QColor(*tuple(map(float, str_pen_color[1:-1].split(", ")))))
    pen.setWidthF(float(str_pen_width))
    pen.setDashOffset(float(str_pen_dash_offset))
    if str_pen_dash_pattern == "[]":
        pen.setDashPattern([])
    else:
        pen.setDashPattern(list(map(float, str_pen_dash_pattern[1:-1].split(", "))))

    pen_style = QtCore.Qt.PenStyle()


    if str_pen_style == "NoPen":
        pen.setStyle(pen_style.NoPen)
    elif str_pen_style == "SolidLine":
        pen.setStyle(pen_style.SolidLine)
    elif str_pen_style == "DashLine":
        pen.setStyle(pen_style.DashLine)
    elif str_pen_style == "DotLine":
        pen.setStyle(pen_style.DotLine)
    elif str_pen_style == "DashDotLine":
        pen.setStyle(pen_style.DashDotLine)
    elif str_pen_style == "DashDotDotLine":
        pen.setStyle(pen_style.DashDotDotLine)
    elif str_pen_style == "CustomDashLine":
        pen.setStyle(pen_style.CustomDashLine)
    elif str_pen_style == "MPenStyle":
        pen.setStyle(pen_style.MPenStyle)


    pen_cap_style = QtCore.Qt.PenCapStyle()
    if  str_pen_cap_style == "FlatCap":
        pen.setCapStyle(pen_cap_style.FlatCap)
    elif  str_pen_cap_style == "SquareCap":
        pen.setCapStyle(pen_cap_style.SquareCap)
    elif  str_pen_cap_style == "RoundCap":
        pen.setCapStyle(pen_cap_style.RoundCap)
    elif  str_pen_cap_style == "MPenCapStyle":
        pen.setCapStyle(pen_cap_style.MPenCapStyle)


    pen_join_style = QtCore.Qt.PenJoinStyle()
    if  str_pen_join_style == "MiterJoin":
        pen.setJoinStyle(pen_join_style.MiterJoin)
    elif  str_pen_join_style == "BevelJoin":
        pen.setJoinStyle(pen_join_style.BevelJoin)
    elif  str_pen_join_style == "RoundJoin":
        pen.setJoinStyle(pen_join_style.RoundJoin)
    elif  str_pen_join_style == "SvgMiterJoin":
        pen.setJoinStyle(pen_join_style.SvgMiterJoin)
    elif  str_pen_join_style == "MPenJoinStyle":
        pen.setJoinStyle(pen_join_style.MPenJoinStyle)
             
    brush.setColor(QtGui.QColor(*tuple(map(float, str_brush_color[1:-1].split(", ")))))

    brush_style = QtCore.Qt.BrushStyle()

    if str_brush_style == "NoBrush":
        brush.setStyle(brush_style.NoBrush)
    elif str_brush_style == "SolidPattern":
        brush.setStyle(brush_style.SolidPattern)
    elif str_brush_style == "Dense1Pattern":
        brush.setStyle(brush_style.Dense1Pattern)
    elif str_brush_style == "Dense2Pattern":
        brush.setStyle(brush_style.Dense2Pattern)
    elif str_brush_style == "Dense3Pattern":
        brush.setStyle(brush_style.Dense3Pattern)
    elif str_brush_style == "Dense4Pattern":
        brush.setStyle(brush_style.Dense4Pattern)
    elif str_brush_style == "Dense5Pattern":
        brush.setStyle(brush_style.Dense5Pattern)
    elif str_brush_style == "Dense6Pattern":
        brush.setStyle(brush_style.Dense6Pattern)
    elif str_brush_style == "Dense7Pattern":
        brush.setStyle(brush_style.Dense7Pattern)
    elif str_brush_style == "HorPattern":
        brush.setStyle(brush_style.HorPattern)
    elif str_brush_style == "VerPattern":
        brush.setStyle(brush_style.VerPattern)
    elif str_brush_style == "CrossPattern":
        brush.setStyle(brush_style.CrossPattern)
    elif str_brush_style == "BDiagPattern":
        brush.setStyle(brush_style.BDiagPattern)
    elif str_brush_style == "FDiagPattern":
        brush.setStyle(brush_style.FDiagPattern)
    elif str_brush_style == "DiagCrossPattern":
        brush.setStyle(brush_style.DiagCrossPattern)
    elif str_brush_style == "LinearGradientPattern":
        brush.setStyle(brush_style.LinearGradientPattern)
    elif str_brush_style == "RadialGradientPattern":
        brush.setStyle(brush_style.RadialGradientPattern)
    elif str_brush_style == "ConicalGradientPattern":
        brush.setStyle(brush_style.ConicalGradientPattern)
    elif str_brush_style == "TexturePattern":
        brush.setStyle(brush_style.TexturePattern)

    return pen, brush

