-- A script that creates the MySQL server user `user_0d_1`.
-- `user_0d_1` have all privileges of MySQL server
-- `user_0d_1` password set to `user_0d_1_pwd`
-- If the user user_0d_1 already exists, the script will not fail.
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
