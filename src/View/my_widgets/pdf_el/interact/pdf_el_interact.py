import sys, re, math, json
from collections import OrderedDict
import pickle
from PySide6 import QtWidgets, QtGui,  QtCore 
import asyncio
# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_el.tab.pdf_el_tab as pdf_el_tab



red_style = "background-color: rgb(255, 0, 0);"
green_style = "background-color: rgb(0, 255, 0);"
blue_style = "background-color: rgb(0, 0, 255);"

class GrIt(QtWidgets.QGraphicsItem):
    def __init__(self):
        super().__init__()


class PdfElInteract(pdf_el_tab.TabPdfEl):
    """класс для обработки событий в GUI "PDF el" """

    def __init__(self, root: QtWidgets):
        super().__init__(root)
        self.root: QtWidgets = root

        self.pdf_el_path_open_qt_file = ""
       
        self.frame_menu.btn_open_qt.clicked.connect(self.open_qt)
        # self.frame_menu.btn_open_qt.click

    def open_qt(self):
        self.pdf_el_path_open_qt_file = QtWidgets.QFileDialog.getOpenFileName(self, 'Open pdf_ex', "",'Pdf_ex(*.pdf_ex);;All(*)' )[0]
        if self.pdf_el_path_open_qt_file != '':
            # self.pdf_editor_scene.clear()

            with open(self.pdf_el_path_open_qt_file) as json_file:
                data = json.load(json_file)
                
                self.list_widgets_graph_el.clear()
                
                for num_it in range(len(data['items'])):
                    list_item = QtWidgets.QListWidgetItem()
                    list_item.setText(data['items'][num_it]["i_type"])
                    # list_item.setIcon(QtGui.QIcon(QtGui.QPixmap()))
                    self.list_widgets_graph_el.addItem(list_item)

                    if data['items'][num_it]["i_type"] == "path":
                        print("path")


                    elif data['items'][num_it]["i_type"] == "pol":
                        print("pol")

                    elif data['items'][num_it]["i_type"] == "rect":
                        print("rect")

                    elif data['items'][num_it]["i_type"] == "ell":
                        print("ell")

                    elif data['items'][num_it]["i_type"] == "text":
                        print("text")

                    elif data['items'][num_it]["i_type"] == "img":
                        print("img")





















