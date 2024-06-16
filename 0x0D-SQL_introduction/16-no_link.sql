-- A script that lists all records of the table second_table of hbtn_0c_0 database in MySQL server.
-- Rows must be listed with a value name.
-- Result should display the score and the name.
-- Record should be listed in descending order.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC; 
