-- A script that converts hbtn_0c_0 database to UTF8 in MySQL server
-- convert Database hbtn_0c_0, first_table and field name in first_table to UTF8;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
