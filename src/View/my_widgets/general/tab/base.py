import sys
from PySide6 import QtWidgets, QtGui,  QtCore 


class TabBase(QtWidgets.QWidget):
    """Бпзовый класс для создания вкладок QTabWidget"""

    def __init__(self, obj_name):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        # self.setToolTip(obj_name)
        self.setObjectName(obj_name)

        self.h_box_lay = QtWidgets.QHBoxLayout()
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.h_box_lay)
        self.split_hor = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.split_hor.setContentsMargins(0, 0, 0, 0)
        self.h_box_lay.addWidget(self.split_hor) 
        
        self.frame_left_panel = QtWidgets.QFrame()
        self.frame_left_panel.setContentsMargins(0, 0, 0, 0)
        self.frame_left_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)


        self.frame_right_panel = QtWidgets.QFrame()
        self.frame_right_panel.setContentsMargins(0, 0, 0, 0)

        self.split_hor.addWidget(self.frame_left_panel)
        self.split_hor.addWidget(self.frame_right_panel)
        self.split_hor.setStretchFactor(0, 1)
        self.split_hor.setStretchFactor(1, 10)
        self.split_hor.setSizes([10, 100])

        self.v_box_lay = QtWidgets.QVBoxLayout()
        self.v_box_lay.setContentsMargins(0, 0, 0, 0)
        self.frame_right_panel.setLayout(self.v_box_lay)

        self.split_ver = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.split_ver.setContentsMargins(0, 0, 0, 0)
        self.v_box_lay.addWidget(self.split_ver) 
        
        self.frame_right_top_panel = QtWidgets.QFrame()
        self.frame_right_top_panel.setContentsMargins(0, 0, 0, 0)
        self.frame_right_top_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame_right_bottom_panel = QtWidgets.QFrame()
        self.frame_right_bottom_panel.setContentsMargins(0, 0, 0, 0)
        self.frame_right_bottom_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)


        self.split_ver.addWidget(self.frame_right_top_panel)
        self.split_ver.addWidget(self.frame_right_bottom_panel)
        self.split_ver.setStretchFactor(0, 30)
        self.split_ver.setStretchFactor(1, 1)
        self.split_ver.setSizes([100, 5])