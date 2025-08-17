--- SQL script to create a table users with following attributes:
--- id (INT, PRIMARY KEY, NOT NULL, AUTO INCREMENT)
--- email (VARCHAR(255), NOT NULL, UNIQUE)
--- name (VARCHAR(255))
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
