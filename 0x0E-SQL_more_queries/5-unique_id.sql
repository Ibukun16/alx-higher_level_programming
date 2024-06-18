-- A script that creates the table `unique_id` on MySQL server.
-- If table `unique_id` already exits, script holds.
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
