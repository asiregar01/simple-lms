# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindPeminjam.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindPeminjam(object):
    def setupUi(self, FindPeminjam):
        FindPeminjam.setObjectName("FindPeminjam")
        FindPeminjam.resize(295, 246)
        self.tblData = QtWidgets.QTableWidget(FindPeminjam)
        self.tblData.setGeometry(QtCore.QRect(10, 10, 271, 192))
        self.tblData.setAlternatingRowColors(True)
        self.tblData.setObjectName("tblData")
        self.tblData.setColumnCount(2)
        self.tblData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblData.setHorizontalHeaderItem(1, item)
        self.btnSelect = QtWidgets.QPushButton(FindPeminjam)
        self.btnSelect.setGeometry(QtCore.QRect(206, 210, 75, 23))
        self.btnSelect.setStyleSheet("QPushButton#btnSelect:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnSelect:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnSelect.setDefault(True)
        self.btnSelect.setObjectName("btnSelect")
        self.label_5 = QtWidgets.QLabel(FindPeminjam)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 290, 241))
        self.label_5.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.tblData.raise_()
        self.btnSelect.raise_()

        self.retranslateUi(FindPeminjam)
        QtCore.QMetaObject.connectSlotsByName(FindPeminjam)

    def retranslateUi(self, FindPeminjam):
        _translate = QtCore.QCoreApplication.translate
        FindPeminjam.setWindowTitle(_translate("FindPeminjam", "Cari Peminjam"))
        item = self.tblData.horizontalHeaderItem(0)
        item.setText(_translate("FindPeminjam", "Kode"))
        item = self.tblData.horizontalHeaderItem(1)
        item.setText(_translate("FindPeminjam", "Nama"))
        self.btnSelect.setText(_translate("FindPeminjam", "Select"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindPeminjam = QtWidgets.QDialog()
    ui = Ui_FindPeminjam()
    ui.setupUi(FindPeminjam)
    FindPeminjam.show()
    sys.exit(app.exec_())
