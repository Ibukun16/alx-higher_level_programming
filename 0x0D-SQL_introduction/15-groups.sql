-- A script that lists the number of records with the same score in `second_table`
-- table of hbtn_0c_0 in MySQL server.
-- Display  score, the number of records for score with the label number.
-- Sort list by the number of records in descending order.
SELECT score, count(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
