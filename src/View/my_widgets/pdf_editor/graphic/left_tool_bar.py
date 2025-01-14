import sys, os
from PySide6 import QtWidgets, QtGui,  QtCore 
# import src.View.my_window.main_window as main_window
import src.View.my_widgets.pdf_editor.graphic.pointer_path.my_pointer_path as my_pointer_path
import src.View.my_widgets.pdf_editor.graphic.polygon.my_polygon as my_polygon
import src.View.my_widgets.pdf_editor.graphic.rectangle.my_rectangle as my_rectangle
import src.View.my_widgets.pdf_editor.graphic.image.my_image as my_image
import src.View.my_widgets.pdf_editor.graphic.text.my_text_item as my_text_item

import src.View.my_widgets.general.button.radio_buttom as radio_buttom

import src.View.my_widgets.general.button.combo_box_num as combo_box_num

import my_os_path as my_os_path

icon_dir = my_os_path.icon
icon_svg_dir = my_os_path.icon_svg

red_style = "background-color: rgb(255, 0, 0);"
green_style = "background-color: rgb(0, 255, 0);"
blue_style = "background-color: rgb(0, 0, 255);"

class MyLeftToolBar(QtWidgets.QFrame):
    """класс для выбора способа взаимодействия с элементами 
        графической сцены и ей самой."""
        
    def __init__(self, root: QtWidgets, **kwargs):
        super().__init__( **kwargs)
        self.root: QtWidgets = root
        self.tool_cursors: list[str] = ["arrow", "hand", "move", "pencil", "line", "bezier", "polygon", "rect", "circle", "text", "ruler"]
        self.tool_cursor: str = ""

        self.c_cursor: bool = True
        # self.rect_page_cursor = "arrow"
        # self.scene_cursor = "arrow"
        # self.view_cursor = "arrow"
        

        # self.setStyleSheet(green_style)

        self.v_box = QtWidgets.QVBoxLayout(self)

        # self.setLayout(self.v_box)
        self.v_box.setContentsMargins(0, 0, 0, 0)

        # self.btn_save_qt = QtWidgets.QPushButton("", self)
        # self.v_box.addWidget(self.btn_save_qt)

        # self.r_btn_cursor_arrow = QtWidgets.QRadioButton()
        self.r_btn_cursor_arrow = radio_buttom.MyRadioButton(self, '8666726_mouse_pointer_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_arrow)
        self.r_btn_cursor_arrow.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_arrow, "arrow"))
        
        self.r_btn_cursor_hand = radio_buttom.MyRadioButton(self, '8664932_hand_gesture_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_hand)
        self.r_btn_cursor_hand.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_hand, "hand"))
        
        self.r_btn_cursor_move = radio_buttom.MyRadioButton(self, '9035986_move_sharp_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_move)
        self.r_btn_cursor_move.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_move, "move"))
        
        self.r_btn_cursor_pencil = radio_buttom.MyRadioButton(self, '9035966_pencil_sharp_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_pencil)
        self.r_btn_cursor_pencil.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_pencil, "pencil"))
        
        self.r_btn_cursor_line = radio_buttom.MyRadioButton(self, '352898_linearray_lines_shape_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_line)
        self.r_btn_cursor_line.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_line, "line"))
        
        self.r_btn_cursor_bezier = radio_buttom.MyRadioButton(self, '352897_path_shape_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_bezier)
        self.r_btn_cursor_bezier.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_bezier, "bezier"))
        
        self.r_btn_cursor_polygon = radio_buttom.MyRadioButton(self, '352895_polygon_shape_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_polygon)
        self.r_btn_cursor_polygon.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_polygon, "polygon"))
        
        self.r_btn_cursor_rect = radio_buttom.MyRadioButton(self, '8664870_square_shape_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_rect)
        self.r_btn_cursor_rect.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_rect, "rect"))
        
        self.r_btn_cursor_circle = radio_buttom.MyRadioButton(self, '9035952_radio_button_off_sharp_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_circle)
        self.r_btn_cursor_circle.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_circle, "circle"))
        
        self.r_btn_cursor_text = radio_buttom.MyRadioButton(self, '9036041_text_sharp_icon.png')
        self.v_box.addWidget(self.r_btn_cursor_text)
        self.r_btn_cursor_text.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_text, "text"))
        
        
        self.r_btn_cursor_img = radio_buttom.MyRadioButton(self, 'img.png')
        self.v_box.addWidget(self.r_btn_cursor_img)
        self.r_btn_cursor_img.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_img, "img"))
        
        self.r_btn_cursor_ruler= radio_buttom.MyRadioButton(self, 'student_ruler_school_brush_learning_stationery_icon_230451.png')
        self.v_box.addWidget(self.r_btn_cursor_ruler)
        self.r_btn_cursor_ruler.clicked.connect(lambda: self.disable_checked(self.r_btn_cursor_ruler, "ruler"))
        
        self.spacer_tool_box = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_box.addItem(self.spacer_tool_box)

    def text_changed(self, s):
        self.root.tab_pdf_editor.graph_scene.grid_step = int(s)
        # print(int(s))


    def disable_checked(self, check_btn: radio_buttom.MyRadioButton, cursor: str):
        size_cursor = QtCore.QSize(50, 50)
        self.r_btn_cursor_arrow.setChecked(False)
        self.r_btn_cursor_hand.setChecked(False)
        self.r_btn_cursor_move.setChecked(False)
        self.r_btn_cursor_pencil.setChecked(False)
        self.r_btn_cursor_line.setChecked(False)
        self.r_btn_cursor_bezier.setChecked(False)
        self.r_btn_cursor_polygon.setChecked(False)
        self.r_btn_cursor_rect.setChecked(False)
        self.r_btn_cursor_circle.setChecked(False)
        self.r_btn_cursor_text.setChecked(False)
        self.r_btn_cursor_img.setChecked(False)
        self.r_btn_cursor_ruler.setChecked(False)
        self.tool_cursor = cursor
        check_btn.setChecked(True)

        if cursor in  ["arrow", "hand", "move", "ruler"]:
            
            self.c_cursor = True
            
            if cursor == "arrow":
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            
            elif cursor == "hand":
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            
            elif cursor == "move":
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(QtCore.Qt.CursorShape.ArrowCursor)
            
            elif cursor == "ruler":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_ruller.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        else:

            self.c_cursor = False

            if cursor == "pencil":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_pencil.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

            elif cursor == "line":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_line.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

            elif cursor == "bezier":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_curve.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

            elif cursor == "polygon":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_polygon.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

            elif cursor == "rect":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_rect.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

            elif cursor == "circle":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_circle.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

            elif cursor == "text":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_text.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

            elif cursor == "img":
                self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_image_itemt.png")
                self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
                self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
                self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        for item in self.root.tab_pdf_editor.graph_scene.items():
            if hasattr(item, "delete_attribute_my_point_rect"):
                self.root.tab_pdf_editor.graph_scene.removeItem(item)
            if hasattr(item, "current_cursor"):
                if self.c_cursor:
                    # item.setFlag(QtWidgets.QGraphicsItem.unsetCursor, False)
                    item.setCursor(item.current_cursor)
                else:
                    # item.setFlag(QtWidgets.QGraphicsItem.unsetCursor, True)
                    item.setCursor(self.root.tab_pdf_editor.graph_view.viewport().cursor())










































        
        # if cursor == "move":
        #     # self.root.tab_pdf_editor.graph_scene.blockSignals(False)
        #     self.root.tab_pdf_editor.graph_view.viewport().setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        #     for item in self.root.tab_pdf_editor.graph_scene.items():
        #         if hasattr(item, "delete_attribute_my_point_rect"):
        #             self.root.tab_pdf_editor.graph_scene.removeItem(item)
        #         # item.setCursor(item.all_size_cursor)
        #         if not hasattr(item, "attribute_rect_page"):
        #             item.setCursor(QtCore.Qt.CursorShape.SizeAllCursor)
        #         else:
        #             item.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
  
        # elif cursor in ["arrow", "hand"]:
        #     # self.root.tab_pdf_editor.graph_scene.blockSignals(False)
        #     self.root.tab_pdf_editor.graph_view.viewport().setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        #     for item in self.root.tab_pdf_editor.graph_scene.items():
        #         # item.setFlag(QtWidgets.QGraphicsItem.unsetCursor, False)
  
        #         if not hasattr(item, "attribute_cross_line"):
     
        #             if hasattr(item, "delete_attribute_my_point_rect"):
        #                 self.root.tab_pdf_editor.graph_scene.removeItem(item)
        #             if item != QtWidgets.QGraphicsLineItem:
        #                 if hasattr(item, "current_cursor"):
        #                     item.setCursor(item.current_cursor)
        #             if hasattr(item, "attribute_rect_page"):
        #                 item.setCursor(QtCore.Qt.CursorShape.ArrowCursor)
        # else :
        #     # self.root.tab_pdf_editor.graph_scene.blockSignals(True)
        #     for item in self.root.tab_pdf_editor.graph_scene.items():
        #         if hasattr(item, "delete_attribute_my_point_rect"):
        #             self.root.tab_pdf_editor.graph_scene.removeItem(item)
        #         if item != QtWidgets.QGraphicsLineItem:
        #         # item.setCursor(item.current_cursor)
        #             item.unsetCursor()
        #         if hasattr(item, "attribute_rect_page"):
        #             item.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

        #     if cursor == "pencil":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_pencil.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        #     elif cursor == "line":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_line.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        #     elif cursor == "bezier":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_curve.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        #     elif cursor == "polygon":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_polygon.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        #     elif cursor == "rect":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_rect.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        #     elif cursor == "circle":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_circle.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        #     elif cursor == "text":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_text.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)

        #     elif cursor == "ruler":
        #         self.cursor_pix = QtGui.QPixmap(icon_svg_dir + "arrow_ruller.png")
        #         self.cursor_scaled_pix = self.cursor_pix.scaled(size_cursor, QtCore.Qt.KeepAspectRatio)
        #         self.current_cursor = QtGui.QCursor(self.cursor_scaled_pix, 1, -1)
        #         self.root.tab_pdf_editor.graph_view.viewport().setCursor(self.current_cursor)









