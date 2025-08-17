-- SQL script to create a table users with following attributes:
-- id (INTEGER, NOT NULL, AUTO INCREMENT, PRIMARY KEY)
-- email (VARCHAR(255), NOT NULL, UNIQUE)
-- name (VARCHAR(255))
-- country (ENUM('US', 'CO', 'TN'), NOT NULL) default 'US'
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
