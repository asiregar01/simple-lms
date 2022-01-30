import sys
from datetime import datetime
from datetime import timedelta
from Login import *
from Konfigurasi import *
from MainWindow import *
from MasterBuku import *
from MasterPeminjam import *
from TransPeminjaman import *
from TransPengembalian import *
from FindPeminjam import *
from FindBuku import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MySQLdb as mdb
#import mysql.connector

#Variable Global Buat Form
main_window = None
master_buku = None
MasterBuku = None
MasterPeminjam = None
TransPeminjaman = None
TransPengembalian = None
Konfigurasi = None
FindPeminjam = None
FindBuku = None
uib = None
uip = None
ui_tpm = None
ui_tpk = None
uik = None
ui_fp = None
ui_fb = None
failed_logins = 0

class Config():
    maks_pinjam = 0
    lama_pinjam = 0

    def __init__(self):
        db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

        cur = db_connection.cursor()
        cur.execute("SELECT * FROM config")
        result = cur.fetchall()

        for row_number, row_data in enumerate(result):
            self.maks_pinjam = row_data[0]
            self.lama_pinjam = row_data[1]
        
        cur.close()
        db_connection.close()
        
    def update_config(self, maks_pinjam, lama_pinjam):
        db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

        query = ("UPDATE config SET max_borrow = %s, return_days = %s")
        cur = db_connection.cursor()
        cur.execute(query, (maks_pinjam, lama_pinjam))
        db_connection.commit()
        cur.close()
        db_connection.close()
        
    def get_maks_pinjam(self):
        return self.maks_pinjam

    def get_lama_pinjam(self):
        return self.lama_pinjam
        
def signals(self):
    self.btnLogin.clicked.connect(self.login)
    self.btnExit.clicked.connect(self.exit)
    self.chkShowPassword.stateChanged.connect(self.show_hide_pass)

def konfigurasi_signals(self):
    self.btnUpdate.clicked.connect(self.update_konfigurasi)

def main_signals(self):
    self.btnBuku.clicked.connect(self.open_master_buku)
    self.btnPeminjam.clicked.connect(self.open_master_peminjam)
    self.btnPeminjaman.clicked.connect(self.open_trans_peminjaman)
    self.btnPengembalian.clicked.connect(self.open_trans_pengembalian)
    self.btnKonfigurasi.clicked.connect(self.open_konfigurasi)
    self.btnRefresh.clicked.connect(self.read_dashboard)
    self.actionExit_2.triggered.connect(self.exit_file)
    self.actionKonfigurasi.triggered.connect(self.konfigurasi_file)
    self.actionBuku.triggered.connect(self.buku_master)
    self.actionPeminjam.triggered.connect(self.peminjam_master)
    self.actionPeminjaman.triggered.connect(self.peminjaman_transaksi)
    self.actionPengembalian.triggered.connect(self.pengembalian_transaksi)
    self.actionAbout_2.triggered.connect(self.about_help)

def master_buku_signals(self):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tblBuku.sizePolicy().hasHeightForWidth())
    self.tblBuku.setSizePolicy(sizePolicy)
    self.tblBuku.setMinimumSize(QtCore.QSize(0, 0))
    self.btnCreate.clicked.connect(self.create_data_buku)
    self.btnUpdate.clicked.connect(self.update_data_buku)
    self.btnDelete.clicked.connect(self.delete_data_buku)
    self.btnClear.clicked.connect(self.clear_data_buku)
    self.btnRefresh.clicked.connect(self.refresh_data_buku)
    self.tblBuku.currentItemChanged.connect(self.load_data_buku)

def master_peminjam_signals(self):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tblPeminjam.sizePolicy().hasHeightForWidth())
    self.tblPeminjam.setSizePolicy(sizePolicy)
    self.tblPeminjam.setMinimumSize(QtCore.QSize(0, 0))
    self.btnCreate.clicked.connect(self.create_data_peminjam)
    self.btnUpdate.clicked.connect(self.update_data_peminjam)
    self.btnDelete.clicked.connect(self.delete_data_peminjam)
    self.btnClear.clicked.connect(self.clear_data_peminjam)
    self.btnRefresh.clicked.connect(self.refresh_data_peminjam)
    self.tblPeminjam.currentItemChanged.connect(self.load_data_peminjam)
    
def login(self):
    try:
        username = self.edtUsername.text()
        password = self.edtPassword.text()

        db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

        cur = db_connection.cursor()
        cur.execute("SELECT username, password "
                    "FROM user "
                    "WHERE UPPER(username) = '" + username.upper() + "' AND password = '" + password+ "'")
        result = cur.fetchone()
        cur.close()
        db_connection.close()

        if result == None:
            dlg = QMessageBox()
            dlg.setWindowTitle("Login failed!")
            dlg.setIcon(QMessageBox.Warning)
            dlg.setText("Login gagal\nSilakan periksa kembali username dan password anda")
            dlg.exec_()
            global failed_logins
            failed_logins += 1
            if failed_logins == 3:
                dlg = QMessageBox()
                dlg.setWindowTitle("Login failed!")
                dlg.setIcon(QMessageBox.Warning)
                dlg.setText("Terlalu banyak login gagal\nSystem akan keluar")
                dlg.exec_()
                LoginDialog.close()
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("Login berhasil")
            dlg.setIcon(QMessageBox.Information)
            dlg.setText("Selamat datang di Simple Library Management System")
            dlg.exec_()
            LoginDialog.hide()
            uim.read_dashboard()
            main_window.show()
    except mdb.Error as e:
        dlg = QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setIcon(QMessageBox.Critical)
        dlg.setText("Error telah terjadi di system")
        dlg.exec_()

def exit(self):
    LoginDialog.close()

def show_hide_pass(self):
    if self.chkShowPassword.checkState() == Qt.Checked:
        self.edtPassword.setEchoMode(QLineEdit.Normal)
    else:
        self.edtPassword.setEchoMode(QLineEdit.Password)
        
