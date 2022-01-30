# SimpleLybraryManagementSystem

Project Akhir Mata Kuliah Logika dan Teknik Pemrograman
Semester I Institut Teknologi Tangerang Selatan

Kelompok I:
1. Alexander Dalimarta Siregar (NIM: 1002210031)
2. Alfando Riski Rorong (NIM: 1002210068)
3. Faiz Azhari M (NIM: 1002210075)

Untuk menjalankan (compile dan execute) source code, ikut langkah berikut:
* Pastikan Python 3 sudah terinstall
* Pastikan module PyQt5 sudah terinstall
    * Untuk melihat apakah module PyQt5 sudah terinstall, jalankan "pip list" dari command line dan periksa apakah PyQt5, PyQt5-tools, dan PyQt5Designer sudah ada di list
    * Jika PyQt5, PyQt5-tools, dan PyQt5Designer tidak ada di list setelah menjalankan "pip list" maka lakukan instalasi module tersebut dengan cara:
          * Dari command line, ketikkan "pip install pyqt5" kemudian "pip install pyqt5-tools"
          * Setelah proses instalasi selesai jalankan lagi "pip list" untuk memastikan semua module tersebut sudah terinstall dengan baik
* Pastikan library mysqlclient sudah terinstall
    * Untuk melihat apakah module mysqlclient sudah terinstall, jalankan "pip list" dari command line dan periksa apakah mysqlclient sudah ada di list
    * Jika mysqlclient tidak ada di list setelah menjalankan "pip list" maka lakukan instalasi module tersebut dengan cara:
          * Akses https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient dari web browser Anda
          * Download package yang sesuai dengan versi Python dan operating system yang Anda gunakan (32 bit atau 64 bit)
          * Setelah melakukan download, lakukan instalasi dengan ketikkan perintah di bawah ini di command line:
            pip install mysqlclient-1.4.6-cp38-cp38-win_amd64.whl
            Sesuaikan nama package tersebut dengan package yang sudah Anda download sebelumnya
          * Setelah proses instalasi selesai jalankan lagi "pip list" untuk memastikan semua module mysqlclient tersebut sudah terinstall dengan baik
* Pastikan MySQL atau MariaDB sudah terinstall dan Anda memiliki akses serta privelege untuk membuat dan mengakses database

Setelah semua requirements tersebut, ikuti langkah dibawah ini untuk setup dan konfigurasi database:
1. Install font dripicons-v2.ttf yang disertakan sesuai dengan operating system yang Anda gunakan
2. Login ke MySQL dan dari mysql shell jalankan script SQL untuk membuat skema database dan table dan juga data sample
3. Setelah masuk ke mysql shell, jalankan perintah: 
    * CREATE DATABASE lmsdb;
    * USE lmsdb;
    * source lmsdb.sql
4. Setelah proses restore data selesai jalankan perintah SHOW TABLES; untuk memastikan semua table sudah terbentuk (book, borrower, categories, config, trans, user)
5. Pada bagian code untuk melakukan koneksi ke database:
    db_connection = mdb.connect(
        host="localhost",
        user="root",
        password="",
        database="lmsdb")
   Sesuaikan credentials (host, user, password) sesuai dengan credentials MySQL Anda

# End of File
