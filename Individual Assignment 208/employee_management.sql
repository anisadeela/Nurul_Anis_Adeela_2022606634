-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 12:17 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `employee_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `Employee_ID` int(10) NOT NULL,
  `Employee_Name` varchar(100) NOT NULL,
  `Employee_Department` varchar(100) NOT NULL,
  `Job_Title` varchar(100) NOT NULL,
  `Experience_Years` int(100) NOT NULL,
  `Monthly_Salary` decimal(12,2) NOT NULL,
  `Annual_Salary` decimal(12,2) NOT NULL,
  `Total_Earnings` decimal(12,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`Employee_ID`, `Employee_Name`, `Employee_Department`, `Job_Title`, `Experience_Years`, `Monthly_Salary`, `Annual_Salary`, `Total_Earnings`) VALUES
(2022606634, 'NURUL ANIS ADEELA BINTI ROSELE', 'Executive', 'CEO', 4, 291482.00, 3497784.00, 13991136.00),
(2022606612, 'NURUL HANIN BINTI ROSLAN', 'Marketing', 'Social Media Specialist', 3, 6789.00, 81468.00, 244404.00),
(2022606613, 'NURUL HANIS BINTI OMAR', 'IT', 'Systems Administrator', 5, 7890.00, 94680.00, 473400.00),
(2022606614, 'AHMAD BIN DIN', 'Operations', 'Business Analyst', 6, 6754.00, 81048.00, 486288.00),
(2022606615, 'SULAIMAN BIN IDRIS', 'Human Resources', 'Recruiter', 7, 6785.00, 81420.00, 569940.00),
(2022606616, 'HAMZAH BIN ZAIN', 'Sales', 'Account Executive', 7, 7865.00, 94380.00, 660660.00),
(2022606617, 'ZULAIKHA BINTI ZULFAHMI', 'Finance', 'Accountant', 2, 3456.00, 41472.00, 82944.00);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