def trans_peminjaman_signals(self):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tblPeminjaman.sizePolicy().hasHeightForWidth())
    self.tblPeminjaman.setSizePolicy(sizePolicy)
    self.tblPeminjaman.setMinimumSize(QtCore.QSize(0, 0))
    self.btnCreate.clicked.connect(self.create_trans_peminjaman)
    self.btnUpdate.clicked.connect(self.update_trans_peminjaman)
    self.btnDelete.clicked.connect(self.delete_trans_peminjaman)
    self.btnClear.clicked.connect(self.clear_trans_peminjaman)
    self.btnRefresh.clicked.connect(self.refresh_trans_peminjaman)
    self.tblPeminjaman.currentItemChanged.connect(self.load_trans_peminjaman)
    self.edtKodeBuku.editingFinished.connect(self.read_master_peminjaman)
    self.edtKodePeminjam.editingFinished.connect(self.read_master_peminjaman)
    self.btnCariPeminjam.clicked.connect(self.find_peminjam)
    self.btnCariBuku.clicked.connect(self.find_buku)

def trans_pengembalian_signals(self):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tblPengembalian.sizePolicy().hasHeightForWidth())
    self.tblPengembalian.setSizePolicy(sizePolicy)
    self.tblPengembalian.setMinimumSize(QtCore.QSize(0, 0))
    self.btnUpdate.clicked.connect(self.update_trans_pengembalian)
    self.btnDelete.clicked.connect(self.delete_trans_pengembalian)
    self.btnClear.clicked.connect(self.clear_trans_pengembalian)
    self.btnRefresh.clicked.connect(self.refresh_trans_pengembalian)
    self.tblPengembalian.currentItemChanged.connect(self.load_trans_pengembalian)
    self.edtKodeBuku.editingFinished.connect(self.read_master_pengembalian)
    self.edtKodePeminjam.editingFinished.connect(self.read_master_pengembalian)
    self.btnCariPeminjam.clicked.connect(self.find_peminjam)
    self.btnCariBuku.clicked.connect(self.find_buku)

def find_peminjam_signals(self):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tblData.sizePolicy().hasHeightForWidth())
    self.tblData.setSizePolicy(sizePolicy)
    self.tblData.setMinimumSize(QtCore.QSize(0, 0))
    self.btnSelect.clicked.connect(self.return_kode_peminjam)    

def find_buku_signals(self):
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tblData.sizePolicy().hasHeightForWidth())
    self.tblData.setSizePolicy(sizePolicy)
    self.tblData.setMinimumSize(QtCore.QSize(0, 0))
    self.btnSelect.clicked.connect(self.return_kode_buku)    

def update_konfigurasi(self):
    maks_pinjam = self.edtMaksPinjam.text().strip()
    lama_pinjam = self.edtLamaPinjam.text().strip()

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan melakukan update konfigurasi\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return
    
    config = Config()
    config.update_config(maks_pinjam, lama_pinjam)
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Konfigurasi telah berhasil diupdate")
    dlg.exec_()

def login(self):
    try:
        username = self.edtUsername.text()
        password = self.edtPassword.text()

        db_connection = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database="lmsdb")

        cur = db_connection.cursor()
        cur.execute("SELECT username, password "
                    "FROM user "
                    "WHERE UPPER(username) = '" + username.upper() + "' AND password = '" + password+ "'")
        result = cur.fetchone()
        cur.close()
        db_connection.close()

        if result == None:
            dlg = QMessageBox()
            dlg.setWindowTitle("Login failed!")
            dlg.setIcon(QMessageBox.Warning)
            dlg.setText("Login gagal\nSilakan periksa kembali username dan password anda")
            dlg.exec_()
            global failed_logins
            failed_logins += 1
            if failed_logins == 3:
                dlg = QMessageBox()
                dlg.setWindowTitle("Login failed!")
                dlg.setIcon(QMessageBox.Warning)
                dlg.setText("Terlalu banyak login gagal\nSystem akan keluar")
                dlg.exec_()
                LoginDialog.close()
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("Login berhasil")
            dlg.setIcon(QMessageBox.Information)
            dlg.setText("Selamat datang di Simple Library Management System")
            dlg.exec_()
            LoginDialog.hide()
            uim.read_dashboard()
            main_window.show()
            
    except mdb.Error as e:
        dlg = QMessageBox()
        dlg.setWindowTitle("Error")
        dlg.setIcon(QMessageBox.Critical)
        dlg.setText("Error telah terjadi di system")
        dlg.exec_()

def exit(self):
    LoginDialog.close()

def show_hide_pass(self):
    if self.chkShowPassword.checkState() == Qt.Checked:
        self.edtPassword.setEchoMode(QLineEdit.Normal)
    else:
        self.edtPassword.setEchoMode(QLineEdit.Password)

def open_master_buku(self):
    global MasterBuku
    global uib

    if MasterBuku not in globals():
        MasterBuku = QtWidgets.QDialog()
        uib = Ui_MasterBuku()
        uib.setupUi(MasterBuku)
        uib.signals()

    # Populate combo box with book categories
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")
    cur = db_connection.cursor()

    cur.execute("SELECT CONCAT(id, ':', name) AS Categories FROM categories ORDER BY id")

    result = cur.fetchall()

    for row_data in enumerate(result):
        uib.cboKategori.addItem(str(row_data[1][0]))

    cur.execute("SELECT * FROM book")
    result = cur.fetchall()

    for row_number, row_data in enumerate(result):
        uib.tblBuku.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            uib.tblBuku.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    cur.close()
    db_connection.close()
    MasterBuku.show()

def open_master_peminjam(self):
    global MasterPeminjam
    global uip

    if MasterPeminjam not in globals():
        MasterPeminjam = QtWidgets.QDialog()
        uip = Ui_MasterPeminjam()
        uip.setupUi(MasterPeminjam)
        uip.signals()

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM borrower")
    result = cur.fetchall()

    for row_number, row_data in enumerate(result):
        uip.tblPeminjam.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            uip.tblPeminjam.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            
    cur.close()
    db_connection.close()
    MasterPeminjam.show()

