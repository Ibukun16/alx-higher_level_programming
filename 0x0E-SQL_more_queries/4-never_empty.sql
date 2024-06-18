-- A script that creates table `id_not_null` on MySQL server
-- If table `id_not_null' already exit, script should not fail.
CREATE TABLE IF NOT EXIST id_not_null (id INT DEFAULT 1, name VARCHAR(256));
