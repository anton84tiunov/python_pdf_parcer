# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_settings_imgraXEmS.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(340, 217)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_z_index = QLabel(self.groupBox_2)
        self.lbl_z_index.setObjectName(u"lbl_z_index")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_z_index)

        self.dbl_sp_box_z_index = QDoubleSpinBox(self.groupBox_2)
        self.dbl_sp_box_z_index.setObjectName(u"dbl_sp_box_z_index")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.dbl_sp_box_z_index)

        self.lbl_opacity = QLabel(self.groupBox_2)
        self.lbl_opacity.setObjectName(u"lbl_opacity")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_opacity)

        self.dbl_sp_box_opacity = QDoubleSpinBox(self.groupBox_2)
        self.dbl_sp_box_opacity.setObjectName(u"dbl_sp_box_opacity")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.dbl_sp_box_opacity)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.lbl_width = QLabel(self.groupBox)
        self.lbl_width.setObjectName(u"lbl_width")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lbl_width)

        self.dbl_sp_box_width = QDoubleSpinBox(self.groupBox)
        self.dbl_sp_box_width.setObjectName(u"dbl_sp_box_width")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.dbl_sp_box_width)

        self.ibi_height = QLabel(self.groupBox)
        self.ibi_height.setObjectName(u"ibi_height")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.ibi_height)

        self.dbl_sp_box_height = QDoubleSpinBox(self.groupBox)
        self.dbl_sp_box_height.setObjectName(u"dbl_sp_box_height")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.dbl_sp_box_height)

        self.btn_select_file = QPushButton(self.groupBox)
        self.btn_select_file.setObjectName(u"btn_select_file")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.btn_select_file)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_default = QPushButton(Dialog)
        self.btn_default.setObjectName(u"btn_default")

        self.horizontalLayout_2.addWidget(self.btn_default)

        self.btn_save_to_file = QPushButton(Dialog)
        self.btn_save_to_file.setObjectName(u"btn_save_to_file")

        self.horizontalLayout_2.addWidget(self.btn_save_to_file)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")

        self.horizontalLayout_2.addWidget(self.btn_ok)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"item", None))
        self.lbl_z_index.setText(QCoreApplication.translate("Dialog", u"z index", None))
        self.lbl_opacity.setText(QCoreApplication.translate("Dialog", u"opacity", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"pixmap", None))
        self.lbl_width.setText(QCoreApplication.translate("Dialog", u"width", None))
        self.ibi_height.setText(QCoreApplication.translate("Dialog", u"height", None))
        self.btn_select_file.setText(QCoreApplication.translate("Dialog", u"file", None))
        self.btn_default.setText(QCoreApplication.translate("Dialog", u"default", None))
        self.btn_save_to_file.setText(QCoreApplication.translate("Dialog", u"save to file", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"cancel", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"ok", None))
    # retranslateUi

