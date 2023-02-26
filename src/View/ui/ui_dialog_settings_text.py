# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_settings_textbvAkJy.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QDoubleSpinBox, QFormLayout, QGraphicsView, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(361, 248)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_color = QLabel(Dialog)
        self.lbl_color.setObjectName(u"lbl_color")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_color)

        self.lbl_italic = QLabel(Dialog)
        self.lbl_italic.setObjectName(u"lbl_italic")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_italic)

        self.lbl_size = QLabel(Dialog)
        self.lbl_size.setObjectName(u"lbl_size")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_size)

        self.btn_color = QPushButton(Dialog)
        self.btn_color.setObjectName(u"btn_color")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.btn_color)

        self.ch_box_italic = QCheckBox(Dialog)
        self.ch_box_italic.setObjectName(u"ch_box_italic")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ch_box_italic)

        self.lbl_bold = QLabel(Dialog)
        self.lbl_bold.setObjectName(u"lbl_bold")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lbl_bold)

        self.ch_box_bold = QCheckBox(Dialog)
        self.ch_box_bold.setObjectName(u"ch_box_bold")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ch_box_bold)

        self.sp_box_size = QDoubleSpinBox(Dialog)
        self.sp_box_size.setObjectName(u"sp_box_size")
        self.sp_box_size.setMinimum(0.100000000000000)
        self.sp_box_size.setMaximum(999.990000000000009)
        self.sp_box_size.setSingleStep(0.100000000000000)
        self.sp_box_size.setValue(1.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.sp_box_size)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_default = QPushButton(Dialog)
        self.btn_default.setObjectName(u"btn_default")

        self.verticalLayout_3.addWidget(self.btn_default)

        self.btn_ok = QPushButton(Dialog)
        self.btn_ok.setObjectName(u"btn_ok")

        self.verticalLayout_3.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.verticalLayout_3.addWidget(self.btn_cancel)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_text = QLabel(Dialog)
        self.lbl_text.setObjectName(u"lbl_text")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lbl_text)

        self.l_e_text = QLineEdit(Dialog)
        self.l_e_text.setObjectName(u"l_e_text")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.l_e_text)

        self.lbl_family = QLabel(Dialog)
        self.lbl_family.setObjectName(u"lbl_family")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lbl_family)

        self.com_box_family = QComboBox(Dialog)
        self.com_box_family.setObjectName(u"com_box_family")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.com_box_family)

        self.lbl_z_index = QLabel(Dialog)
        self.lbl_z_index.setObjectName(u"lbl_z_index")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lbl_z_index)

        self.dbl_sp_box_z_index = QDoubleSpinBox(Dialog)
        self.dbl_sp_box_z_index.setObjectName(u"dbl_sp_box_z_index")
        self.dbl_sp_box_z_index.setMinimum(-99999999.900000005960464)
        self.dbl_sp_box_z_index.setMaximum(99999999.989999994635582)
        self.dbl_sp_box_z_index.setSingleStep(0.100000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.dbl_sp_box_z_index)

        self.lbl_box_opacity = QLabel(Dialog)
        self.lbl_box_opacity.setObjectName(u"lbl_box_opacity")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lbl_box_opacity)

        self.dbl_sp_box_opacity = QDoubleSpinBox(Dialog)
        self.dbl_sp_box_opacity.setObjectName(u"dbl_sp_box_opacity")
        self.dbl_sp_box_opacity.setMaximum(1.000000000000000)
        self.dbl_sp_box_opacity.setSingleStep(0.100000000000000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.dbl_sp_box_opacity)


        self.gridLayout_2.addLayout(self.formLayout_2, 1, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gr_view = QGraphicsView(Dialog)
        self.gr_view.setObjectName(u"gr_view")
        self.gr_view.setMinimumSize(QSize(250, 100))
        self.gr_view.setMaximumSize(QSize(250, 100))
        self.gr_view.setSizeIncrement(QSize(250, 100))
        self.gr_view.setBaseSize(QSize(250, 100))

        self.gridLayout.addWidget(self.gr_view, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_color.setText(QCoreApplication.translate("Dialog", u"color", None))
        self.lbl_italic.setText(QCoreApplication.translate("Dialog", u"italic", None))
        self.lbl_size.setText(QCoreApplication.translate("Dialog", u"size", None))
        self.btn_color.setText("")
        self.ch_box_italic.setText("")
        self.lbl_bold.setText(QCoreApplication.translate("Dialog", u"bold", None))
        self.ch_box_bold.setText("")
        self.btn_default.setText(QCoreApplication.translate("Dialog", u"default", None))
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("Dialog", u"cancel", None))
        self.lbl_text.setText(QCoreApplication.translate("Dialog", u"text", None))
        self.lbl_family.setText(QCoreApplication.translate("Dialog", u"family", None))
        self.lbl_z_index.setText(QCoreApplication.translate("Dialog", u"zIndex", None))
        self.lbl_box_opacity.setText(QCoreApplication.translate("Dialog", u"opacity", None))
    # retranslateUi

