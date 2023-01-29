from PySide2 import QtCore, QtGui, QtWidgets

import src.View.my_window.main_window as main_window

class DialogScalePath(object):
    def setupUi(self, pdf_editor_dialog_scale):
        pdf_editor_dialog_scale.setObjectName("pdf_editor_dialog_scale")
        pdf_editor_dialog_scale.resize(212, 116)
        self.verticalLayout = QtWidgets.QVBoxLayout(pdf_editor_dialog_scale)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.sp_box_scale = QtWidgets.QDoubleSpinBox(pdf_editor_dialog_scale)
        self.sp_box_scale.setMinimum(1.0)
        self.sp_box_scale.setMaximum(1000000.0)
        self.sp_box_scale.setProperty("value", 100.0)
        self.sp_box_scale.setObjectName("sp_box_scale")
        self.verticalLayout.addWidget(self.sp_box_scale)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_scale_cancel = QtWidgets.QPushButton(pdf_editor_dialog_scale)
        self.btn_scale_cancel.setObjectName("btn_scale_cancel")
        self.horizontalLayout.addWidget(self.btn_scale_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_scale_ok = QtWidgets.QPushButton(pdf_editor_dialog_scale)
        self.btn_scale_ok.setObjectName("btn_scale_ok")
        self.horizontalLayout.addWidget(self.btn_scale_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(pdf_editor_dialog_scale)
        QtCore.QMetaObject.connectSlotsByName(pdf_editor_dialog_scale)

    def retranslateUi(self, pdf_editor_dialog_scale):
        _translate = QtCore.QCoreApplication.translate
        pdf_editor_dialog_scale.setWindowTitle(_translate("pdf_editor_dialog_scale", "pdf editor dialog scale"))
        self.btn_scale_cancel.setText(_translate("pdf_editor_dialog_scale", "cancel"))
        self.btn_scale_ok.setText(_translate("pdf_editor_dialog_scale", "ok"))

class MyDialogScalePath(QtWidgets.QDialog, DialogScalePath):
    
    def __init__(self, root: main_window.MainWindow, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.root: main_window.MainWindow = root
        self.setStyleSheet(self.main.styleSheet())
        self.val_scale = 0
        self.btn_scale_ok.clicked.connect(self.get_value)

    def get_value(self):
        self.val_scale = self.sp_box_scale.value()
        self.accept()

    def go_end(self):       
        self.hide()


