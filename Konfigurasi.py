# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Konfigurasi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Konfigurasi(object):
    def setupUi(self, Konfigurasi):
        Konfigurasi.setObjectName("Konfigurasi")
        Konfigurasi.resize(293, 158)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("config-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Konfigurasi.setWindowIcon(icon)
        self.btnUpdate = QtWidgets.QPushButton(Konfigurasi)
        self.btnUpdate.setGeometry(QtCore.QRect(200, 111, 75, 31))
        self.btnUpdate.setStyleSheet("QPushButton#btnUpdate:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnUpdate:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnUpdate.setObjectName("btnUpdate")
        self.label_5 = QtWidgets.QLabel(Konfigurasi)
        self.label_5.setGeometry(QtCore.QRect(0, 1, 290, 151))
        self.label_5.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(Konfigurasi)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 21, 271, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.edtMaksPinjam = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtMaksPinjam.setStyleSheet("")
        self.edtMaksPinjam.setText("")
        self.edtMaksPinjam.setMaxLength(3)
        self.edtMaksPinjam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edtMaksPinjam.setObjectName("edtMaksPinjam")
        self.gridLayout.addWidget(self.edtMaksPinjam, 0, 1, 1, 1)
        self.edtLamaPinjam = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edtLamaPinjam.setMaxLength(3)
        self.edtLamaPinjam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edtLamaPinjam.setObjectName("edtLamaPinjam")
        self.gridLayout.addWidget(self.edtLamaPinjam, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_5.raise_()
        self.btnUpdate.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(Konfigurasi)
        QtCore.QMetaObject.connectSlotsByName(Konfigurasi)

    def retranslateUi(self, Konfigurasi):
        _translate = QtCore.QCoreApplication.translate
        Konfigurasi.setWindowTitle(_translate("Konfigurasi", "Konfigurasi"))
        self.btnUpdate.setToolTip(_translate("Konfigurasi", "Update konfigurasi"))
        self.btnUpdate.setText(_translate("Konfigurasi", "Update"))
        self.edtMaksPinjam.setToolTip(_translate("Konfigurasi", "Jumlah maksimal buku yang bisa dipinjam"))
        self.edtMaksPinjam.setInputMask(_translate("Konfigurasi", "000"))
        self.edtLamaPinjam.setToolTip(_translate("Konfigurasi", "Lama peminjaman dalam hari"))
        self.edtLamaPinjam.setInputMask(_translate("Konfigurasi", "000"))
        self.label.setText(_translate("Konfigurasi", "Maks Pinjam"))
        self.label_3.setText(_translate("Konfigurasi", "Lama Pinjam"))
        self.label_2.setText(_translate("Konfigurasi", "Buku"))
        self.label_4.setText(_translate("Konfigurasi", "Hari"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Konfigurasi = QtWidgets.QDialog()
    ui = Ui_Konfigurasi()
    ui.setupUi(Konfigurasi)
    Konfigurasi.show()
    sys.exit(app.exec_())
