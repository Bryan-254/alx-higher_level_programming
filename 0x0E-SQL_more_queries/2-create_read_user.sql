-- SQL script that creates the database hbtn_0d_2 and the user user_0d_2.

-- creates a database if it doesn't exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creates a user if it doesn't exists
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- grants SELECT privileges on hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
