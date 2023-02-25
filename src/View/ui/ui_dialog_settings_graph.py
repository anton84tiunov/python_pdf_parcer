# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_settings_graphkwlMBF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_dialog_settins_el(object):
    def setupUi(self, dialog_settins_el):
        if not dialog_settins_el.objectName():
            dialog_settins_el.setObjectName(u"dialog_settins_el")
        dialog_settins_el.resize(336, 382)
        self.horizontalLayout = QHBoxLayout(dialog_settins_el)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gr_box_pen = QGroupBox(dialog_settins_el)
        self.gr_box_pen.setObjectName(u"gr_box_pen")
        self.formLayout_2 = QFormLayout(self.gr_box_pen)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_pen_color = QLabel(self.gr_box_pen)
        self.lbl_pen_color.setObjectName(u"lbl_pen_color")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_pen_color)

        self.btn_pen_color = QPushButton(self.gr_box_pen)
        self.btn_pen_color.setObjectName(u"btn_pen_color")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.btn_pen_color)

        self.lbl_pen_cap_style = QLabel(self.gr_box_pen)
        self.lbl_pen_cap_style.setObjectName(u"lbl_pen_cap_style")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.lbl_pen_cap_style)

        self.com_box_pen_cap_style = QComboBox(self.gr_box_pen)
        self.com_box_pen_cap_style.addItem("")
        self.com_box_pen_cap_style.addItem("")
        self.com_box_pen_cap_style.addItem("")
        self.com_box_pen_cap_style.addItem("")
        self.com_box_pen_cap_style.setObjectName(u"com_box_pen_cap_style")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.com_box_pen_cap_style)

        self.lbl_pen_join_style = QLabel(self.gr_box_pen)
        self.lbl_pen_join_style.setObjectName(u"lbl_pen_join_style")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.lbl_pen_join_style)

        self.com_box_pen_join_style = QComboBox(self.gr_box_pen)
        self.com_box_pen_join_style.addItem("")
        self.com_box_pen_join_style.addItem("")
        self.com_box_pen_join_style.addItem("")
        self.com_box_pen_join_style.addItem("")
        self.com_box_pen_join_style.addItem("")
        self.com_box_pen_join_style.setObjectName(u"com_box_pen_join_style")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.com_box_pen_join_style)

        self.lbl_pen_dash_pattern = QLabel(self.gr_box_pen)
        self.lbl_pen_dash_pattern.setObjectName(u"lbl_pen_dash_pattern")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.lbl_pen_dash_pattern)

        self.l_e_dash_pattern = QLineEdit(self.gr_box_pen)
        self.l_e_dash_pattern.setObjectName(u"l_e_dash_pattern")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.l_e_dash_pattern)

        self.lbl_pen_dash_offset = QLabel(self.gr_box_pen)
        self.lbl_pen_dash_offset.setObjectName(u"lbl_pen_dash_offset")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.lbl_pen_dash_offset)

        self.dbl_sp_box_dash_offset = QDoubleSpinBox(self.gr_box_pen)
        self.dbl_sp_box_dash_offset.setObjectName(u"dbl_sp_box_dash_offset")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.dbl_sp_box_dash_offset)

        self.dbl_sp_box_width = QDoubleSpinBox(self.gr_box_pen)
        self.dbl_sp_box_width.setObjectName(u"dbl_sp_box_width")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.dbl_sp_box_width)

        self.lbl_pen_width = QLabel(self.gr_box_pen)
        self.lbl_pen_width.setObjectName(u"lbl_pen_width")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_pen_width)

        self.lbl_pen_style = QLabel(self.gr_box_pen)
        self.lbl_pen_style.setObjectName(u"lbl_pen_style")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_pen_style)

        self.com_box_pen_style = QComboBox(self.gr_box_pen)
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.addItem("")
        self.com_box_pen_style.setObjectName(u"com_box_pen_style")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.com_box_pen_style)


        self.verticalLayout.addWidget(self.gr_box_pen)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_default = QPushButton(dialog_settins_el)
        self.btn_default.setObjectName(u"btn_default")

        self.verticalLayout_4.addWidget(self.btn_default)

        self.btn_ok = QPushButton(dialog_settins_el)
        self.btn_ok.setObjectName(u"btn_ok")

        self.verticalLayout_4.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(dialog_settins_el)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.verticalLayout_4.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gr_box_brush = QGroupBox(dialog_settins_el)
        self.gr_box_brush.setObjectName(u"gr_box_brush")
        self.formLayout = QFormLayout(self.gr_box_brush)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_brush_color = QLabel(self.gr_box_brush)
        self.lbl_brush_color.setObjectName(u"lbl_brush_color")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_brush_color)

        self.btn_brush_color = QPushButton(self.gr_box_brush)
        self.btn_brush_color.setObjectName(u"btn_brush_color")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.btn_brush_color)

        self.lbl_brush_style = QLabel(self.gr_box_brush)
        self.lbl_brush_style.setObjectName(u"lbl_brush_style")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_brush_style)

        self.com_box_brush_style = QComboBox(self.gr_box_brush)
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.addItem("")
        self.com_box_brush_style.setObjectName(u"com_box_brush_style")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.com_box_brush_style)


        self.verticalLayout_3.addWidget(self.gr_box_brush)

        self.gr_box_item = QGroupBox(dialog_settins_el)
        self.gr_box_item.setObjectName(u"gr_box_item")
        self.formLayout_3 = QFormLayout(self.gr_box_item)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_z_index = QLabel(self.gr_box_item)
        self.lbl_z_index.setObjectName(u"lbl_z_index")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_z_index)

        self.dbl_sp_box_z_index = QDoubleSpinBox(self.gr_box_item)
        self.dbl_sp_box_z_index.setObjectName(u"dbl_sp_box_z_index")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.dbl_sp_box_z_index)

        self.lbl_box_opacity = QLabel(self.gr_box_item)
        self.lbl_box_opacity.setObjectName(u"lbl_box_opacity")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lbl_box_opacity)

        self.dbl_sp_box_opacity = QDoubleSpinBox(self.gr_box_item)
        self.dbl_sp_box_opacity.setObjectName(u"dbl_sp_box_opacity")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.dbl_sp_box_opacity)


        self.verticalLayout_3.addWidget(self.gr_box_item)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gr_view_priview = QGraphicsView(dialog_settins_el)
        self.gr_view_priview.setObjectName(u"gr_view_priview")
        self.gr_view_priview.setMinimumSize(QSize(150, 150))
        self.gr_view_priview.setMaximumSize(QSize(150, 150))
        self.gr_view_priview.setSizeIncrement(QSize(150, 150))
        self.gr_view_priview.setBaseSize(QSize(150, 150))

        self.gridLayout.addWidget(self.gr_view_priview, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(dialog_settins_el)

        QMetaObject.connectSlotsByName(dialog_settins_el)
    # setupUi

    def retranslateUi(self, dialog_settins_el):
        dialog_settins_el.setWindowTitle(QCoreApplication.translate("dialog_settins_el", u"settings", None))
        self.gr_box_pen.setTitle(QCoreApplication.translate("dialog_settins_el", u"pen", None))
        self.lbl_pen_color.setText(QCoreApplication.translate("dialog_settins_el", u"color", None))
        self.btn_pen_color.setText("")
        self.lbl_pen_cap_style.setText(QCoreApplication.translate("dialog_settins_el", u"cap", None))
        self.com_box_pen_cap_style.setItemText(0, QCoreApplication.translate("dialog_settins_el", u"FlatCap", None))
        self.com_box_pen_cap_style.setItemText(1, QCoreApplication.translate("dialog_settins_el", u"SquareCap", None))
        self.com_box_pen_cap_style.setItemText(2, QCoreApplication.translate("dialog_settins_el", u"RoundCap", None))
        self.com_box_pen_cap_style.setItemText(3, QCoreApplication.translate("dialog_settins_el", u"MPenCapStyle", None))

        self.lbl_pen_join_style.setText(QCoreApplication.translate("dialog_settins_el", u"join", None))
        self.com_box_pen_join_style.setItemText(0, QCoreApplication.translate("dialog_settins_el", u"MiterJoin", None))
        self.com_box_pen_join_style.setItemText(1, QCoreApplication.translate("dialog_settins_el", u"BevelJoin", None))
        self.com_box_pen_join_style.setItemText(2, QCoreApplication.translate("dialog_settins_el", u"RoundJoin", None))
        self.com_box_pen_join_style.setItemText(3, QCoreApplication.translate("dialog_settins_el", u"SvgMiterJoin", None))
        self.com_box_pen_join_style.setItemText(4, QCoreApplication.translate("dialog_settins_el", u"MPenJoinStyle", None))

        self.lbl_pen_dash_pattern.setText(QCoreApplication.translate("dialog_settins_el", u"pattern", None))
        self.lbl_pen_dash_offset.setText(QCoreApplication.translate("dialog_settins_el", u"offset", None))
        self.lbl_pen_width.setText(QCoreApplication.translate("dialog_settins_el", u"width", None))
        self.lbl_pen_style.setText(QCoreApplication.translate("dialog_settins_el", u"style", None))
        self.com_box_pen_style.setItemText(0, QCoreApplication.translate("dialog_settins_el", u"NoPen", None))
        self.com_box_pen_style.setItemText(1, QCoreApplication.translate("dialog_settins_el", u"SolidLine", None))
        self.com_box_pen_style.setItemText(2, QCoreApplication.translate("dialog_settins_el", u"DashLine", None))
        self.com_box_pen_style.setItemText(3, QCoreApplication.translate("dialog_settins_el", u"DotLine", None))
        self.com_box_pen_style.setItemText(4, QCoreApplication.translate("dialog_settins_el", u"DashDotLine", None))
        self.com_box_pen_style.setItemText(5, QCoreApplication.translate("dialog_settins_el", u"DashDotDotLine", None))
        self.com_box_pen_style.setItemText(6, QCoreApplication.translate("dialog_settins_el", u"CustomDashLine", None))
        self.com_box_pen_style.setItemText(7, QCoreApplication.translate("dialog_settins_el", u"MPenStyle", None))

        self.btn_default.setText(QCoreApplication.translate("dialog_settins_el", u"default", None))
        self.btn_ok.setText(QCoreApplication.translate("dialog_settins_el", u"ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("dialog_settins_el", u"cancel", None))
        self.gr_box_brush.setTitle(QCoreApplication.translate("dialog_settins_el", u"brush", None))
        self.lbl_brush_color.setText(QCoreApplication.translate("dialog_settins_el", u"color", None))
        self.btn_brush_color.setText("")
        self.lbl_brush_style.setText(QCoreApplication.translate("dialog_settins_el", u"style", None))
        self.com_box_brush_style.setItemText(0, QCoreApplication.translate("dialog_settins_el", u"NoBrush", None))
        self.com_box_brush_style.setItemText(1, QCoreApplication.translate("dialog_settins_el", u"SolidPattern", None))
        self.com_box_brush_style.setItemText(2, QCoreApplication.translate("dialog_settins_el", u"Dense1Pattern", None))
        self.com_box_brush_style.setItemText(3, QCoreApplication.translate("dialog_settins_el", u"Dense2Pattern", None))
        self.com_box_brush_style.setItemText(4, QCoreApplication.translate("dialog_settins_el", u"Dense3Pattern", None))
        self.com_box_brush_style.setItemText(5, QCoreApplication.translate("dialog_settins_el", u"Dense4Pattern", None))
        self.com_box_brush_style.setItemText(6, QCoreApplication.translate("dialog_settins_el", u"Dense5Pattern", None))
        self.com_box_brush_style.setItemText(7, QCoreApplication.translate("dialog_settins_el", u"Dense6Pattern", None))
        self.com_box_brush_style.setItemText(8, QCoreApplication.translate("dialog_settins_el", u"Dense7Pattern", None))
        self.com_box_brush_style.setItemText(9, QCoreApplication.translate("dialog_settins_el", u"HorPattern", None))
        self.com_box_brush_style.setItemText(10, QCoreApplication.translate("dialog_settins_el", u"VerPattern", None))
        self.com_box_brush_style.setItemText(11, QCoreApplication.translate("dialog_settins_el", u"CrossPattern", None))
        self.com_box_brush_style.setItemText(12, QCoreApplication.translate("dialog_settins_el", u"BDiagPattern", None))
        self.com_box_brush_style.setItemText(13, QCoreApplication.translate("dialog_settins_el", u"FDiagPattern", None))
        self.com_box_brush_style.setItemText(14, QCoreApplication.translate("dialog_settins_el", u"DiagCrossPattern", None))
        self.com_box_brush_style.setItemText(15, QCoreApplication.translate("dialog_settins_el", u"LinearGradientPattern", None))
        self.com_box_brush_style.setItemText(16, QCoreApplication.translate("dialog_settins_el", u"RadialGradientPattern", None))
        self.com_box_brush_style.setItemText(17, QCoreApplication.translate("dialog_settins_el", u"ConicalGradientPattern", None))
        self.com_box_brush_style.setItemText(18, QCoreApplication.translate("dialog_settins_el", u"TexturePattern", None))

        self.gr_box_item.setTitle(QCoreApplication.translate("dialog_settins_el", u"item", None))
        self.lbl_z_index.setText(QCoreApplication.translate("dialog_settins_el", u"zIndex", None))
        self.lbl_box_opacity.setText(QCoreApplication.translate("dialog_settins_el", u"opacity", None))
    # retranslateUi

