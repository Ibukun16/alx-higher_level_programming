-- A script that creates database `hbtn_0d_2` and the `user_0d_2.
-- user_0d_2 only have SELECET privilege in the database hbtn_0d_2.
-- user_0d_2 password set to user_0d_2_pwd.
-- If database `hbtn_0d_2` or `user_0d_2' already exists, script will not fail.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED WITH mysql_native_password BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
