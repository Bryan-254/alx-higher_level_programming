-- SQL script that creates the database hbtn_0d_2 and the user user_0d_2.
-- Create database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user if it doesn't exist and set password.
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd'
-- Grant SELECT privilege on hbtn_0d_2 database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
