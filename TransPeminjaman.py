# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TransPeminjaman.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TransPeminjaman(object):
    def setupUi(self, TransPeminjaman):
        TransPeminjaman.setObjectName("TransPeminjaman")
        TransPeminjaman.resize(523, 458)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("borrow-book-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TransPeminjaman.setWindowIcon(icon)
        self.tblPeminjaman = QtWidgets.QTableWidget(TransPeminjaman)
        self.tblPeminjaman.setEnabled(True)
        self.tblPeminjaman.setGeometry(QtCore.QRect(10, 260, 501, 171))
        self.tblPeminjaman.setAlternatingRowColors(True)
        self.tblPeminjaman.setColumnCount(5)
        self.tblPeminjaman.setObjectName("tblPeminjaman")
        self.tblPeminjaman.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjaman.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjaman.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjaman.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjaman.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjaman.setHorizontalHeaderItem(4, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(TransPeminjaman)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 501, 41))
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
        self.label_8 = QtWidgets.QLabel(TransPeminjaman)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.label_8.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(TransPeminjaman)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 501, 183))
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
        self.verticalLayout.addLayout(self.formLayout)
        self.label_8.raise_()
        self.tblPeminjaman.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(TransPeminjaman)
        QtCore.QMetaObject.connectSlotsByName(TransPeminjaman)
        TransPeminjaman.setTabOrder(self.edtKodeTrans, self.dteTglTrans)
        TransPeminjaman.setTabOrder(self.dteTglTrans, self.edtKodePeminjam)
        TransPeminjaman.setTabOrder(self.edtKodePeminjam, self.btnCariPeminjam)
        TransPeminjaman.setTabOrder(self.btnCariPeminjam, self.edtNamaPeminjam)
        TransPeminjaman.setTabOrder(self.edtNamaPeminjam, self.edtKodeBuku)
        TransPeminjaman.setTabOrder(self.edtKodeBuku, self.btnCariBuku)
        TransPeminjaman.setTabOrder(self.btnCariBuku, self.edtJudulBuku)
        TransPeminjaman.setTabOrder(self.edtJudulBuku, self.dteTglHrsKembali)
        TransPeminjaman.setTabOrder(self.dteTglHrsKembali, self.btnCreate)
        TransPeminjaman.setTabOrder(self.btnCreate, self.btnUpdate)
        TransPeminjaman.setTabOrder(self.btnUpdate, self.btnDelete)
        TransPeminjaman.setTabOrder(self.btnDelete, self.btnClear)
        TransPeminjaman.setTabOrder(self.btnClear, self.btnRefresh)
        TransPeminjaman.setTabOrder(self.btnRefresh, self.tblPeminjaman)

    def retranslateUi(self, TransPeminjaman):
        _translate = QtCore.QCoreApplication.translate
        TransPeminjaman.setWindowTitle(_translate("TransPeminjaman", "Transaksi Peminjaman"))
        self.tblPeminjaman.setToolTip(_translate("TransPeminjaman", "Tabel peminjaman"))
        item = self.tblPeminjaman.horizontalHeaderItem(0)
        item.setText(_translate("TransPeminjaman", "Kode Trans"))
        item = self.tblPeminjaman.horizontalHeaderItem(1)
        item.setText(_translate("TransPeminjaman", "Tanggal Pinjam"))
        item = self.tblPeminjaman.horizontalHeaderItem(2)
        item.setText(_translate("TransPeminjaman", "Kode Peminjam"))
        item = self.tblPeminjaman.horizontalHeaderItem(3)
        item.setText(_translate("TransPeminjaman", "Kode Buku"))
        item = self.tblPeminjaman.horizontalHeaderItem(4)
        item.setText(_translate("TransPeminjaman", "Tgl Hrs Kembali"))
        self.btnCreate.setToolTip(_translate("TransPeminjaman", "Tambah transaksi peminjaman"))
        self.btnCreate.setText(_translate("TransPeminjaman", "Create"))
        self.btnUpdate.setToolTip(_translate("TransPeminjaman", "Update transaksi peminjaman"))
        self.btnUpdate.setText(_translate("TransPeminjaman", "Update"))
        self.btnDelete.setToolTip(_translate("TransPeminjaman", "Hapus transaksi peminjaman"))
        self.btnDelete.setText(_translate("TransPeminjaman", "Delete"))
        self.btnClear.setToolTip(_translate("TransPeminjaman", "Clear input"))
        self.btnClear.setText(_translate("TransPeminjaman", "Clear"))
        self.btnRefresh.setToolTip(_translate("TransPeminjaman", "Refresh tabel peminjaman"))
        self.btnRefresh.setText(_translate("TransPeminjaman", "Refresh"))
        self.label_6.setText(_translate("TransPeminjaman", "TRANSAKSI PEMINJAMAN"))
        self.label.setText(_translate("TransPeminjaman", "Kode Transaksi"))
        self.edtKodeTrans.setToolTip(_translate("TransPeminjaman", "Kode transaksi peminjaman"))
        self.label_2.setText(_translate("TransPeminjaman", "Tanggal Transaksi*"))
        self.dteTglTrans.setToolTip(_translate("TransPeminjaman", "Masukkan tanggal peminjaman [bulan/tanggal/tahun]"))
        self.dteTglTrans.setDisplayFormat(_translate("TransPeminjaman", "dd/MM/yyyy"))
        self.label_5.setText(_translate("TransPeminjaman", "Kode Peminjam*"))
        self.edtKodePeminjam.setToolTip(_translate("TransPeminjaman", "Masukkan kode peminjam"))
        self.btnCariPeminjam.setText(_translate("TransPeminjaman", "Find"))
        self.edtNamaPeminjam.setToolTip(_translate("TransPeminjaman", "Nama peminjam"))
        self.label_4.setText(_translate("TransPeminjaman", "Kode Buku*"))
        self.edtKodeBuku.setToolTip(_translate("TransPeminjaman", "Masukkan kode buku"))
        self.btnCariBuku.setText(_translate("TransPeminjaman", "Find"))
        self.edtJudulBuku.setToolTip(_translate("TransPeminjaman", "Judul buku"))
        self.label_3.setText(_translate("TransPeminjaman", "Tanggal Harus Kembali*"))
        self.dteTglHrsKembali.setToolTip(_translate("TransPeminjaman", "Tanggal harus kembali [bulan/tanggal/tahun]"))
        self.dteTglHrsKembali.setDisplayFormat(_translate("TransPeminjaman", "dd/MM/yyyy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TransPeminjaman = QtWidgets.QDialog()
    ui = Ui_TransPeminjaman()
    ui.setupUi(TransPeminjaman)
    TransPeminjaman.show()
    sys.exit(app.exec_())
