# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MasterBuku.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MasterBuku(object):
    def setupUi(self, MasterBuku):
        MasterBuku.setObjectName("MasterBuku")
        MasterBuku.resize(524, 462)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("book-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MasterBuku.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(MasterBuku)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 200, 501, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCreate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCreate.setStyleSheet("\n"
"QPushButton#btnCreate:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnCreate:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnCreate.setObjectName("btnCreate")
        self.horizontalLayout.addWidget(self.btnCreate)
        self.btnUpdate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnUpdate.setStyleSheet("\n"
"QPushButton#btnUpdate:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnUpdate:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout.addWidget(self.btnUpdate)
        self.btnDelete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnDelete.setStyleSheet("\n"
"QPushButton#btnDelete:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnDelete:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnClear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnClear.setStyleSheet("\n"
"QPushButton#btnClear:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnClear:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.btnRefresh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnRefresh.setStyleSheet("\n"
"QPushButton#btnRefresh:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnRefresh:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout.addWidget(self.btnRefresh)
        self.tblBuku = QtWidgets.QTableWidget(MasterBuku)
        self.tblBuku.setGeometry(QtCore.QRect(10, 250, 501, 192))
        self.tblBuku.setObjectName("tblBuku")
        self.tblBuku.setColumnCount(5)
        self.tblBuku.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuku.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuku.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuku.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblBuku.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tblBuku.setHorizontalHeaderItem(4, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(MasterBuku)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.edtKodeBuku = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtKodeBuku.setObjectName("edtKodeBuku")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edtKodeBuku)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.edtJudulBuku = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtJudulBuku.setObjectName("edtJudulBuku")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edtJudulBuku)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.edtPengarang = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtPengarang.setObjectName("edtPengarang")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edtPengarang)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.cboKategori = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cboKategori.setObjectName("cboKategori")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cboKategori)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spnJumlahBuku = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spnJumlahBuku.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnJumlahBuku.setMinimum(1)
        self.spnJumlahBuku.setMaximum(500)
        self.spnJumlahBuku.setObjectName("spnJumlahBuku")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spnJumlahBuku)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_8 = QtWidgets.QLabel(MasterBuku)
        self.label_8.setGeometry(QtCore.QRect(0, 5, 521, 451))
        self.label_8.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.horizontalLayoutWidget.raise_()
        self.tblBuku.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(MasterBuku)
        QtCore.QMetaObject.connectSlotsByName(MasterBuku)
        MasterBuku.setTabOrder(self.btnCreate, self.btnUpdate)
        MasterBuku.setTabOrder(self.btnUpdate, self.btnDelete)
        MasterBuku.setTabOrder(self.btnDelete, self.btnClear)
        MasterBuku.setTabOrder(self.btnClear, self.btnRefresh)
        MasterBuku.setTabOrder(self.btnRefresh, self.edtKodeBuku)
        MasterBuku.setTabOrder(self.edtKodeBuku, self.edtJudulBuku)
        MasterBuku.setTabOrder(self.edtJudulBuku, self.edtPengarang)
        MasterBuku.setTabOrder(self.edtPengarang, self.cboKategori)
        MasterBuku.setTabOrder(self.cboKategori, self.spnJumlahBuku)
        MasterBuku.setTabOrder(self.spnJumlahBuku, self.tblBuku)

    def retranslateUi(self, MasterBuku):
        _translate = QtCore.QCoreApplication.translate
        MasterBuku.setWindowTitle(_translate("MasterBuku", "Master Buku"))
        self.btnCreate.setToolTip(_translate("MasterBuku", "Tambah data buku"))
        self.btnCreate.setText(_translate("MasterBuku", "Create"))
        self.btnUpdate.setToolTip(_translate("MasterBuku", "Update data buku"))
        self.btnUpdate.setText(_translate("MasterBuku", "Update"))
        self.btnDelete.setToolTip(_translate("MasterBuku", "Hapus data buku"))
        self.btnDelete.setText(_translate("MasterBuku", "Delete"))
        self.btnClear.setToolTip(_translate("MasterBuku", "Clear input"))
        self.btnClear.setText(_translate("MasterBuku", "Clear"))
        self.btnRefresh.setToolTip(_translate("MasterBuku", "Refresh tabel buku"))
        self.btnRefresh.setText(_translate("MasterBuku", "Refresh"))
        item = self.tblBuku.horizontalHeaderItem(0)
        item.setText(_translate("MasterBuku", "Kode"))
        item = self.tblBuku.horizontalHeaderItem(1)
        item.setText(_translate("MasterBuku", "Judul"))
        item = self.tblBuku.horizontalHeaderItem(2)
        item.setText(_translate("MasterBuku", "Pengarang"))
        item = self.tblBuku.horizontalHeaderItem(3)
        item.setText(_translate("MasterBuku", "Kategori"))
        item = self.tblBuku.horizontalHeaderItem(4)
        item.setText(_translate("MasterBuku", "Jumlah"))
        self.label_6.setText(_translate("MasterBuku", "MASTER BUKU"))
        self.label.setText(_translate("MasterBuku", "Kode Buku*"))
        self.edtKodeBuku.setToolTip(_translate("MasterBuku", "Masukkan kode buku"))
        self.label_2.setText(_translate("MasterBuku", "Judul Buku*"))
        self.edtJudulBuku.setToolTip(_translate("MasterBuku", "Masukkan judul buku"))
        self.label_5.setText(_translate("MasterBuku", "Pengarang*"))
        self.edtPengarang.setToolTip(_translate("MasterBuku", "Masukkan nama pengarang"))
        self.label_4.setText(_translate("MasterBuku", "Kategori*"))
        self.cboKategori.setToolTip(_translate("MasterBuku", "Masukkan kategori buku"))
        self.label_3.setText(_translate("MasterBuku", "Jumlah Buku*"))
        self.spnJumlahBuku.setToolTip(_translate("MasterBuku", "Masukkan jumlah buku"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MasterBuku = QtWidgets.QDialog()
    ui = Ui_MasterBuku()
    ui.setupUi(MasterBuku)
    MasterBuku.show()
    sys.exit(app.exec_())
