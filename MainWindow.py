# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 520)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("main-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 391, 20))
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
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 311, 171))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("lms-main.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 391, 471))
        self.label_8.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 160, 242))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addWidget(self.btnRefresh)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.btnBuku = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnBuku.setStyleSheet("\n"
"QPushButton#btnBuku:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnBuku:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnBuku.setObjectName("btnBuku")
        self.verticalLayout.addWidget(self.btnBuku)
        self.btnPeminjam = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPeminjam.setStyleSheet("\n"
"QPushButton#btnPeminjam:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnPeminjam:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnPeminjam.setObjectName("btnPeminjam")
        self.verticalLayout.addWidget(self.btnPeminjam)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.btnPeminjaman = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPeminjaman.setStyleSheet("\n"
"QPushButton#btnPeminjaman:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnPeminjaman:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnPeminjaman.setObjectName("btnPeminjaman")
        self.verticalLayout.addWidget(self.btnPeminjaman)
        self.btnPengembalian = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPengembalian.setStyleSheet("\n"
"QPushButton#btnPengembalian:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnPengembalian:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnPengembalian.setObjectName("btnPengembalian")
        self.verticalLayout.addWidget(self.btnPengembalian)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.btnKonfigurasi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnKonfigurasi.setStyleSheet("\n"
"QPushButton#btnKonfigurasi:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#btnKonfigurasi:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.btnKonfigurasi.setObjectName("btnKonfigurasi")
        self.verticalLayout.addWidget(self.btnKonfigurasi)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 210, 160, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.edtTotalPeminjam = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edtTotalPeminjam.setFont(font)
        self.edtTotalPeminjam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edtTotalPeminjam.setReadOnly(True)
        self.edtTotalPeminjam.setObjectName("edtTotalPeminjam")
        self.verticalLayout_3.addWidget(self.edtTotalPeminjam)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.edtTotalBuku = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edtTotalBuku.setFont(font)
        self.edtTotalBuku.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edtTotalBuku.setReadOnly(True)
        self.edtTotalBuku.setObjectName("edtTotalBuku")
        self.verticalLayout_3.addWidget(self.edtTotalBuku)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.edtTotalBukuDipinjam = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edtTotalBukuDipinjam.setFont(font)
        self.edtTotalBukuDipinjam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edtTotalBukuDipinjam.setReadOnly(True)
        self.edtTotalBukuDipinjam.setObjectName("edtTotalBukuDipinjam")
        self.verticalLayout_3.addWidget(self.edtTotalBukuDipinjam)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.edtTotalBukuTersedia = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edtTotalBukuTersedia.setFont(font)
        self.edtTotalBukuTersedia.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edtTotalBukuTersedia.setReadOnly(True)
        self.edtTotalBukuTersedia.setObjectName("edtTotalBukuTersedia")
        self.verticalLayout_3.addWidget(self.edtTotalBukuTersedia)
        self.label_8.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMaster = QtWidgets.QMenu(self.menubar)
        self.menuMaster.setObjectName("menuMaster")
        self.menuTransaksi = QtWidgets.QMenu(self.menubar)
        self.menuTransaksi.setObjectName("menuTransaksi")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionBuku = QtWidgets.QAction(MainWindow)
        self.actionBuku.setObjectName("actionBuku")
        self.actionPeminjam = QtWidgets.QAction(MainWindow)
        self.actionPeminjam.setObjectName("actionPeminjam")
        self.actionPeminjaman = QtWidgets.QAction(MainWindow)
        self.actionPeminjaman.setObjectName("actionPeminjaman")
        self.actionPengembalian = QtWidgets.QAction(MainWindow)
        self.actionPengembalian.setObjectName("actionPengembalian")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionKonfigurasi = QtWidgets.QAction(MainWindow)
        self.actionKonfigurasi.setObjectName("actionKonfigurasi")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.menuFile.addAction(self.actionKonfigurasi)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuMaster.addAction(self.actionBuku)
        self.menuMaster.addAction(self.actionPeminjam)
        self.menuTransaksi.addAction(self.actionPeminjaman)
        self.menuTransaksi.addAction(self.actionPengembalian)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuMaster.menuAction())
        self.menubar.addAction(self.menuTransaksi.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Library Management System"))
        self.label_6.setText(_translate("MainWindow", "DASHBOARD"))
        self.btnRefresh.setToolTip(_translate("MainWindow", "Refresh Dashboard"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.label_9.setText(_translate("MainWindow", "Master"))
        self.btnBuku.setToolTip(_translate("MainWindow", "Buka form master buku"))
        self.btnBuku.setText(_translate("MainWindow", "Buku"))
        self.btnPeminjam.setToolTip(_translate("MainWindow", "Buka form master peminjam"))
        self.btnPeminjam.setText(_translate("MainWindow", "Peminjam"))
        self.label_10.setText(_translate("MainWindow", "Transaksi"))
        self.btnPeminjaman.setToolTip(_translate("MainWindow", "Buka form transaksi peminjaman"))
        self.btnPeminjaman.setText(_translate("MainWindow", "Peminjaman"))
        self.btnPengembalian.setToolTip(_translate("MainWindow", "Buka form transaksi pengembalian"))
        self.btnPengembalian.setText(_translate("MainWindow", "Pengembalian"))
        self.label_11.setText(_translate("MainWindow", "Konfigurasi"))
        self.btnKonfigurasi.setToolTip(_translate("MainWindow", "Buka form konfigurasi"))
        self.btnKonfigurasi.setText(_translate("MainWindow", "Konfigurasi"))
        self.label_2.setText(_translate("MainWindow", "Total Data Peminjam"))
        self.label_3.setText(_translate("MainWindow", "Total Buku"))
        self.label_4.setText(_translate("MainWindow", "Total Buku Dipinjam"))
        self.label_5.setText(_translate("MainWindow", "Total Buku Tersedia"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMaster.setTitle(_translate("MainWindow", "Master"))
        self.menuTransaksi.setTitle(_translate("MainWindow", "Transaksi"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionBuku.setText(_translate("MainWindow", "Buku"))
        self.actionPeminjam.setText(_translate("MainWindow", "Peminjam"))
        self.actionPeminjaman.setText(_translate("MainWindow", "Peminjaman"))
        self.actionPengembalian.setText(_translate("MainWindow", "Pengembalian"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionKonfigurasi.setText(_translate("MainWindow", "Konfigurasi"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
