-- A script that creates database `hbtn_0d_usa` and table `states` in the database on MySQL server.
-- If database `hbtn_0d_usa` or table `states` already exists, script should hold.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
