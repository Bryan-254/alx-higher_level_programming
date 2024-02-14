-- SQL script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

-- creates a database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create a table if it doesn't exists
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	UNIQUE KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
);
