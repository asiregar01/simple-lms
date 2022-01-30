-- MySQL dump 10.16  Distrib 10.1.40-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: lmsdb
-- ------------------------------------------------------
-- Server version	10.1.40-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `id` varchar(50) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_CategoryID` (`category_id`),
  CONSTRAINT `FK_CategoryID` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES ('B-0001','Pengantar Filsafat','Jan Hendrik Rapar',1,5),('B-0002','Filfasat Pendidikan','Refika',2,3),('B-0003','Pengantar Filsafat Pengetahuan','Yusuf Lubis',2,1),('B-0004','Pengantar Ekonomi Mikro','Greg Mankiw',3,7),('B-0005','Akuntansi Keuangan Menengah','Kieso',3,6),('B-0006','Hukum Perdata Indonesia','Abdulkadir Muhammad',4,2),('B-0007','Pengantar Hukum Ketenagakerjaan','Lalu Husni',4,10),('B-0008','Dasar-Dasar Ilmu Politik','Miriam Budiardjo',5,4),('B-0009','Keamanan Jaringan Internet','Onno W. Purbo',6,7),('B-0010','Logika Pemrograman Python','Abdul Kadir',6,11),('B-0011','Pemrograman C : Soal dan Penyelesaian','R.H. Sianipar',6,8),('B-0012','Menyelami Keindahan Sastra Indonesia','Lianawati W.S.',7,8),('B-0013','Aku','Sjuman Djaya',7,5),('B-0014','Siti Nurbaya','Marah Roesli',7,1),('B-0015','Buku Guru Matematika','Asnah Tahar',9,9),('B-0016','Pemrograman C++','Abdul Kadir',6,5),('B-0020','Konsep TCP/IP','Onno W. Purbo',6,5);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrower`
--

DROP TABLE IF EXISTS `borrower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `borrower` (
  `id` varchar(50) NOT NULL,
  `id_number` varchar(45) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrower`
--

LOCK TABLES `borrower` WRITE;
/*!40000 ALTER TABLE `borrower` DISABLE KEYS */;
INSERT INTO `borrower` VALUES ('P-0001','3172051187190003','Budi','Cahyono','Jl. Mawar No. 1, RT 05 / RW 09, Jakarta Selatan'),('P-0002','3581052147190209','Alexander','Siregar','Jl. Raya Boulevard Barat RT 09 / RW 11, Jakarta Utara'),('P-0003','1860111641139010','Ani','Widiastuti','Jl. Martadinata No. 100, Jakarta'),('P-0004','1124198183112900','Alfando','Rorong','Jakarta Pusat'),('P-0005','2180188164916191','Andi','Hermansyah','Jakarta Selatan'),('P-0006','Adi','S','','');
/*!40000 ALTER TABLE `borrower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'AGAMA'),(2,'FILSAFAT'),(3,'EKONOMI'),(4,'HUKUM'),(5,'POLITIK'),(6,'TEKNIK'),(7,'SASTRA'),(8,'BAHASA'),(9,'MATEMATIKA'),(10,'FIKSI');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `max_borrow` int(11) DEFAULT NULL,
  `return_days` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES (3,7);
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trans`
--

DROP TABLE IF EXISTS `trans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `borrow_date` date DEFAULT NULL,
  `borrower_id` varchar(50) DEFAULT NULL,
  `book_id` varchar(50) DEFAULT NULL,
  `def_return_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_BookID` (`book_id`),
  KEY `FK_BorrowerID` (`borrower_id`),
  CONSTRAINT `FK_BookID` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `FK_BorrowerID` FOREIGN KEY (`borrower_id`) REFERENCES `borrower` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trans`
--

LOCK TABLES `trans` WRITE;
/*!40000 ALTER TABLE `trans` DISABLE KEYS */;
INSERT INTO `trans` VALUES (2,'2021-12-15','P-0001','B-0012','2021-12-22',NULL),(3,'2021-12-15','P-0001','B-0014','2021-12-22',NULL),(4,'2021-12-20','P-0002','B-0010','2021-12-27','2021-12-29'),(5,'2021-12-20','P-0003','B-0003','2021-12-27','2021-12-21'),(6,'2021-12-20','P-0004','B-0009','2021-12-27','2021-12-21'),(7,'2021-12-20','P-0004','B-0011','2021-12-27',NULL),(8,'2021-12-21','P-0003','B-0001','2021-12-28',NULL),(9,'2021-12-29','P-0004','B-0005','2022-01-05',NULL);
/*!40000 ALTER TABLE `trans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Alexander','Siregar','a','a');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-30 11:55:53
