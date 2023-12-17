-- Create the database
CREATE DATABASE IF NOT EXISTS stud;

-- Use the database
USE stud;

-- Create the student table
CREATE TABLE IF NOT EXISTS student (
    address VARCHAR(255),
    gender VARCHAR(10),
    moahel VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255),
    name VARCHAR(255),
    id INT AUTO_INCREMENT PRIMARY KEY
);
