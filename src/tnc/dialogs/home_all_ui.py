# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/turboss/Projects/tnc/tnc/dialogs/home_all.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 247)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.statuslabel = StatusLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statuslabel.sizePolicy().hasHeightForWidth())
        self.statuslabel.setSizePolicy(sizePolicy)
        self.statuslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statuslabel.setObjectName("statuslabel")
        self.verticalLayout_2.addWidget(self.statuslabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, 0, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.close_button = QtWidgets.QPushButton(Dialog)
        self.close_button.setMaximumSize(QtCore.QSize(72, 64))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.homeall_abutton = ActionButton(Dialog)
        self.homeall_abutton.setEnabled(True)
        self.homeall_abutton.setMaximumSize(QtCore.QSize(72, 64))
        self.homeall_abutton.setObjectName("homeall_abutton")
        self.horizontalLayout_2.addWidget(self.homeall_abutton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Frame"))
        self.statuslabel.setText(_translate("Dialog", "Do you want to reference the machine?"))
        self.statuslabel.setProperty("rules", _translate("Dialog", "[]"))
        self.close_button.setText(_translate("Dialog", "CLOSE"))
        self.homeall_abutton.setText(_translate("Dialog", "OK"))
        self.homeall_abutton.setProperty("rules", _translate("Dialog", "[]"))
        self.homeall_abutton.setProperty("actionName", _translate("Dialog", "machine.home.all"))
from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel