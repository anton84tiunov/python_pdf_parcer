# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_settings_textugJDgz.ui'
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
    QFormLayout, QGraphicsView, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(355, 226)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pushButton_4)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.checkBox)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBox_2)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox)


        self.gridLayout_2.addLayout(self.formLayout_2, 1, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(250, 100))
        self.graphicsView.setMaximumSize(QSize(250, 100))
        self.graphicsView.setSizeIncrement(QSize(250, 100))
        self.graphicsView.setBaseSize(QSize(250, 100))

        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"color", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"italic", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"size", None))
        self.pushButton_4.setText("")
        self.checkBox.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"bold", None))
        self.checkBox_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"default", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"ok", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"cancel", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"text", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"family", None))
    # retranslateUi