def open_trans_peminjaman(self):
    global TransPeminjaman
    global ui_tpm

    if TransPeminjaman not in globals():
        TransPeminjaman = QtWidgets.QDialog()
        ui_tpm = Ui_TransPeminjaman()
        ui_tpm.setupUi(TransPeminjaman)
        ui_tpm.signals()

    db_connection = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database="lmsdb")
    cur = db_connection.cursor()

    cur.execute("SELECT * FROM trans")
    result = cur.fetchall()

    for row_number, row_data in enumerate(result):
        ui_tpm.tblPeminjaman.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            ui_tpm.tblPeminjaman.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    cur.close()
    db_connection.close()
    TransPeminjaman.show()

def open_trans_pengembalian(self):
    global TransPengembalian
    global ui_tpk

    if TransPengembalian not in globals():
        TransPengembalian = QtWidgets.QDialog()
        ui_tpk = Ui_TransPengembalian()
        ui_tpk.setupUi(TransPengembalian)
        ui_tpk.signals()

    db_connection = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database="lmsdb")
    cur = db_connection.cursor()

    cur.execute("SELECT * FROM trans")
    result = cur.fetchall()

    for row_number, row_data in enumerate(result):
        ui_tpk.tblPengembalian.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            ui_tpk.tblPengembalian.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    cur.close()
    db_connection.close()
    TransPengembalian.show()

def open_konfigurasi(self):
    global Konfigurasi
    global uik
    
    if Konfigurasi not in globals():
        Konfigurasi = QtWidgets.QDialog()
        uik = Ui_Konfigurasi()
        uik.setupUi(Konfigurasi)
        uik.signals()

    config = Config()
    
    uik.edtMaksPinjam.setText(str(config.get_maks_pinjam()))
    uik.edtLamaPinjam.setText(str(config.get_lama_pinjam()))

    Konfigurasi.show()

def create_data_buku(self):
    kode_buku = uib.edtKodeBuku.text().strip()
    judul_buku = uib.edtJudulBuku.text().strip()
    pengarang = uib.edtPengarang.text().strip()
    kategori_buku = uib.cboKategori.currentIndex() + 1
    quantity = uib.spnJumlahBuku.value()

    # Validasi data
    err_msg = ''
    if kode_buku == '':
        err_msg += 'Kode buku tidak boleh kosong\n'
    if judul_buku == '':
        err_msg += 'Judul buku tidak boleh kosong\n'
    if pengarang == '':
        err_msg += 'Nama pengarang tidak boleh kosong\n'
    if quantity <= 0:    
        err_msg += 'Quantity buku tidak boleh minus atau sama dengan nol\n'

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM book WHERE id = '" + kode_buku + "'")
    result = cur.fetchall()
    if len(result) != 0:
        err_msg += 'Kode buku tersebut sudah ada, periksa kembali kode buku\n'

    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan menambah data buku dengan Kode : " + kode_buku + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    query = ("INSERT INTO book (id, title, author, category_id, quantity) VALUES (%s, %s, %s, %s, %s)")
    cur = db_connection.cursor()
    cur.execute(query, (kode_buku, judul_buku, pengarang, kategori_buku, quantity))
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Kode buku : " + kode_buku + " telah ditambahkan")
    dlg.exec_()
    self.refresh_data_buku()

def update_data_buku(self):
    kode_buku = uib.edtKodeBuku.text().strip()
    judul_buku = uib.edtJudulBuku.text().strip()
    pengarang = uib.edtPengarang.text().strip()
    kategori_buku = uib.cboKategori.currentIndex() + 1
    quantity = uib.spnJumlahBuku.value()

    # Validasi data
    err_msg = ''
    if kode_buku == '':
        err_msg += 'Kode buku tidak boleh kosong\n'
    if judul_buku == '':
        err_msg += 'Judul buku tidak boleh kosong\n'
    if pengarang == '':
        err_msg += 'Nama pengarang tidak boleh kosong\n'
    if quantity <= 0:
        err_msg += 'Quantity buku tidak boleh minus atau sama dengan nol\n'

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM book WHERE id = '" + kode_buku + "'")
    result = cur.fetchall()
    if len(result) == 0:
        err_msg += 'Kode buku tersebut tidak ada, periksa kembali kode buku\n'

    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan melakukan update data buku dengan Kode : " + kode_buku + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    query = ("UPDATE book SET id = %s, title = %s, author = %s, category_id = %s, quantity = %s WHERE id = %s")
    cur = db_connection.cursor()
    cur.execute(query, (kode_buku, judul_buku, pengarang, kategori_buku, quantity, kode_buku))
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Kode buku : " + kode_buku + " telah diupdate")
    dlg.exec_()
    self.refresh_data_buku()

def delete_data_buku(self):
    book_id = uib.edtKodeBuku.text().strip()

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    err_msg = ''
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM trans WHERE book_id = '" + book_id + "'")
    result = cur.fetchall()
    if len(result) != 0:
        err_msg += 'Kode buku tersebut sudah dipakai untuk transaksi, hapus terlebih dahulu data transaksi\n'
        
    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan menghapus data buku dengan Kode : " + book_id + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    cur = db_connection.cursor()
    cur.execute("DELETE FROM book WHERE id = %s", [book_id])
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Kode buku : " + book_id + " telah dihapus")
    dlg.exec_()
    self.refresh_data_buku()

def clear_data_buku(self):
    uib.edtKodeBuku.setText('')
    uib.edtJudulBuku.setText('')
    uib.edtPengarang.setText('')
    uib.cboKategori.setCurrentIndex(0)
    uib.spnJumlahBuku.setValue(1)

def refresh_data_buku(self):
    uib.tblBuku.clearSelection()
    uib.tblBuku.setRowCount(0)
    # Refresh table data
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    
    cur.execute("SELECT * FROM book")
    result = cur.fetchall()
    if len(result) > 0:
        for row_number, row_data in enumerate(result):
            uib.tblBuku.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                uib.tblBuku.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
def load_data_buku(self):
    if uib.tblBuku.currentRow()>=0:
        item = uib.tblBuku.item(uib.tblBuku.currentRow(), 0)
        db_connection = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="lmsdb")
        cur = db_connection.cursor()
        cur.execute("SELECT * FROM book WHERE id='" + item.text() + "'")
        result = cur.fetchall()
        for row_number, row_data in enumerate(result):
            uib.edtKodeBuku.setText(str(row_data[0]))
            uib.edtJudulBuku.setText(str(row_data[1]))
            uib.edtPengarang.setText(str(row_data[2]))
            uib.cboKategori.setCurrentIndex(int(row_data[3]) - 1)
            uib.spnJumlahBuku.setValue(int(row_data[4]))
        cur.close()
        db_connection.close()

