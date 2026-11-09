CREATE DATABASE IF NOT EXISTS vehicle_db;

USE vehicle_db;

CREATE TABLE vehicles(
    id INT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    year INT
);

