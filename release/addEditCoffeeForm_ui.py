# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 204))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.layout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.layout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setVerticalSpacing(7)
        self.layout.setObjectName("layout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_input.setObjectName("name_input")
        self.layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_input)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.roast_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.roast_input.setObjectName("roast_input")
        self.layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roast_input)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.grind_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.grind_input.setObjectName("grind_input")
        self.layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.grind_input)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.taste_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.taste_input.setObjectName("taste_input")
        self.layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.taste_input)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.price_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price_input.setObjectName("price_input")
        self.layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.price_input)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.volume_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.volume_input.setObjectName("volume_input")
        self.layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.volume_input)
        self.save_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.save_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название"))
        self.label_2.setText(_translate("Dialog", "Степень обжарки"))
        self.label_3.setText(_translate("Dialog", "Молотый/в зёрнах"))
        self.label_4.setText(_translate("Dialog", "Вкус"))
        self.label_5.setText(_translate("Dialog", "Цена"))
        self.label_6.setText(_translate("Dialog", "Объём упаковки"))
        self.save_button.setText(_translate("Dialog", "Save"))