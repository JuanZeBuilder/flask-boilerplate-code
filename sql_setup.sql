-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

DROP DATABASE IF EXISTS `test_db`;
CREATE DATABASE IF NOT EXISTS `test_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `test_db`;

CREATE TABLE `users` (
  `user_id` varchar(200) PRIMARY KEY,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `hashed_password` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `creation_date` datetime(0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `hashed_password`, `email`, `creation_date`) VALUES
('fgdsaf23453215', 'john', 'cena', 'dma39fohw2g97hzslv218fjas', 'johncena@gmail.com', '')