def create_data_peminjam(self):
    kode_peminjam = uip.edtKodePeminjam.text().strip()
    no_identitas = uip.edtNoIdentitas.text().strip()
    nama_depan = uip.edtNamaDepan.text().strip()
    nama_belakang = uip.edtNamaBelakang.text().strip()
    alamat = uip.txtAlamat.toPlainText()

    # Validasi data
    err_msg = ''
    if kode_peminjam == '':
        err_msg += 'Kode peminjam tidak boleh kosong\n'
    if no_identitas == '':
        err_msg += 'Nomor identitas tidak boleh kosong\n'
    if nama_depan == '':
        err_msg += 'Nama depan tidak boleh kosong\n'

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM borrower WHERE id = '" + kode_peminjam + "'")
    result = cur.fetchall()
    if len(result) != 0:
        err_msg += 'Kode peminjam tersebut sudah ada, periksa kembali kode peminjam\n'

    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan menambah data peminjam dengan Kode : " + kode_peminjam + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    query = ("INSERT INTO borrower (id, id_number, first_name, last_name, address) VALUES (%s, %s, %s, %s, %s)")
    cur = db_connection.cursor()
    cur.execute(query, (kode_peminjam, no_identitas, nama_depan, nama_belakang, alamat))
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Kode peminjam : " + kode_peminjam + " telah ditambahkan")
    dlg.exec_()
    self.refresh_data_peminjam()

def update_data_peminjam(self):
    kode_peminjam = uip.edtKodePeminjam.text().strip()
    no_identitas = uip.edtNoIdentitas.text().strip()
    nama_depan = uip.edtNamaDepan.text().strip()
    nama_belakang = uip.edtNamaBelakang.text().strip()
    alamat = uip.txtAlamat.toPlainText()

    # Validasi data
    err_msg = ''
    if kode_peminjam == '':
        err_msg += 'Kode peminjam tidak boleh kosong\n'
    if no_identitas == '':
        err_msg += 'Nomor identitas tidak boleh kosong\n'
    if nama_depan == '':
        err_msg += 'Nama depan tidak boleh kosong\n'

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM borrower WHERE id = '" + kode_peminjam + "'")
    result = cur.fetchall()
    if len(result) == 0:
        err_msg += 'Kode peminjam tersebut tidak ada, periksa kembali kode peminjam\n'

    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan melakukan update data peminjam dengan Kode : " + kode_peminjam + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    query = ("UPDATE borrower SET id = %s, id_number = %s, first_name = %s, last_name = %s, address = %s WHERE id = %s")
    cur = db_connection.cursor()
    cur.execute(query, (kode_peminjam, no_identitas, nama_depan, nama_belakang, alamat, kode_peminjam))
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Kode peminjam : " + kode_peminjam + " telah diupdate")
    dlg.exec_()
    self.refresh_data_peminjam()

def delete_data_peminjam(self):
    borrower_id = uip.edtKodePeminjam.text().strip()

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    err_msg = ''
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM trans WHERE borrower_id = '" + borrower_id + "'")
    result = cur.fetchall()
    if len(result) != 0:
        err_msg += 'Kode peminjam tersebut sudah dipakai untuk transaksi, hapus terlebih dahulu data transaksi\n'
        
    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan menghapus data peminjam dengan Kode : " + borrower_id + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return
    
    cur = db_connection.cursor()
    cur.execute("DELETE FROM borrower WHERE id = %s", [borrower_id])
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Kode peminjam : " + borrower_id + " telah dihapus")
    dlg.exec_()    
    self.refresh_data_peminjam()

def clear_data_peminjam(self):
    uip.edtKodePeminjam.setText('')
    uip.edtNoIdentitas.setText('')
    uip.edtNamaDepan.setText('')
    uip.edtNamaBelakang.setText('')
    uip.txtAlamat.setText('')

def load_data_peminjam(self):
    if uip.tblPeminjam.currentRow()>=0:
        item = uip.tblPeminjam.item(uip.tblPeminjam.currentRow(), 0)
        db_connection = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="lmsdb")
        cur = db_connection.cursor()
        cur.execute("SELECT * FROM borrower WHERE id='" + item.text() + "'")
        result = cur.fetchall()
        for row_number, row_data in enumerate(result):
            uip.edtKodePeminjam.setText(str(row_data[0]))
            uip.edtNoIdentitas.setText(str(row_data[1]))
            uip.edtNamaDepan.setText(str(row_data[2]))
            uip.edtNamaBelakang.setText(str(row_data[3]))
            uip.txtAlamat.setText(str(row_data[4]))
        cur.close()
        db_connection.close()

def refresh_data_peminjam(self):
    uip.tblPeminjam.clearSelection()
    uip.tblPeminjam.setRowCount(0)
    # Refresh table data
    
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM borrower; ")
    result = cur.fetchall()
    if len(result) > 0:
        for row_number, row_data in enumerate(result):
            uip.tblPeminjam.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                uip.tblPeminjam.setItem(row_number, column_number, QTableWidgetItem(str(data)))

