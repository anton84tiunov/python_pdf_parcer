from PySide2 import QtCore, QtGui, QtWidgets

# import src.View.my_window.main_window as main_window


class DialogRotatePath(object):
    def setupUi(self, pdf_editor_dialog_rotate):
        pdf_editor_dialog_rotate.setObjectName("pdf_editor_dialog_rotate")
        pdf_editor_dialog_rotate.resize(212, 116)
        self.verticalLayout = QtWidgets.QVBoxLayout(pdf_editor_dialog_rotate)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.sp_box_rotate = QtWidgets.QDoubleSpinBox(pdf_editor_dialog_rotate)
        self.sp_box_rotate.setMinimum(-360.0)
        self.sp_box_rotate.setMaximum(360.0)
        self.sp_box_rotate.setSingleStep(0.5)
        self.sp_box_rotate.setObjectName("sp_box_rotate")
        self.verticalLayout.addWidget(self.sp_box_rotate)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_rotate_cancel = QtWidgets.QPushButton(pdf_editor_dialog_rotate)
        self.btn_rotate_cancel.setObjectName("btn_rotate_cancel")
        self.horizontalLayout.addWidget(self.btn_rotate_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_rotate_ok = QtWidgets.QPushButton(pdf_editor_dialog_rotate)
        self.btn_rotate_ok.setObjectName("btn_rotate_ok")
        self.horizontalLayout.addWidget(self.btn_rotate_ok)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(pdf_editor_dialog_rotate)
        QtCore.QMetaObject.connectSlotsByName(pdf_editor_dialog_rotate)

    def retranslateUi(self, pdf_editor_dialog_rotate):
        _translate = QtCore.QCoreApplication.translate
        pdf_editor_dialog_rotate.setWindowTitle(_translate("pdf_editor_dialog_rotate", "pdf editor dialog rotate"))
        self.btn_rotate_cancel.setText(_translate("pdf_editor_dialog_rotate", "cancel"))
        self.btn_rotate_ok.setText(_translate("pdf_editor_dialog_rotate", "ok"))


class MyDialogRotatePath(QtWidgets.QDialog, DialogRotatePath):
    
    def __init__(self, root: QtWidgets, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.root: QtWidgets = root
        self.setStyleSheet(self.main.styleSheet())
        self.val_rotate = 0
        self.btn_rotate_ok.clicked.connect(self.get_value)

    def get_value(self):
        self.val_rotate = self.sp_box_rotate.value()
        self.accept()

    def go_end(self):       
        self.hide()