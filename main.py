import sys
from numba import njit
import src.Utility.general.comfig.config as config
from PySide6 import QtWidgets, QtGui,  QtCore 
# import src.View.style.win_style as my_style
import src.View.my_window.main_window as main_window
import my_os_path
import src.Utility.loging.base_loger as base_loger


win_icon = my_os_path.icon_ico + "icon.ico"

win_style = "win_style"

# @njit( parallel=True)
def main():

    base_loger.init_loger('app')
    
    win_style = config.get_setting(config.resource_path("configs/sryle_config.INI"), "Style", "current_style")

    app = QtWidgets.QApplication(sys.argv)
    # print(app.styleSheet())
    app.setStyleSheet(open(config.resource_path("style/" + win_style + ".qss"), "r").read())


    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(win_icon))
    app.setWindowIcon(icon)
    window = main_window.MainWindow()
    # window.tab_pdf_editor.graph_scene.addRect(120.0, 20.0, 100.0, 100.0)
    # print(window.styleSheet())
    window.show()
    sys.exit(app.exec())
    # app.exec_()


if __name__ == "__main__":
    main()


 
 



























































