def create_trans_peminjaman(self):
    # trans_id = ui_tpm.edtKodeTrans.text().strip()
    tgl_trans = ui_tpm.dteTglTrans.date().toPyDate().strftime("%Y-%m-%d")
    kode_peminjam = ui_tpm.edtKodePeminjam.text().strip()
    kode_buku = ui_tpm.edtKodeBuku.text().strip()
    # tgl_hrs_kembali = ui_tpm.dteTglHrsKembali.date().toPyDate().strftime("%Y-%m-%d")

    config = Config()
    maks_pinjam = config.get_maks_pinjam()
    lama_pinjam = config.get_lama_pinjam()
    tgl_hrs_kembali = ui_tpm.dteTglTrans.date().toPyDate() + timedelta(days = lama_pinjam)
    tgl_hrs_kembali = tgl_hrs_kembali.strftime("%Y-%m-%d")
    
    # Validasi data
    err_msg = ''
    if kode_peminjam == '':
        err_msg += 'Kode peminjam tidak boleh kosong\n'
    if kode_buku == '':
        err_msg += 'Kode buku tidak boleh kosong\n'

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM borrower WHERE id = '" + kode_peminjam + "'")
    result = cur.fetchall()
    if len(result) == 0:
        err_msg += 'Kode peminjam tidak dapat ditemukan, periksa kembali kode peminjam\n'

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM book WHERE id = '" + kode_buku + "'")
    result = cur.fetchall()
    if len(result) == 0:
        err_msg += 'Kode buku tidak dapat ditemukan, periksa kembali kode buku\n'    

    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM trans WHERE borrower_id = '" + kode_peminjam + "' "
                "AND book_id = '" + kode_buku + "' "
                "AND return_date IS NULL")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if row_data[0] > 0:
                    err_msg += 'Kode peminjam : ' + kode_peminjam + ' sudah meminjam kode buku : ' + kode_buku + '\n'
    
    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM trans WHERE borrower_id = '" + kode_peminjam + "' "
                "AND return_date IS NULL")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if row_data[0] >= maks_pinjam:
                    err_msg += 'Kode peminjam : ' + kode_peminjam + ' sudah meminjam buku lebih dari : ' + str(maks_pinjam) + '\n'

    cur = db_connection.cursor()
    cur.execute("SELECT quantity - COUNT(*) FROM book inner join trans on trans.book_id = book.id WHERE book.id = '" + kode_buku + "' "
                "AND return_date IS NULL")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if row_data[0] <= 0:
                    err_msg += 'Kode buku : ' + kode_buku + ' tidak tersedia karena sedang dipinjam semua\n'
    
    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return
    
    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan menambah data transaksi peminjaman\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    query = ("INSERT INTO trans (id, borrow_date, borrower_id, book_id, def_return_date) VALUES (%s, %s, %s, %s, %s)")
    cur = db_connection.cursor()
    cur.execute(query, (0, tgl_trans, kode_peminjam, kode_buku, tgl_hrs_kembali))
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Transaksi berhasil disimpan")
    dlg.exec_() 
    self.refresh_trans_peminjaman()

def update_trans_peminjaman(self):
    trans_id = ui_tpm.edtKodeTrans.text().strip()
    tgl_trans = ui_tpm.dteTglTrans.date().toPyDate().strftime("%Y-%m-%d")
    kode_peminjam = ui_tpm.edtKodePeminjam.text().strip()
    kode_buku = ui_tpm.edtKodeBuku.text().strip()
    # tgl_hrs_kembali = ui_tpm.dteTglHrsKembali.date().toPyDate().strftime("%Y-%m-%d")

    config = Config()
    maks_pinjam = config.get_maks_pinjam()
    lama_pinjam = config.get_lama_pinjam()
    tgl_hrs_kembali = ui_tpm.dteTglTrans.date().toPyDate() + timedelta(days = lama_pinjam)
    tgl_hrs_kembali = tgl_hrs_kembali.strftime("%Y-%m-%d")
    
    # Validasi data
    err_msg = ''
    if kode_peminjam == '':
        err_msg += 'Kode peminjam tidak boleh kosong\n'
    if kode_buku == '':
        err_msg += 'Kode buku tidak boleh kosong\n'

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM borrower WHERE id = '" + kode_peminjam + "'")
    result = cur.fetchall()
    if len(result) == 0:
        err_msg += 'Kode peminjam tidak dapat ditemukan, periksa kembali kode peminjam\n'

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM book WHERE id = '" + kode_buku + "'")
    result = cur.fetchall()
    if len(result) == 0:
        err_msg += 'Kode buku tidak dapat ditemukan, periksa kembali kode buku\n'    

    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(*) FROM trans WHERE borrower_id = '" + kode_peminjam + "' "
                "AND book_id = '" + kode_buku + "' "
                "AND return_date IS NULL")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if row_data[0] > 0:
                    err_msg += 'Kode peminjam : ' + kode_peminjam + ' sudah meminjam kode buku : ' + kode_buku + '\n'
    
##    cur = db_connection.cursor()
##    cur.execute("SELECT COUNT(*) FROM trans WHERE borrower_id = '" + kode_peminjam + "' "
##                "AND return_date IS NULL")
##    result = cur.fetchall()
##    if len(result) != 0:
##        for row_number, row_data in enumerate(result):
##            for column_number, data in enumerate(row_data):
##                if row_data[0] >= maks_pinjam:
##                    err_msg += 'Kode peminjam : ' + kode_peminjam + ' sudah meminjam buku lebih dari : ' + str(maks_pinjam) + '\n'

    cur = db_connection.cursor()
    cur.execute("SELECT quantity - COUNT(*) FROM book inner join trans on trans.book_id = book.id WHERE book.id = '" + kode_buku + "' "
                "AND return_date IS NULL")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                if row_data[0] <= 0:
                    err_msg += 'Kode buku : ' + kode_buku + ' tidak tersedia karena sedang dipinjam semua\n'
                    
    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return
    
    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan melakukan update data transaksi peminjaman\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    query = ("UPDATE trans SET borrow_date = %s, borrower_id = %s, book_id = %s, def_return_date = %s WHERE id = %s")
    cur = db_connection.cursor()
    cur.execute(query, (tgl_trans, kode_peminjam, kode_buku, tgl_hrs_kembali, trans_id))
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Transaksi berhasil disimpan")
    dlg.exec_() 
    self.refresh_trans_peminjaman()

def delete_trans_peminjaman(self):
    trans_id = ui_tpm.edtKodeTrans.text().strip()

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan menghapus transaksi peminjaman dengan Kode : " + trans_id + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return

    db_connection = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database="lmsdb")
    cur = db_connection.cursor()
    cur.execute("DELETE FROM trans WHERE id = %s", [trans_id])
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Transaksi berhasil dihapus")
    dlg.exec_()
    ui_tpm.tblPeminjaman.setRowCount(0)
    self.refresh_trans_peminjaman()

