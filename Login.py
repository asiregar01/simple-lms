# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 341)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("user-icon.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 290, 251, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        self.btnLogin.setStyleSheet("\n"
"QPushButton#btnLogin:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnLogin:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnExit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy)
        self.btnExit.setStyleSheet("\n"
"QPushButton#btnExit:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnExit:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout.addWidget(self.btnExit)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 290, 341))
        self.label_5.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 140, 251, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("color:rgba(255, 255, 255, 150);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edtPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtPassword.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.edtPassword.setText("")
        self.edtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtPassword.setObjectName("edtPassword")
        self.gridLayout.addWidget(self.edtPassword, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color:rgba(255, 255, 255, 150);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.edtUsername = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtUsername.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px")
        self.edtUsername.setText("")
        self.edtUsername.setObjectName("edtUsername")
        self.gridLayout.addWidget(self.edtUsername, 1, 0, 1, 1)
        self.chkShowPassword = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.chkShowPassword.setStyleSheet("color:rgba(255, 255, 255, 150);")
        self.chkShowPassword.setObjectName("chkShowPassword")
        self.gridLayout.addWidget(self.chkShowPassword, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 101, 100))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        font.setPointSize(70)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(255, 255, 255, 150);")
        self.label_3.setObjectName("label_3")
        self.label_5.raise_()
        self.horizontalLayoutWidget.raise_()
        self.gridLayoutWidget.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simple LMS - Login"))
        self.btnLogin.setToolTip(_translate("Dialog", "Login ke system"))
        self.btnLogin.setText(_translate("Dialog", "Log In"))
        self.btnExit.setToolTip(_translate("Dialog", "Keluar dari system"))
        self.btnExit.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Username"))
        self.edtPassword.setToolTip(_translate("Dialog", "Masukkan password"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.edtUsername.setToolTip(_translate("Dialog", "Masukkan username"))
        self.chkShowPassword.setToolTip(_translate("Dialog", "Show / hide password"))
        self.chkShowPassword.setText(_translate("Dialog", "Show Password"))
        self.label_3.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
