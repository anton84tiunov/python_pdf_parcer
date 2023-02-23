from PySide6 import QtCore, QtGui, QtWidgets

# import src.View.my_window.main_window as main_window

class DialogPropEll(object):
    def setupUi(self, pdf_editor_dialog_prop_ell):
        pdf_editor_dialog_prop_ell.setObjectName("pdf_editor_dialog_prop_ell")
        pdf_editor_dialog_prop_ell.resize(212, 116)
        self.verticalLayout = QtWidgets.QVBoxLayout(pdf_editor_dialog_prop_ell)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.sp_box_prop = QtWidgets.QDoubleSpinBox(pdf_editor_dialog_prop_ell)
        self.sp_box_prop.setMinimum(1.0)
        self.sp_box_prop.setMaximum(1000000.0)
        self.sp_box_prop.setProperty("value", 100.0)
        self.sp_box_prop.setObjectName("sp_box_prop")
        self.verticalLayout.addWidget(self.sp_box_prop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_prop_cancel = QtWidgets.QPushButton(pdf_editor_dialog_prop_ell)
        self.btn_prop_cancel.setObjectName("btn_prop_cancel")
        self.horizontalLayout.addWidget(self.btn_prop_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_prop_ok = QtWidgets.QPushButton(pdf_editor_dialog_prop_ell)
        self.btn_prop_ok.setObjectName("btn_prop_ok")
        self.horizontalLayout.addWidget(self.btn_prop_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(pdf_editor_dialog_prop_ell)
        QtCore.QMetaObject.connectSlotsByName(pdf_editor_dialog_prop_ell)

    def retranslateUi(self, pdf_editor_dialog_prop_ell):
        _translate = QtCore.QCoreApplication.translate
        pdf_editor_dialog_prop_ell.setWindowTitle(_translate("pdf_editor_dialog_prop_ell", "pdf editor dialog scale"))
        self.btn_prop_cancel.setText(_translate("pdf_editor_dialog_prop_ell", "cancel"))
        self.btn_prop_ok.setText(_translate("pdf_editor_dialog_prop_ell", "ok"))

class MyDialogPropEll(QtWidgets.QDialog, DialogPropEll):
    
    def __init__(self, root: QtWidgets, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.root: QtWidgets = root
        self.setStyleSheet(self.root.styleSheet())
        self.val_prop = 0
        self.btn_prop_ok.clicked.connect(self.get_value)

    def get_value(self):
        self.val_prop = self.sp_box_prop.value()
        self.accept()

    def go_end(self):       
        self.hide()