def refresh_trans_peminjaman(self):
    ui_tpm.tblPeminjaman.clearSelection()
    ui_tpm.tblPeminjaman.setRowCount(0)
    # Refresh table data
    
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM trans; ")
    result = cur.fetchall()
    if len(result) > 0:
        for row_number, row_data in enumerate(result):
            ui_tpm.tblPeminjaman.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui_tpm.tblPeminjaman.setItem(row_number, column_number, QTableWidgetItem(str(data)))

def load_trans_peminjaman(self):
    if ui_tpm.tblPeminjaman.currentRow()>=0: #Checklagi
        item = ui_tpm.tblPeminjaman.item(ui_tpm.tblPeminjaman.currentRow(), 0)
        db_connection = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="lmsdb")
        cur = db_connection.cursor()
        cur.execute("SELECT * FROM trans WHERE id='" + item.text() + "'")
        result = cur.fetchall()
        if len(result) > 0:
            for row_number, row_data in enumerate(result):
                ui_tpm.edtKodeTrans.setText(str(row_data[0]))
                qdate = QtCore.QDate.fromString(str(row_data[1]), "yyyy-MM-dd")
                ui_tpm.dteTglTrans.setDate(qdate)
                ui_tpm.edtKodePeminjam.setText(str(row_data[2]))
                ui_tpm.edtKodeBuku.setText(str(row_data[3]))
                qdate = QtCore.QDate.fromString(str(row_data[4]), "yyyy-MM-dd")
                ui_tpm.dteTglHrsKembali.setDate(qdate)
        cur.close()
        db_connection.close()
    self.read_master_peminjaman()

def clear_trans_peminjaman(self):
    ui_tpm.edtKodeTrans.setText('')
    ui_tpm.dteTglTrans.setDate(QDate.currentDate())
    ui_tpm.edtKodePeminjam.setText('')
    ui_tpm.edtNamaPeminjam.setText('')
    ui_tpm.edtKodeBuku.setText('')
    ui_tpm.edtJudulBuku.setText('')
    ui_tpm.dteTglHrsKembali.setDate(QDate.currentDate())

def read_master_peminjaman(self):
    kode_peminjam = ui_tpm.edtKodePeminjam.text().strip()
    kode_buku = ui_tpm.edtKodeBuku.text().strip()
    nama_peminjam = ''
    judul_buku = ''
    
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT first_name FROM borrower WHERE id = '" + kode_peminjam + "'")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                nama_peminjam = row_data[0]

    cur = db_connection.cursor()
    cur.execute("SELECT title FROM book WHERE id = '" + kode_buku + "'")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                judul_buku = row_data[0]
    cur.close()
    db_connection.close()
    ui_tpm.edtNamaPeminjam.setText(nama_peminjam)
    ui_tpm.edtJudulBuku.setText(judul_buku)
    
def update_trans_pengembalian(self):
    trans_id = ui_tpk.edtKodeTrans.text().strip()
    tgl_pinjam = ui_tpk.dteTglTrans.date().toPyDate().strftime("%Y-%m-%d")
    tgl_kembali = ui_tpk.dteTglKembali.date().toPyDate().strftime("%Y-%m-%d")

    # Validasi data
    err_msg = ''
    if trans_id == '':
        err_msg += 'Kode transaksi boleh kosong\n'

    if tgl_kembali < tgl_pinjam:
        err_msg += 'Tanggal kembali tidak boleh lebih awal dari tanggal pinjam\n'
        
    if err_msg != '':
        dlg = QMessageBox()
        dlg.setWindowTitle("Invalid data")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("Terdapat data yang tidak valid:\n" + err_msg)
        dlg.exec_()
        return
    
    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan melakukan update data transaksi pengembalian\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return
    
    db_connection = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="lmsdb")
    query = ("UPDATE trans SET return_date = %s WHERE id = %s")
    cur = db_connection.cursor()
    cur.execute(query, (tgl_kembali, trans_id))
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Transaksi berhasil diupdate")
    dlg.exec_() 
    self.refresh_trans_pengembalian()

def delete_trans_pengembalian(self):
    trans_id = ui_tpk.edtKodeTrans.text().strip()

    dlg = QMessageBox()
    dlg.setWindowTitle("Konfirmasi")
    dlg.setIcon(QMessageBox.Question)
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setDefaultButton(QMessageBox.Yes)
    dlg.setText("Anda akan menghapus transaksi pengembalian dengan Kode : " + trans_id + "\nLanjutkan?")
    if (dlg.exec_() == QMessageBox.No):
        return
    
    db_connection = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="lmsdb")
    query = ("UPDATE trans SET return_date = NULL WHERE id = " + trans_id)
    cur = db_connection.cursor()
    cur.execute(query)
    db_connection.commit()
    cur.close()
    db_connection.close()
    dlg = QMessageBox()
    dlg.setWindowTitle("Informasi")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Transaksi berhasil dihapus")
    dlg.exec_()
    self.refresh_trans_pengembalian()

def refresh_trans_pengembalian(self):
    ui_tpk.tblPengembalian.clearSelection()
    ui_tpk.tblPengembalian.setRowCount(0)
    # Refresh table data
    
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT * FROM trans; ")
    result = cur.fetchall()
    if len(result) > 0:
        for row_number, row_data in enumerate(result):
            ui_tpk.tblPengembalian.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                ui_tpk.tblPengembalian.setItem(row_number, column_number, QTableWidgetItem(str(data)))

