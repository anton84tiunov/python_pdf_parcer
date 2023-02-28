import copy

from PySide6 import QtCore, QtGui, QtWidgets

import src.Utility.general.comfig.config as config
import src.Utility.pdf_editor.get_set_default_style as get_set_default_style
import src.View.my_widgets.pdf_editor.dialog.my_dialog_settings_img as my_dialog_settings_img


class MyDialogPropImg(QtWidgets.QDialog, my_dialog_settings_img.Ui_Dialog):
    
    def __init__(self, root: QtWidgets, pix: QtGui.QPixmap, item_z_index: float, item_opacity: float, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.root: QtWidgets = root
        self.setStyleSheet(self.root.styleSheet())

















