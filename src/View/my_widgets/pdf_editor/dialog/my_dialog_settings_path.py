from PySide2 import QtCore, QtGui, QtWidgets

# import src.View.my_window.main_window as main_window

class DialogSettingsPath(object):
    def setupUi(self, PdfEditorDialogSettingsPathItem):
        PdfEditorDialogSettingsPathItem.setObjectName("PdfEditorDialogSettingsPathItem")
        PdfEditorDialogSettingsPathItem.setEnabled(True)
        PdfEditorDialogSettingsPathItem.resize(706, 443)
        PdfEditorDialogSettingsPathItem.setAccessibleName("")
        PdfEditorDialogSettingsPathItem.setStyleSheet("font: 16pt \"PT Sans\";\n"
"background-color: rgb(71, 71, 71);\n"
"color: rgb(255, 255, 127);\n"
"background-color: rgb(40, 40, 40);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PdfEditorDialogSettingsPathItem)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ch_box_stroke = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke.setObjectName("ch_box_stroke")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke)
        self.ch_box_stroke_color = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_color.setEnabled(False)
        self.ch_box_stroke_color.setObjectName("ch_box_stroke_color")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_color)
        self.btn_stroke_color = QtWidgets.QPushButton(PdfEditorDialogSettingsPathItem)
        self.btn_stroke_color.setEnabled(False)
        self.btn_stroke_color.setObjectName("btn_stroke_color")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_stroke_color)
        self.ch_box_stroke_style = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_style.setEnabled(False)
        self.ch_box_stroke_style.setObjectName("ch_box_stroke_style")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_style)
        self.com_box_stroke_style = QtWidgets.QComboBox(PdfEditorDialogSettingsPathItem)
        self.com_box_stroke_style.setEnabled(False)
        self.com_box_stroke_style.setObjectName("com_box_stroke_style")
        self.com_box_stroke_style.addItem("")
        self.com_box_stroke_style.addItem("")
        self.com_box_stroke_style.addItem("")
        self.com_box_stroke_style.addItem("")
        self.com_box_stroke_style.addItem("")
        self.com_box_stroke_style.addItem("")
        self.com_box_stroke_style.addItem("")
        self.com_box_stroke_style.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.com_box_stroke_style)
        self.com_box_stroke_join_style = QtWidgets.QComboBox(PdfEditorDialogSettingsPathItem)
        self.com_box_stroke_join_style.setEnabled(False)
        self.com_box_stroke_join_style.setObjectName("com_box_stroke_join_style")
        self.com_box_stroke_join_style.addItem("")
        self.com_box_stroke_join_style.addItem("")
        self.com_box_stroke_join_style.addItem("")
        self.com_box_stroke_join_style.addItem("")
        self.com_box_stroke_join_style.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.com_box_stroke_join_style)
        self.com_box_stroke_cap_style = QtWidgets.QComboBox(PdfEditorDialogSettingsPathItem)
        self.com_box_stroke_cap_style.setEnabled(False)
        self.com_box_stroke_cap_style.setObjectName("com_box_stroke_cap_style")
        self.com_box_stroke_cap_style.addItem("")
        self.com_box_stroke_cap_style.addItem("")
        self.com_box_stroke_cap_style.addItem("")
        self.com_box_stroke_cap_style.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.com_box_stroke_cap_style)
        self.ch_box_stroke_join_style = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_join_style.setEnabled(False)
        self.ch_box_stroke_join_style.setObjectName("ch_box_stroke_join_style")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_join_style)
        self.ch_box_stroke_cap_style = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_cap_style.setEnabled(False)
        self.ch_box_stroke_cap_style.setObjectName("ch_box_stroke_cap_style")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_cap_style)
        self.ch_box_stroke_z_value = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_z_value.setEnabled(False)
        self.ch_box_stroke_z_value.setObjectName("ch_box_stroke_z_value")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_z_value)
        self.dbl_sp_box_stroke_z_value = QtWidgets.QDoubleSpinBox(PdfEditorDialogSettingsPathItem)
        self.dbl_sp_box_stroke_z_value.setEnabled(False)
        self.dbl_sp_box_stroke_z_value.setObjectName("dbl_sp_box_stroke_z_value")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dbl_sp_box_stroke_z_value)
        self.dbl_sp_box_stroke_opacity = QtWidgets.QDoubleSpinBox(PdfEditorDialogSettingsPathItem)
        self.dbl_sp_box_stroke_opacity.setEnabled(False)
        self.dbl_sp_box_stroke_opacity.setObjectName("dbl_sp_box_stroke_opacity")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.dbl_sp_box_stroke_opacity)
        self.ch_box_stroke_opacity = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_opacity.setEnabled(False)
        self.ch_box_stroke_opacity.setObjectName("ch_box_stroke_opacity")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_opacity)
        self.ch_box_stroke_width_f = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_width_f.setEnabled(False)
        self.ch_box_stroke_width_f.setObjectName("ch_box_stroke_width_f")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_width_f)
        self.dbl_sp_box_stroke_width_f = QtWidgets.QDoubleSpinBox(PdfEditorDialogSettingsPathItem)
        self.dbl_sp_box_stroke_width_f.setEnabled(False)
        self.dbl_sp_box_stroke_width_f.setObjectName("dbl_sp_box_stroke_width_f")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.dbl_sp_box_stroke_width_f)
        self.ch_box_stroke_dash_pattern = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_dash_pattern.setEnabled(False)
        self.ch_box_stroke_dash_pattern.setObjectName("ch_box_stroke_dash_pattern")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_dash_pattern)
        self.l_ed_box_stroke_dash_pattern = QtWidgets.QLineEdit(PdfEditorDialogSettingsPathItem)
        self.l_ed_box_stroke_dash_pattern.setEnabled(False)
        self.l_ed_box_stroke_dash_pattern.setObjectName("l_ed_box_stroke_dash_pattern")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.l_ed_box_stroke_dash_pattern)
        self.ch_box_stroke_dash_offect = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_dash_offect.setEnabled(False)
        self.ch_box_stroke_dash_offect.setObjectName("ch_box_stroke_dash_offect")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_dash_offect)
        self.dbl_sp_box_stroke_dash_offect = QtWidgets.QDoubleSpinBox(PdfEditorDialogSettingsPathItem)
        self.dbl_sp_box_stroke_dash_offect.setEnabled(False)
        self.dbl_sp_box_stroke_dash_offect.setObjectName("dbl_sp_box_stroke_dash_offect")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dbl_sp_box_stroke_dash_offect)
        self.ch_box_stroke_close_path = QtWidgets.QRadioButton(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke_close_path.setEnabled(False)
        self.ch_box_stroke_close_path.setObjectName("ch_box_stroke_close_path")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.ch_box_stroke_close_path)
        self.groupBox_2 = QtWidgets.QGroupBox(PdfEditorDialogSettingsPathItem)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.r_btn_stroke_close_path_true = QtWidgets.QRadioButton(self.groupBox_2)
        self.r_btn_stroke_close_path_true.setEnabled(False)
        self.r_btn_stroke_close_path_true.setGeometry(QtCore.QRect(0, 0, 41, 20))
        self.r_btn_stroke_close_path_true.setObjectName("r_btn_stroke_close_path_true")
        self.r_btn_stroke_close_path_false = QtWidgets.QRadioButton(self.groupBox_2)
        self.r_btn_stroke_close_path_false.setEnabled(False)
        self.r_btn_stroke_close_path_false.setGeometry(QtCore.QRect(50, 0, 71, 20))
        self.r_btn_stroke_close_path_false.setObjectName("r_btn_stroke_close_path_false")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.ch_box_fill = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_fill.setObjectName("ch_box_fill")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ch_box_fill)
        self.ch_box_fill_color = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_fill_color.setEnabled(False)
        self.ch_box_fill_color.setObjectName("ch_box_fill_color")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ch_box_fill_color)
        self.btn_fill_color = QtWidgets.QPushButton(PdfEditorDialogSettingsPathItem)
        self.btn_fill_color.setEnabled(False)
        self.btn_fill_color.setObjectName("btn_fill_color")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_fill_color)
        self.ch_box_fill_style = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_fill_style.setEnabled(False)
        self.ch_box_fill_style.setObjectName("ch_box_fill_style")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ch_box_fill_style)
        self.com_box_fill_style = QtWidgets.QComboBox(PdfEditorDialogSettingsPathItem)
        self.com_box_fill_style.setEnabled(False)
        self.com_box_fill_style.setObjectName("com_box_fill_style")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.com_box_fill_style.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.com_box_fill_style)
        self.ch_box_fill_rule = QtWidgets.QCheckBox(PdfEditorDialogSettingsPathItem)
        self.ch_box_fill_rule.setEnabled(False)
        self.ch_box_fill_rule.setObjectName("ch_box_fill_rule")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.ch_box_fill_rule)
        self.groupBox = QtWidgets.QGroupBox(PdfEditorDialogSettingsPathItem)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.r_btn_fill_rule_true = QtWidgets.QRadioButton(self.groupBox)
        self.r_btn_fill_rule_true.setEnabled(False)
        self.r_btn_fill_rule_true.setGeometry(QtCore.QRect(0, 0, 41, 20))
        self.r_btn_fill_rule_true.setObjectName("r_btn_fill_rule_true")
        self.r_btn_fill_rule_false = QtWidgets.QRadioButton(self.groupBox)
        self.r_btn_fill_rule_false.setEnabled(False)
        self.r_btn_fill_rule_false.setGeometry(QtCore.QRect(50, 0, 71, 20))
        self.r_btn_fill_rule_false.setObjectName("r_btn_fill_rule_false")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_cancel = QtWidgets.QPushButton(PdfEditorDialogSettingsPathItem)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_back = QtWidgets.QPushButton(PdfEditorDialogSettingsPathItem)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout_2.addWidget(self.btn_back)
        self.btn_ok = QtWidgets.QPushButton(PdfEditorDialogSettingsPathItem)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_2.addWidget(self.btn_ok)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PdfEditorDialogSettingsPathItem)
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_color.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_style.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_join_style.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_cap_style.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_z_value.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_opacity.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_width_f.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_dash_pattern.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_dash_offect.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_close_path.setEnabled) # type: ignore
        self.ch_box_stroke_color.toggled['bool'].connect(self.btn_stroke_color.setEnabled) # type: ignore
        self.ch_box_stroke_style.toggled['bool'].connect(self.com_box_stroke_style.setEnabled) # type: ignore
        self.ch_box_stroke_join_style.toggled['bool'].connect(self.com_box_stroke_join_style.setEnabled) # type: ignore
        self.ch_box_stroke_cap_style.toggled['bool'].connect(self.com_box_stroke_cap_style.setEnabled) # type: ignore
        self.ch_box_stroke_z_value.toggled['bool'].connect(self.dbl_sp_box_stroke_z_value.setEnabled) # type: ignore
        self.ch_box_stroke_opacity.toggled['bool'].connect(self.dbl_sp_box_stroke_opacity.setEnabled) # type: ignore
        self.ch_box_stroke_width_f.toggled['bool'].connect(self.dbl_sp_box_stroke_width_f.setEnabled) # type: ignore
        self.ch_box_stroke_dash_pattern.toggled['bool'].connect(self.l_ed_box_stroke_dash_pattern.setEnabled) # type: ignore
        self.ch_box_stroke_dash_offect.toggled['bool'].connect(self.dbl_sp_box_stroke_dash_offect.setEnabled) # type: ignore
        self.ch_box_stroke_close_path.toggled['bool'].connect(self.r_btn_stroke_close_path_true.setEnabled) # type: ignore
        self.ch_box_stroke_close_path.toggled['bool'].connect(self.r_btn_stroke_close_path_false.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_color.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_style.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_join_style.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_cap_style.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_opacity.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_width_f.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_dash_pattern.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_dash_offect.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_close_path.setChecked) # type: ignore
        self.ch_box_fill_color.toggled['bool'].connect(self.btn_fill_color.setEnabled) # type: ignore
        self.ch_box_fill_style.toggled['bool'].connect(self.com_box_fill_style.setEnabled) # type: ignore
        self.ch_box_fill_rule.toggled['bool'].connect(self.r_btn_fill_rule_true.setEnabled) # type: ignore
        self.ch_box_fill_rule.toggled['bool'].connect(self.r_btn_fill_rule_false.setEnabled) # type: ignore
        self.ch_box_fill.toggled['bool'].connect(self.ch_box_fill_color.setEnabled) # type: ignore
        self.ch_box_fill.toggled['bool'].connect(self.ch_box_fill_color.setChecked) # type: ignore
        self.ch_box_fill.toggled['bool'].connect(self.ch_box_fill_style.setEnabled) # type: ignore
        self.ch_box_fill.toggled['bool'].connect(self.ch_box_fill_style.setChecked) # type: ignore
        self.ch_box_fill.toggled['bool'].connect(self.ch_box_fill_rule.setEnabled) # type: ignore
        self.ch_box_fill.toggled['bool'].connect(self.ch_box_fill_rule.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_width_f.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_width_f.setEnabled) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_style.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_style.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_z_value.setChecked) # type: ignore
        self.ch_box_stroke.toggled['bool'].connect(self.ch_box_stroke_z_value.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PdfEditorDialogSettingsPathItem)

    def retranslateUi(self, PdfEditorDialogSettingsPathItem):
        _translate = QtCore.QCoreApplication.translate
        PdfEditorDialogSettingsPathItem.setWindowTitle(_translate("PdfEditorDialogSettingsPathItem", "pdf editor dialog settings path item"))
        self.ch_box_stroke.setText(_translate("PdfEditorDialogSettingsPathItem", "stroke"))
        self.ch_box_stroke_color.setText(_translate("PdfEditorDialogSettingsPathItem", "color"))
        self.btn_stroke_color.setText(_translate("PdfEditorDialogSettingsPathItem", "color"))
        self.ch_box_stroke_style.setText(_translate("PdfEditorDialogSettingsPathItem", "style"))
        self.com_box_stroke_style.setItemText(0, _translate("PdfEditorDialogSettingsPathItem", "NoPen"))
        self.com_box_stroke_style.setItemText(1, _translate("PdfEditorDialogSettingsPathItem", "SolidLine"))
        self.com_box_stroke_style.setItemText(2, _translate("PdfEditorDialogSettingsPathItem", "DashLine"))
        self.com_box_stroke_style.setItemText(3, _translate("PdfEditorDialogSettingsPathItem", "DotLine"))
        self.com_box_stroke_style.setItemText(4, _translate("PdfEditorDialogSettingsPathItem", "DashDotLine"))
        self.com_box_stroke_style.setItemText(5, _translate("PdfEditorDialogSettingsPathItem", "DashDotDotLine"))
        self.com_box_stroke_style.setItemText(6, _translate("PdfEditorDialogSettingsPathItem", "CustomDashLine"))
        self.com_box_stroke_style.setItemText(7, _translate("PdfEditorDialogSettingsPathItem", "MPenStyle"))
        self.com_box_stroke_join_style.setItemText(0, _translate("PdfEditorDialogSettingsPathItem", "MiterJoin"))
        self.com_box_stroke_join_style.setItemText(1, _translate("PdfEditorDialogSettingsPathItem", "BevelJoin"))
        self.com_box_stroke_join_style.setItemText(2, _translate("PdfEditorDialogSettingsPathItem", "RoundJoin"))
        self.com_box_stroke_join_style.setItemText(3, _translate("PdfEditorDialogSettingsPathItem", "MPenJoinStyle"))
        self.com_box_stroke_join_style.setItemText(4, _translate("PdfEditorDialogSettingsPathItem", "SvgMiterJoin"))
        self.com_box_stroke_cap_style.setItemText(0, _translate("PdfEditorDialogSettingsPathItem", "FlatCap"))
        self.com_box_stroke_cap_style.setItemText(1, _translate("PdfEditorDialogSettingsPathItem", "SquareCap"))
        self.com_box_stroke_cap_style.setItemText(2, _translate("PdfEditorDialogSettingsPathItem", "RoundCap"))
        self.com_box_stroke_cap_style.setItemText(3, _translate("PdfEditorDialogSettingsPathItem", "MPenCapStyle"))
        self.ch_box_stroke_join_style.setText(_translate("PdfEditorDialogSettingsPathItem", "joinStyle"))
        self.ch_box_stroke_cap_style.setText(_translate("PdfEditorDialogSettingsPathItem", "CapStyle"))
        self.ch_box_stroke_z_value.setText(_translate("PdfEditorDialogSettingsPathItem", "ZValue"))
        self.ch_box_stroke_opacity.setText(_translate("PdfEditorDialogSettingsPathItem", "Opacity"))
        self.ch_box_stroke_width_f.setText(_translate("PdfEditorDialogSettingsPathItem", "WidthF"))
        self.ch_box_stroke_dash_pattern.setText(_translate("PdfEditorDialogSettingsPathItem", "DashPattern"))
        self.ch_box_stroke_dash_offect.setText(_translate("PdfEditorDialogSettingsPathItem", "DashOffset"))
        self.ch_box_stroke_close_path.setText(_translate("PdfEditorDialogSettingsPathItem", "close path"))
        self.r_btn_stroke_close_path_true.setText(_translate("PdfEditorDialogSettingsPathItem", "true"))
        self.r_btn_stroke_close_path_false.setText(_translate("PdfEditorDialogSettingsPathItem", "false"))
        self.ch_box_fill.setText(_translate("PdfEditorDialogSettingsPathItem", "fill"))
        self.ch_box_fill_color.setText(_translate("PdfEditorDialogSettingsPathItem", "color"))
        self.btn_fill_color.setText(_translate("PdfEditorDialogSettingsPathItem", "color"))
        self.ch_box_fill_style.setText(_translate("PdfEditorDialogSettingsPathItem", "style"))
        self.com_box_fill_style.setItemText(0, _translate("PdfEditorDialogSettingsPathItem", "NoBrush"))
        self.com_box_fill_style.setItemText(1, _translate("PdfEditorDialogSettingsPathItem", "SolidPattern"))
        self.com_box_fill_style.setItemText(2, _translate("PdfEditorDialogSettingsPathItem", "Dense1Pattern"))
        self.com_box_fill_style.setItemText(3, _translate("PdfEditorDialogSettingsPathItem", "Dense2Pattern"))
        self.com_box_fill_style.setItemText(4, _translate("PdfEditorDialogSettingsPathItem", "Dense3Pattern"))
        self.com_box_fill_style.setItemText(5, _translate("PdfEditorDialogSettingsPathItem", "Dense4Pattern"))
        self.com_box_fill_style.setItemText(6, _translate("PdfEditorDialogSettingsPathItem", "Dense5Pattern"))
        self.com_box_fill_style.setItemText(7, _translate("PdfEditorDialogSettingsPathItem", "Dense6Pattern"))
        self.com_box_fill_style.setItemText(8, _translate("PdfEditorDialogSettingsPathItem", "Dense7Pattern"))
        self.com_box_fill_style.setItemText(9, _translate("PdfEditorDialogSettingsPathItem", "HorPattern"))
        self.com_box_fill_style.setItemText(10, _translate("PdfEditorDialogSettingsPathItem", "VerPattern"))
        self.com_box_fill_style.setItemText(11, _translate("PdfEditorDialogSettingsPathItem", "CrossPattern"))
        self.com_box_fill_style.setItemText(12, _translate("PdfEditorDialogSettingsPathItem", "BDiagPattern"))
        self.com_box_fill_style.setItemText(13, _translate("PdfEditorDialogSettingsPathItem", "FDiagPattern"))
        self.com_box_fill_style.setItemText(14, _translate("PdfEditorDialogSettingsPathItem", "DiagCrossPattern"))
        self.com_box_fill_style.setItemText(15, _translate("PdfEditorDialogSettingsPathItem", "LinearGradientPattern"))
        self.com_box_fill_style.setItemText(16, _translate("PdfEditorDialogSettingsPathItem", "RadialGradientPattern"))
        self.com_box_fill_style.setItemText(17, _translate("PdfEditorDialogSettingsPathItem", "ConicalGradientPattern"))
        self.com_box_fill_style.setItemText(18, _translate("PdfEditorDialogSettingsPathItem", "TexturePattern"))
        self.ch_box_fill_rule.setText(_translate("PdfEditorDialogSettingsPathItem", "fill rule"))
        self.r_btn_fill_rule_true.setText(_translate("PdfEditorDialogSettingsPathItem", "true"))
        self.r_btn_fill_rule_false.setText(_translate("PdfEditorDialogSettingsPathItem", "false"))
        self.btn_cancel.setText(_translate("PdfEditorDialogSettingsPathItem", "cancel"))
        self.btn_back.setText(_translate("PdfEditorDialogSettingsPathItem", "back"))
        self.btn_ok.setText(_translate("PdfEditorDialogSettingsPathItem", "ok"))

class MyDialogSettingsPath(QtWidgets.QDialog, DialogSettingsPath):
    
    def __init__(self, root: QtWidgets, **kwargs):
        super().__init__(**kwargs)
        self.setupUi(self)
        self.root: QtWidgets = root

    def go_end(self):       
        self.hide()