def load_trans_pengembalian(self):
    if ui_tpk.tblPengembalian.currentRow()>=0:
        item = ui_tpk.tblPengembalian.item(ui_tpk.tblPengembalian.currentRow(), 0)
        db_connection = mdb.connect(
                host="localhost",
                user="root",
                password="",
                database="lmsdb")
        cur = db_connection.cursor()
        cur.execute("SELECT * FROM trans WHERE id='" + item.text() + "'")
        result = cur.fetchall()
        for row_number, row_data in enumerate(result):
            ui_tpk.edtKodeTrans.setText(str(row_data[0]))
            qdate = QtCore.QDate.fromString(str(row_data[1]), "yyyy-MM-dd")
            ui_tpk.dteTglTrans.setDate(qdate)
            ui_tpk.edtKodePeminjam.setText(str(row_data[2]))
            ui_tpk.edtKodeBuku.setText(str(row_data[3]))
            qdate = QtCore.QDate.fromString(str(row_data[4]), "yyyy-MM-dd")
            ui_tpk.dteTglHrsKembali.setDate(qdate)
            qdate = QtCore.QDate.fromString(str(row_data[5]), "yyyy-MM-dd")
            if qdate:
                ui_tpk.dteTglKembali.setDate(qdate)
            else:
                ui_tpk.dteTglKembali.setDate(QDate(1900, 1, 1))
        cur.close()
        db_connection.close()
    self.read_master_pengembalian()

def clear_trans_pengembalian(self):
    ui_tpk.dteTglTrans.setDate(QDate.currentDate())
    ui_tpk.dteTglKembali.setDate(QDate.currentDate())
    ui_tpk.dteTglHrsKembali.setDate(QDate.currentDate()) #Checkroot1
    ui_tpk.edtKodePeminjam.setText('')
    ui_tpk.edtNamaPeminjam.setText('')
    ui_tpk.edtKodeBuku.setText('')
    ui_tpk.edtJudulBuku.setText('')

def read_master_pengembalian(self):
    kode_peminjam = ui_tpk.edtKodePeminjam.text().strip()
    kode_buku = ui_tpk.edtKodeBuku.text().strip()
    nama_peminjam = ''
    judul_buku = ''
    
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT first_name FROM borrower WHERE id = '" + kode_peminjam + "'")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                nama_peminjam = row_data[0]

    cur = db_connection.cursor()
    cur.execute("SELECT title FROM book WHERE id = '" + kode_buku + "'")
    result = cur.fetchall()
    if len(result) != 0:
        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                judul_buku = row_data[0]
    cur.close()
    db_connection.close()
    ui_tpk.edtNamaPeminjam.setText(nama_peminjam)
    ui_tpk.edtJudulBuku.setText(judul_buku)

def exit_file(self):
    sys.exit()

def konfigurasi_file(self):
    self.open_konfigurasi()

def buku_master(self):
    self.open_master_buku()

def peminjam_master(self):
    self.open_master_peminjam()

def peminjaman_transaksi(self):
    self.open_trans_peminjaman()

def pengembalian_transaksi(self):
    self.open_trans_pengembalian()

def about_help(self):
    dlg = QMessageBox()
    dlg.setWindowTitle("About Program")
    dlg.setIcon(QMessageBox.Information)
    dlg.setText("Simple Library Management System\n"
                "Tugas Akhir Mata Kuliah Logika dan Teknik Pemrograman\n"
                "Kelompok 1:\nAlexander Dalimarta Siregar (NIM: 1002210031)\nAlfroot Riski Rorong (NIM: 1002210068)\n"
                "Faiz Azhari M (NIM: 1002210075)")
    dlg.exec_()

def read_dashboard(self):
    total_peminjam = 0
    total_buku = 0
    total_buku_dipinjam = 0
    total_buku_tersedia = 0
    
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")

    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(id) FROM borrower")
    result = cur.fetchall()
    for row_number, row_data in enumerate(result):
        for column_number, data in enumerate(row_data):
            total_peminjam = row_data[0]

    cur = db_connection.cursor()
    cur.execute("SELECT SUM(quantity) FROM book")
    result = cur.fetchall()
    for row_number, row_data in enumerate(result):
        for column_number, data in enumerate(row_data):
            if row_data[0] is None:
                total_buku = 0
            else:
                total_buku = row_data[0]

    cur = db_connection.cursor()
    cur.execute("SELECT COUNT(id) FROM trans WHERE return_date IS NULL")
    result = cur.fetchall()
    for row_number, row_data in enumerate(result):
        for column_number, data in enumerate(row_data):
            total_buku_dipinjam = row_data[0]

    cur.close()
    db_connection.close()
    total_buku_tersedia = total_buku - total_buku_dipinjam

    uim.edtTotalPeminjam.setText(str(total_peminjam))
    uim.edtTotalBuku.setText(str(total_buku))
    uim.edtTotalBukuDipinjam.setText(str(total_buku_dipinjam))
    uim.edtTotalBukuTersedia.setText(str(total_buku_tersedia))

def find_peminjam(self):
    global FindPeminjam
    global ui_fp
    
    if FindPeminjam not in globals():
        FindPeminjam = QtWidgets.QDialog()
        ui_fp = Ui_FindPeminjam()
        ui_fp.setupUi(FindPeminjam)
        ui_fp.signals()

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")
    cur = db_connection.cursor()

    cur.execute("SELECT id, first_name FROM borrower ORDER BY id")
    result = cur.fetchall()

    ui_fp.tblData.setRowCount(0)
    for row_number, row_data in enumerate(result):
        ui_fp.tblData.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            ui_fp.tblData.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    cur.close()
    db_connection.close()
    FindPeminjam.show()

def find_buku(self):
    global FindBuku
    global ui_fb
    
    if FindBuku not in globals():
        FindBuku = QtWidgets.QDialog()
        ui_fb = Ui_FindBuku()
        ui_fb.setupUi(FindBuku)
        ui_fb.signals()

    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")
    cur = db_connection.cursor()

    cur.execute("SELECT id, title FROM book ORDER BY id")
    result = cur.fetchall()

    ui_fb.tblData.setRowCount(0)
    for row_number, row_data in enumerate(result):
        ui_fb.tblData.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            ui_fb.tblData.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    cur.close()
    db_connection.close()
    FindBuku.show()

def return_kode_buku(self):
    if self.tblData.currentRow() >= 0:
        if (TransPeminjaman.isVisible()):
            item = self.tblData.item(self.tblData.currentRow(), 0)
            ui_tpm.edtKodeBuku.setText(item.text().strip())
            ui_tpm.read_master_peminjaman()
        if (TransPengembalian.isVisible()):
            item = self.tblData.item(self.tblData.currentRow(), 0)
            ui_tpk.edtKodeBuku.setText(item.text().strip())
            ui_tpk.read_master_pengembalian()            
    FindBuku.close()
    
