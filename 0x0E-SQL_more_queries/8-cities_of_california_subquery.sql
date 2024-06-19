-- A script that lists all the cities of California that can be found in hbtn_0d_usa.
-- State musts contain only one record where name = California but
-- could of different id as per example.
-- Result sorted in ascending order by cities.
-- JOIN keyword not allowed.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
