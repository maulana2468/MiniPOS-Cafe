-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 21 Bulan Mei 2021 pada 12.00
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database_cafe`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `menu_minuman`
--

CREATE TABLE `menu_minuman` (
  `id_menu` char(10) NOT NULL,
  `nama` char(15) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `menu_minuman`
--

INSERT INTO `menu_minuman` (`id_menu`, `nama`, `harga`) VALUES
('B111', 'KukuRasa', 2500),
('B321', 'Frisian Flak', 3000),
('B348', 'Energy', 4000),
('B431', 'TOP', 4600),
('B432', 'Joss Mantap', 3000),
('B546', 'Minerali', 6000),
('B553', 'OkkyJr', 2500),
('B876', 'Milk Ichi', 5000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `menu_minuman`
--
ALTER TABLE `menu_minuman`
  ADD PRIMARY KEY (`id_menu`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
