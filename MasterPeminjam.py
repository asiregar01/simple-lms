# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MasterPeminjam.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MasterPeminjam(object):
    def setupUi(self, MasterPeminjam):
        MasterPeminjam.setObjectName("MasterPeminjam")
        MasterPeminjam.resize(525, 458)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("borrower-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MasterPeminjam.setWindowIcon(icon)
        self.tblPeminjam = QtWidgets.QTableWidget(MasterPeminjam)
        self.tblPeminjam.setGeometry(QtCore.QRect(10, 269, 501, 171))
        self.tblPeminjam.setAlternatingRowColors(True)
        self.tblPeminjam.setColumnCount(5)
        self.tblPeminjam.setObjectName("tblPeminjam")
        self.tblPeminjam.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjam.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjam.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjam.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjam.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblPeminjam.setHorizontalHeaderItem(4, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(MasterPeminjam)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 255))
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
        self.edtKodePeminjam = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtKodePeminjam.setObjectName("edtKodePeminjam")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edtKodePeminjam)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.edtNoIdentitas = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtNoIdentitas.setObjectName("edtNoIdentitas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.edtNoIdentitas)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.edtNamaDepan = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtNamaDepan.setObjectName("edtNamaDepan")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edtNamaDepan)
        self.edtNamaBelakang = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edtNamaBelakang.setObjectName("edtNamaBelakang")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edtNamaBelakang)
        self.txtAlamat = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txtAlamat.setObjectName("txtAlamat")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtAlamat)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCreate = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.btnUpdate = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.btnDelete = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.btnRefresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_8 = QtWidgets.QLabel(MasterPeminjam)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.label_8.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.raise_()
        self.tblPeminjam.raise_()
        self.verticalLayoutWidget.raise_()

        self.retranslateUi(MasterPeminjam)
        QtCore.QMetaObject.connectSlotsByName(MasterPeminjam)
        MasterPeminjam.setTabOrder(self.btnCreate, self.btnUpdate)
        MasterPeminjam.setTabOrder(self.btnUpdate, self.btnDelete)
        MasterPeminjam.setTabOrder(self.btnDelete, self.btnClear)
        MasterPeminjam.setTabOrder(self.btnClear, self.btnRefresh)
        MasterPeminjam.setTabOrder(self.btnRefresh, self.edtKodePeminjam)
        MasterPeminjam.setTabOrder(self.edtKodePeminjam, self.edtNoIdentitas)
        MasterPeminjam.setTabOrder(self.edtNoIdentitas, self.edtNamaDepan)
        MasterPeminjam.setTabOrder(self.edtNamaDepan, self.edtNamaBelakang)
        MasterPeminjam.setTabOrder(self.edtNamaBelakang, self.txtAlamat)
        MasterPeminjam.setTabOrder(self.txtAlamat, self.tblPeminjam)

    def retranslateUi(self, MasterPeminjam):
        _translate = QtCore.QCoreApplication.translate
        MasterPeminjam.setWindowTitle(_translate("MasterPeminjam", "Master Peminjam"))
        self.tblPeminjam.setToolTip(_translate("MasterPeminjam", "Tabel master peminjam"))
        item = self.tblPeminjam.horizontalHeaderItem(0)
        item.setText(_translate("MasterPeminjam", "Kode"))
        item = self.tblPeminjam.horizontalHeaderItem(1)
        item.setText(_translate("MasterPeminjam", "No Identitas"))
        item = self.tblPeminjam.horizontalHeaderItem(2)
        item.setText(_translate("MasterPeminjam", "Nama Depan"))
        item = self.tblPeminjam.horizontalHeaderItem(3)
        item.setText(_translate("MasterPeminjam", "Nama Belakang"))
        item = self.tblPeminjam.horizontalHeaderItem(4)
        item.setText(_translate("MasterPeminjam", "Alamat"))
        self.label_6.setText(_translate("MasterPeminjam", "MASTER PEMINJAM"))
        self.label.setText(_translate("MasterPeminjam", "Kode Peminjam*"))
        self.edtKodePeminjam.setToolTip(_translate("MasterPeminjam", "Masukkan kode peminjam"))
        self.label_2.setText(_translate("MasterPeminjam", "No. Identitas*"))
        self.edtNoIdentitas.setToolTip(_translate("MasterPeminjam", "Masukkan nomor identitas"))
        self.label_4.setText(_translate("MasterPeminjam", "Nama Belakang"))
        self.label_3.setText(_translate("MasterPeminjam", "Alamat"))
        self.label_5.setText(_translate("MasterPeminjam", "Nama Depan*"))
        self.edtNamaDepan.setToolTip(_translate("MasterPeminjam", "Masukkan nama depan"))
        self.edtNamaBelakang.setToolTip(_translate("MasterPeminjam", "Masukkan nama belakang"))
        self.txtAlamat.setToolTip(_translate("MasterPeminjam", "Masukkan alamat"))
        self.btnCreate.setToolTip(_translate("MasterPeminjam", "Tambah data peminjam"))
        self.btnCreate.setText(_translate("MasterPeminjam", "Create"))
        self.btnUpdate.setToolTip(_translate("MasterPeminjam", "Update data peminjam"))
        self.btnUpdate.setText(_translate("MasterPeminjam", "Update"))
        self.btnDelete.setToolTip(_translate("MasterPeminjam", "Hapus data peminjam"))
        self.btnDelete.setText(_translate("MasterPeminjam", "Delete"))
        self.btnClear.setToolTip(_translate("MasterPeminjam", "Clear input"))
        self.btnClear.setText(_translate("MasterPeminjam", "Clear"))
        self.btnRefresh.setToolTip(_translate("MasterPeminjam", "Refresh tabel peminjam"))
        self.btnRefresh.setText(_translate("MasterPeminjam", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MasterPeminjam = QtWidgets.QDialog()
    ui = Ui_MasterPeminjam()
    ui.setupUi(MasterPeminjam)
    MasterPeminjam.show()
    sys.exit(app.exec_())
