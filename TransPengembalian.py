# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TransPengembalian.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransPengembalian(object):
    def setupUi(self, TransPengembalian):
        TransPengembalian.setObjectName("TransPengembalian")
        TransPengembalian.resize(525, 458)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("return-book-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TransPengembalian.setWindowIcon(icon)
        self.tblPengembalian = QtWidgets.QTableWidget(TransPengembalian)
        self.tblPengembalian.setEnabled(True)
        self.tblPengembalian.setGeometry(QtCore.QRect(10, 280, 501, 160))
        self.tblPengembalian.setAlternatingRowColors(True)
        self.tblPengembalian.setColumnCount(6)
        self.tblPengembalian.setObjectName("tblPengembalian")
        self.tblPengembalian.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblPengembalian.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPengembalian.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPengembalian.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPengembalian.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPengembalian.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPengembalian.setHorizontalHeaderItem(5, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(TransPengembalian)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 230, 501, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        self.label_8 = QtWidgets.QLabel(TransPengembalian)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.label_8.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(TransPengembalian)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 214))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.edtKodeTrans = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtKodeTrans.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edtKodeTrans.setReadOnly(True)
        self.edtKodeTrans.setObjectName("edtKodeTrans")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edtKodeTrans)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dteTglTrans = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dteTglTrans.setAlignment(QtCore.Qt.AlignCenter)
        self.dteTglTrans.setReadOnly(True)
        self.dteTglTrans.setObjectName("dteTglTrans")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dteTglTrans)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edtKodePeminjam = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtKodePeminjam.setReadOnly(True)
        self.edtKodePeminjam.setObjectName("edtKodePeminjam")
        self.horizontalLayout_2.addWidget(self.edtKodePeminjam)
        self.btnCariPeminjam = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCariPeminjam.setStyleSheet("\n"
"QPushButton#btnCariPeminjam:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnCariPeminjam:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnCariPeminjam.setObjectName("btnCariPeminjam")
        self.horizontalLayout_2.addWidget(self.btnCariPeminjam)
        self.edtNamaPeminjam = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtNamaPeminjam.setReadOnly(True)
        self.edtNamaPeminjam.setObjectName("edtNamaPeminjam")
        self.horizontalLayout_2.addWidget(self.edtNamaPeminjam)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edtKodeBuku = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtKodeBuku.setReadOnly(True)
        self.edtKodeBuku.setObjectName("edtKodeBuku")
        self.horizontalLayout_3.addWidget(self.edtKodeBuku)
        self.btnCariBuku = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCariBuku.setStyleSheet("\n"
"QPushButton#btnCariBuku:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnCariBuku:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnCariBuku.setObjectName("btnCariBuku")
        self.horizontalLayout_3.addWidget(self.btnCariBuku)
        self.edtJudulBuku = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtJudulBuku.setReadOnly(True)
        self.edtJudulBuku.setObjectName("edtJudulBuku")
        self.horizontalLayout_3.addWidget(self.edtJudulBuku)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.dteTglHrsKembali = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dteTglHrsKembali.setAlignment(QtCore.Qt.AlignCenter)
        self.dteTglHrsKembali.setReadOnly(True)
        self.dteTglHrsKembali.setObjectName("dteTglHrsKembali")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dteTglHrsKembali)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.dteTglKembali = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dteTglKembali.setAlignment(QtCore.Qt.AlignCenter)
        self.dteTglKembali.setObjectName("dteTglKembali")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dteTglKembali)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_8.raise_()
        self.tblPengembalian.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(TransPengembalian)
        QtCore.QMetaObject.connectSlotsByName(TransPengembalian)
        TransPengembalian.setTabOrder(self.btnUpdate, self.btnDelete)
        TransPengembalian.setTabOrder(self.btnDelete, self.btnClear)
        TransPengembalian.setTabOrder(self.btnClear, self.btnRefresh)
        TransPengembalian.setTabOrder(self.btnRefresh, self.dteTglTrans)
        TransPengembalian.setTabOrder(self.dteTglTrans, self.edtKodeTrans)
        TransPengembalian.setTabOrder(self.edtKodeTrans, self.edtKodePeminjam)
        TransPengembalian.setTabOrder(self.edtKodePeminjam, self.edtNamaPeminjam)
        TransPengembalian.setTabOrder(self.edtNamaPeminjam, self.edtKodeBuku)
        TransPengembalian.setTabOrder(self.edtKodeBuku, self.edtJudulBuku)
        TransPengembalian.setTabOrder(self.edtJudulBuku, self.dteTglHrsKembali)
        TransPengembalian.setTabOrder(self.dteTglHrsKembali, self.dteTglKembali)
        TransPengembalian.setTabOrder(self.dteTglKembali, self.tblPengembalian)

    def retranslateUi(self, TransPengembalian):
        _translate = QtCore.QCoreApplication.translate
        TransPengembalian.setWindowTitle(_translate("TransPengembalian", "Transaksi Pengembalian"))
        self.tblPengembalian.setToolTip(_translate("TransPengembalian", "Tabel Pengembalian"))
        item = self.tblPengembalian.horizontalHeaderItem(0)
        item.setText(_translate("TransPengembalian", "Kode Trans"))
        item = self.tblPengembalian.horizontalHeaderItem(1)
        item.setText(_translate("TransPengembalian", "Tanggal Pinjam"))
        item = self.tblPengembalian.horizontalHeaderItem(2)
        item.setText(_translate("TransPengembalian", "Kode Peminjam"))
        item = self.tblPengembalian.horizontalHeaderItem(3)
        item.setText(_translate("TransPengembalian", "Kode Buku"))
        item = self.tblPengembalian.horizontalHeaderItem(4)
        item.setText(_translate("TransPengembalian", "Tgl Hrs Kembali"))
        item = self.tblPengembalian.horizontalHeaderItem(5)
        item.setText(_translate("TransPengembalian", "Tanggal Kembali"))
        self.btnUpdate.setToolTip(_translate("TransPengembalian", "Update transaksi pengembalian"))
        self.btnUpdate.setText(_translate("TransPengembalian", "Update"))
        self.btnDelete.setToolTip(_translate("TransPengembalian", "Hapus transaksi pengembalian"))
        self.btnDelete.setText(_translate("TransPengembalian", "Delete"))
        self.btnClear.setToolTip(_translate("TransPengembalian", "Clear input"))
        self.btnClear.setText(_translate("TransPengembalian", "Clear"))
        self.btnRefresh.setToolTip(_translate("TransPengembalian", "Refresh tabel pengembalian"))
        self.btnRefresh.setText(_translate("TransPengembalian", "Refresh"))
        self.label_7.setText(_translate("TransPengembalian", "TRANSAKSI PENGEMBALIAN"))
        self.label.setText(_translate("TransPengembalian", "Kode Transaksi"))
        self.edtKodeTrans.setToolTip(_translate("TransPengembalian", "Kode transaksi"))
        self.label_2.setText(_translate("TransPengembalian", "Tanggal Pinjam*"))
        self.dteTglTrans.setToolTip(_translate("TransPengembalian", "Tanggal peminjaman"))
        self.dteTglTrans.setDisplayFormat(_translate("TransPengembalian", "dd/MM/yyyy"))
        self.label_5.setText(_translate("TransPengembalian", "Kode Peminjam*"))
        self.edtKodePeminjam.setToolTip(_translate("TransPengembalian", "Kode peminjam"))
        self.btnCariPeminjam.setText(_translate("TransPengembalian", "Find"))
        self.edtNamaPeminjam.setToolTip(_translate("TransPengembalian", "Nama peminjam"))
        self.label_4.setText(_translate("TransPengembalian", "Kode Buku*"))
        self.edtKodeBuku.setToolTip(_translate("TransPengembalian", "Kode buku"))
        self.btnCariBuku.setText(_translate("TransPengembalian", "Find"))
        self.edtJudulBuku.setToolTip(_translate("TransPengembalian", "Judul buku"))
        self.label_3.setText(_translate("TransPengembalian", "Tanggal Harus Kembali*"))
        self.dteTglHrsKembali.setToolTip(_translate("TransPengembalian", "Tanggal harus kembali [bulan/tanggal/tahun]"))
        self.dteTglHrsKembali.setDisplayFormat(_translate("TransPengembalian", "dd/MM/yyyy"))
        self.label_6.setText(_translate("TransPengembalian", "Tanggal Kembali*"))
        self.dteTglKembali.setToolTip(_translate("TransPengembalian", "Masukkan tanggal pengembalian [bulan/tanggal/tahun]"))
        self.dteTglKembali.setDisplayFormat(_translate("TransPengembalian", "dd/MM/yyyy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TransPengembalian = QtWidgets.QDialog()
    ui = Ui_TransPengembalian()
    ui.setupUi(TransPengembalian)
    TransPengembalian.show()
    sys.exit(app.exec_())