def return_kode_peminjam(self):
    if self.tblData.currentRow() >= 0:
        if (TransPeminjaman.isVisible()):
            item = self.tblData.item(self.tblData.currentRow(), 0)
            ui_tpm.edtKodePeminjam.setText(item.text().strip())
            ui_tpm.read_master_peminjaman()
        if (TransPengembalian.isVisible()):
            item = self.tblData.item(self.tblData.currentRow(), 0)
            ui_tpk.edtKodePeminjam.setText(item.text().strip())
            ui_tpk.read_master_pengembalian()            
    FindPeminjam.close()

Ui_Dialog.signals = signals
Ui_Dialog.login = login
Ui_Dialog.exit = exit
Ui_Dialog.show_hide_pass = show_hide_pass

Ui_Konfigurasi.signals = konfigurasi_signals
Ui_Konfigurasi.update_konfigurasi = update_konfigurasi

Ui_MainWindow.signals = main_signals
Ui_MainWindow.open_master_buku = open_master_buku
Ui_MainWindow.open_master_peminjam = open_master_peminjam
Ui_MainWindow.open_trans_peminjaman = open_trans_peminjaman
Ui_MainWindow.open_trans_pengembalian = open_trans_pengembalian
Ui_MainWindow.open_konfigurasi = open_konfigurasi
Ui_MainWindow.read_dashboard = read_dashboard
Ui_MainWindow.exit_file = exit_file
Ui_MainWindow.konfigurasi_file = konfigurasi_file
Ui_MainWindow.buku_master = buku_master
Ui_MainWindow.peminjam_master = peminjam_master
Ui_MainWindow.peminjaman_transaksi = peminjaman_transaksi
Ui_MainWindow.pengembalian_transaksi = pengembalian_transaksi
Ui_MainWindow.about_help = about_help

Ui_MasterBuku.signals = master_buku_signals
Ui_MasterBuku.load_data_buku = load_data_buku
Ui_MasterBuku.create_data_buku = create_data_buku
Ui_MasterBuku.update_data_buku = update_data_buku
Ui_MasterBuku.delete_data_buku = delete_data_buku
Ui_MasterBuku.refresh_data_buku = refresh_data_buku
Ui_MasterBuku.clear_data_buku = clear_data_buku

Ui_MasterPeminjam.signals = master_peminjam_signals
Ui_MasterPeminjam.load_data_peminjam = load_data_peminjam
Ui_MasterPeminjam.create_data_peminjam = create_data_peminjam
Ui_MasterPeminjam.update_data_peminjam = update_data_peminjam
Ui_MasterPeminjam.delete_data_peminjam = delete_data_peminjam
Ui_MasterPeminjam.refresh_data_peminjam = refresh_data_peminjam
Ui_MasterPeminjam.clear_data_peminjam = clear_data_peminjam

Ui_TransPeminjaman.signals = trans_peminjaman_signals
Ui_TransPeminjaman.load_trans_peminjaman = load_trans_peminjaman
Ui_TransPeminjaman.create_trans_peminjaman = create_trans_peminjaman
Ui_TransPeminjaman.update_trans_peminjaman = update_trans_peminjaman
Ui_TransPeminjaman.delete_trans_peminjaman = delete_trans_peminjaman
Ui_TransPeminjaman.refresh_trans_peminjaman = refresh_trans_peminjaman
Ui_TransPeminjaman.clear_trans_peminjaman = clear_trans_peminjaman
Ui_TransPeminjaman.read_master_peminjaman = read_master_peminjaman
Ui_TransPeminjaman.find_peminjam = find_peminjam
Ui_TransPeminjaman.find_buku = find_buku

Ui_TransPengembalian.signals = trans_pengembalian_signals
Ui_TransPengembalian.load_trans_pengembalian = load_trans_pengembalian
Ui_TransPengembalian.update_trans_pengembalian = update_trans_pengembalian
Ui_TransPengembalian.delete_trans_pengembalian = delete_trans_pengembalian
Ui_TransPengembalian.refresh_trans_pengembalian = refresh_trans_pengembalian
Ui_TransPengembalian.clear_trans_pengembalian = clear_trans_pengembalian
Ui_TransPengembalian.read_master_pengembalian = read_master_pengembalian
Ui_TransPengembalian.find_peminjam = find_peminjam
Ui_TransPengembalian.find_buku = find_buku

Ui_FindPeminjam.signals = find_peminjam_signals
Ui_FindPeminjam.return_kode_peminjam = return_kode_peminjam

Ui_FindBuku.signals = find_buku_signals
Ui_FindBuku.return_kode_buku = return_kode_buku

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()    
    uim = Ui_MainWindow()
    uim.setupUi(main_window)
    uim.signals()

    MasterBuku = QtWidgets.QDialog()
    uib = Ui_MasterBuku()
    uib.setupUi(MasterBuku)
    uib.signals()

    MasterPeminjam = QtWidgets.QDialog()
    uip = Ui_MasterPeminjam()
    uip.setupUi(MasterPeminjam)
    uip.signals()

    TransPeminjaman = QtWidgets.QDialog()
    ui_tpm = Ui_TransPeminjaman()
    ui_tpm.setupUi(TransPeminjaman)
    ui_tpm.signals()

    TransPengembalian = QtWidgets.QDialog()
    ui_tpk = Ui_TransPengembalian()
    ui_tpk.setupUi(TransPengembalian)
    ui_tpk.signals()

    Konfigurasi = QtWidgets.QDialog()
    uik = Ui_Konfigurasi()
    uik.setupUi(Konfigurasi)
    uik.signals()

    FindPeminjam = QtWidgets.QDialog()
    ui_fp = Ui_FindPeminjam()
    ui_fp.setupUi(FindPeminjam)
    ui_fp.signals()

    FindBuku = QtWidgets.QDialog()
    ui_fb = Ui_FindBuku()
    ui_fb.setupUi(FindBuku)
    ui_fb.signals()
        
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(LoginDialog)
    ui.signals()
    LoginDialog.show()
    sys.exit(app.exec_())
