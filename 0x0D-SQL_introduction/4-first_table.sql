-- creates a table called first_table in the current database in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- switch to the database
USE hbtn_0c_0;

-- create the table
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
