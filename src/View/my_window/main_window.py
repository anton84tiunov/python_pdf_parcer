import sys
from PySide6 import QtWidgets, QtGui,  QtCore 
import src.View.my_widgets.pdf_editor.interact.pdf_editor_interact as pdf_editor_tab
import src.View.my_widgets.pdf_el.interact.pdf_el_interact as pdf_el_tab
import src.View.my_widgets.general.menu.menu_bar as menu_bar
import my_os_path

win_icon = my_os_path.icon_ico + "icon.ico"

win_style = """font: 16pt \"PT Sans\";
            background-color: rgb(71, 71, 71);
            color: rgb(255, 255, 127);
            background-color: rgb(40, 40, 40);
            """
centr_style = "background-color: rgb(0, 255, 0);"

class MainWindow(QtWidgets.QMainWindow):
    """класс для создания главного окна приложения"""

    def __init__(self):
        super().__init__()
        # self.tab_pdf_editor.graph_left_tool_bar.tool_cursors
        # print(win_icon)
        self.setWindowTitle("приложение по работе с  pdf")
        # self.setStyleSheet(open("src/View/style/Clocker.qss", "r").read())
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(win_icon))
        self.setWindowIcon(icon)
        self.resize(800, 500)

        
        # self.setStyleSheet(win_style)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setContentsMargins(0, 0, 0, 0)

        self.ver_lay_centr = QtWidgets.QVBoxLayout(self.centralwidget)
        self.ver_lay_centr.setContentsMargins(0, 0, 0, 0)

        self.menu_bar = menu_bar.MenuBar(self)
        self.menu_bar.setContentsMargins(0, 0, 0, 0)
        self.ver_lay_centr.addWidget(self.menu_bar)

        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setContentsMargins(0, 0, 0, 0)
        self.ver_lay_centr.addWidget(self.tabWidget)

        # self.tabWidget.setStyleSheet(centr_style)
        self.tabWidget.setContentsMargins(0, 0, 0, 0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab_pdf_editor = pdf_editor_tab.PdfEditorInteract(self)
        self.tabWidget.addTab(self.tab_pdf_editor, "pdf_editor")
        self.tab_pdf_el = pdf_el_tab.PdfElInteract(self)
        self.tabWidget.addTab(self.tab_pdf_el, "pdf_el")
        self.setCentralWidget(self.centralwidget)
        
        # self.tab_pdf_editor.txt_brow_log
        # self.tab_pdf_editor.graph_scene.addRect(150.0, 150.0, 100.0, 100.0)
        # self.tab_pdf_editor.graph_view.setCursor
        

    #     self.tab_pdf_editor.frame_menu.btn_save_qt.clicked.connect(self.set_style)

    # def set_style(self):
    #     self.setStyleSheet(open("src/View/style/Clocker.qss", "r").read())


    # def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
    #     return super().closeEvent(event)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
                    self, 
                    "Exit", 
                    "Are you sure to quit?", 
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                    QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
             event.ignore()



















