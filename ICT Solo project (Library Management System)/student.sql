-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 28, 2021 at 05:06 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

----
-- Database: `library management system`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

--CREATE TABLE `student` (
--  `First_name` varchar(100) NOT NULL,
--  `Last_name` varchar(100) NOT NULL,
--  `Student_ID` int(100) NOT NULL,
--  `Student_password` char(100) NOT NULL
--) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

--INSERT INTO `student` (`First_name`, `Last_name`, `Student_ID`, `Student_password`) VALUES
--('Amna', 'Hassan', 10, 'Amna3$'),
--('Amna', 'Khan', 11, 'Khan3$'),
--('Fareeha', 'Khan', 18, 'Fareeha3$'),
--('Javeria', 'Tahir', 34, 'Javeria3$');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
--ALTER TABLE `student`
--  ADD PRIMARY KEY (`Student_ID`);
--COMMIT;
--
--/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
--/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
--/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

SELECT *FROM student
