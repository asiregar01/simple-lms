# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindBuku.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FindBuku(object):
    def setupUi(self, FindBuku):
        FindBuku.setObjectName("FindBuku")
        FindBuku.resize(297, 250)
        self.btnSelect = QtWidgets.QPushButton(FindBuku)
        self.btnSelect.setGeometry(QtCore.QRect(204, 210, 75, 23))
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
        self.tblData = QtWidgets.QTableWidget(FindBuku)
        self.tblData.setGeometry(QtCore.QRect(10, 10, 271, 192))
        self.tblData.setAlternatingRowColors(True)
        self.tblData.setObjectName("tblData")
        self.tblData.setColumnCount(2)
        self.tblData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblData.setHorizontalHeaderItem(1, item)
        self.label_5 = QtWidgets.QLabel(FindBuku)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 290, 241))
        self.label_5.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.btnSelect.raise_()
        self.tblData.raise_()

        self.retranslateUi(FindBuku)
        QtCore.QMetaObject.connectSlotsByName(FindBuku)
        FindBuku.setTabOrder(self.tblData, self.btnSelect)

    def retranslateUi(self, FindBuku):
        _translate = QtCore.QCoreApplication.translate
        FindBuku.setWindowTitle(_translate("FindBuku", "Cari Buku"))
        self.btnSelect.setText(_translate("FindBuku", "Select"))
        item = self.tblData.horizontalHeaderItem(0)
        item.setText(_translate("FindBuku", "Kode"))
        item = self.tblData.horizontalHeaderItem(1)
        item.setText(_translate("FindBuku", "Judul"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindBuku = QtWidgets.QDialog()
    ui = Ui_FindBuku()
    ui.setupUi(FindBuku)
    FindBuku.show()
    sys.exit(app.exec_())
