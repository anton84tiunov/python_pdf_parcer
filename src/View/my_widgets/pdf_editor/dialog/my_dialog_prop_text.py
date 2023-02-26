import copy

from PySide6 import QtCore, QtGui, QtWidgets

import src.Utility.general.comfig.config as config
import src.Utility.pdf_editor.get_set_default_style as get_set_default_style
import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_text as my_dialog_settings_text


class MyDialogPropText(QtWidgets.QDialog, my_dialog_settings_text.Ui_Dialog):
    
    def __init__(self, root: QtWidgets,text:str,  font: QtGui.QFont, color: QtGui.QColor, item_z_index: float, item_opacity: float, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.root: QtWidgets = root
        self.setStyleSheet(self.root.styleSheet())
        self.text = text
        self.m_font = font
        self.color: QtGui.QColor = color
        # item.defaultTextColor()
        self.font_size: float = font.pointSizeF()
        # print(font.pixelSize())
       
        self.font_family: str = font.family()
        self.font_italic: bool = font.italic()
        self.font_bold: bool = font.bold()

        self.item_z_index: float = item_z_index
        self.item_opacity: float = item_opacity

        self.btn_color.setStyleSheet(f"background-color: {self.color.name()}")
        self.sp_box_size.setValue(self.font_size)
        self.ch_box_italic.setChecked(bool(self.font_italic))
        self.ch_box_bold.setChecked(bool(self.font_bold))
        self.l_e_text.setText(self.text)
        self.com_box_family.addItems(QtGui.QFontDatabase().families())
        self.com_box_family.setCurrentText(self.font_family)
        self.dbl_sp_box_z_index.setValue(self.item_z_index)
        self.dbl_sp_box_opacity.setValue(self.item_opacity)


        self.btn_color.clicked.connect(self.get_color)
        self.sp_box_size.valueChanged.connect(self.get_size)
        self.ch_box_italic.toggled.connect(self.get_italic)
        self.ch_box_bold.toggled.connect(self.get_bold)
        self.l_e_text.textChanged.connect(self.get_text)
        self.com_box_family.currentTextChanged.connect(self.get_family)
        self.dbl_sp_box_opacity.valueChanged.connect(self.get_opacity)
        self.dbl_sp_box_z_index.valueChanged.connect(self.get_z_index)

        self.btn_default.clicked.connect(self.set_default)
        self.btn_ok.clicked.connect(self.get_value)
        self.btn_cancel.clicked.connect(self.get_exit)


        self.background_brush = QtGui.QBrush( QtGui.QColor(232, 235, 232), QtCore.Qt.SolidPattern)

        self.scene_priview = QtWidgets.QGraphicsScene()
        self.scene_priview.setBackgroundBrush(self.background_brush)
        self.gr_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.gr_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scene_priview.setSceneRect(QtCore.QRectF(0.0, 0.0, 250.0, 100.0))
        self.gr_view.setScene(self.scene_priview)

        self.text_item = QtWidgets.QGraphicsTextItem(self.text)
        self.text_item.setFont(self.m_font)
        self.text_item.setDefaultTextColor(self.color)
        self.scene_priview.addItem(self.text_item)
        # print(self.text_item.font())
    
    def set_default(self):
        conf_path = "configs/default_style_el_config.INI"

        config.update_setting(conf_path, "text", "size",str( self.font_size))
        config.update_setting(conf_path, "text", "family", self.font_family)
        config.update_setting(conf_path, "text", "bold",str( self.font_bold))
        config.update_setting(conf_path, "text", "italic",str( self.font_italic))
        config.update_setting(conf_path, "text", "color",str( self.color.getRgb()))
      

    def get_value(self):

        self.accept()

    def get_exit(self):
        self.reject()

    def set_value(self):
        ...
        # self.val = self.l_e_dash_pattern.text()

    def update_priview(self):
        ...

    def get_opacity(self, val):
        self.item_opacity = val    

    def get_z_index(self, val):
        self.item_z_index = val

    def get_color(self):
        color_dialog = QtWidgets.QColorDialog()
        self.color = color_dialog.getColor()
        self.btn_color.setStyleSheet(f"background-color:{self.color.name()}")
        self.text_item.setDefaultTextColor(self.color)

    def get_size(self, size: float):
        self.font_size = size
        self.m_font.setPointSizeF(self.font_size)
        self.text_item.setFont(self.m_font)

    def get_italic(self, italic: bool):
        self.font_italic = italic
        self.m_font.setItalic(self.font_italic)
        self.text_item.setFont(self.m_font)

    def get_bold(self, bold: bool):
        self.font_bold = bold
        self.m_font.setBold(self.font_bold)
        self.text_item.setFont(self.m_font)

    def get_text(self, text: str):
        self.text = text
        self.text_item.setPlainText(self.text)

    def get_family(self, family):
        self.font_family = family
        self.m_font.setFamily(self.font_family)
        self.text_item.setFont(self.m_font)






                 