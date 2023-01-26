import sys
from PySide2 import QtWidgets, QtGui,  QtCore 
import src.View.my_widgets.general.tab.base as tab_base


class TabPdfEl(tab_base.TabBase):
    """класс для создания вкладки "PDF EL" """

    def __init__(self):
        super().__init__("pdf_el")