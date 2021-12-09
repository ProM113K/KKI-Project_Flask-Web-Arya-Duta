-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2021 at 02:23 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_katalogbuku`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `iduser` int(3) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `alamat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`iduser`, `nama`, `username`, `password`, `alamat`) VALUES
(1, 'Dimas Putra Widiyanto', 'prom113k', 'admin', 'Sidamukti'),
(3, 'Satya Pamungkas', 'satya113', 'admin', 'Cilangkap');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `idbuku` int(3) NOT NULL,
  `kd_buku` varchar(10) NOT NULL,
  `kategori` varchar(3) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `harga` int(10) NOT NULL,
  `deskripsi` text NOT NULL,
  `isbn` varchar(17) NOT NULL,
  `penulis` varchar(30) NOT NULL,
  `ukuran` varchar(20) DEFAULT NULL,
  `halaman` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`idbuku`, `kd_buku`, `kategori`, `nama`, `harga`, `deskripsi`, `isbn`, `penulis`, `ukuran`, `halaman`) VALUES
(1, '1-sd.jpg', 'SD', 'Diriku', 23000, 'Buku ini berisi tentang penjelasan bagaimana menjadi diri sendiri dan pribadi yang baik', '978-979-094-305-6', 'Sarkonah, dkk', 'A4 (21 x 29,7 cm)', 188),
(11, '7-sd.jpg', 'SD', 'Lingkungan bersih, asri dan sehat', 34500, 'Kebersihan sebagaian dari iman', '123-988-232-212', 'Tere Liye', 'A4', 146),
(12, '1-sma.jpg', 'SMA', 'Bahasa Indonesia', 34000, 'Buku bahasa indonesia terpadu', '123-422-232-212', 'Mawardi', 'A4', 240),
(13, '5-smp.jpg', 'SMP', 'Pendidikan Jasmani Olahraga dan Kesehatan', 32000, 'Buku terpadu untuk siswa mengenai olahraga', '322-530-326-032', 'Arya Duta Group', 'A4', 87),
(14, '4-smp.jpg', 'SMP', 'Matematika', 37000, 'Buku lembar kerja siswa matematika', '321-456-908-354', 'Syahrani, dkk', 'A4', 98),
(15, '8-sd.jpg', 'SD', 'Benda, Hewan, dan Tanaman di Sekitarku', 35400, 'Buku untuk mempelajari lingkungan hidup', '322-530-326-032', 'Arya Duta Group', 'A4', 48),
(20, '5-sd.jpg', 'SD', 'Peristiwa Alam', 50000000, 'Buku peristiwa alam', '321-456-908-354', 'LP3I', 'A4', 454545);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`iduser`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`idbuku`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `iduser` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `idbuku` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
