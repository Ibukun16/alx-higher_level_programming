-- A script that displays thetop 3 cities temperature during July and August ordered by temperature in descending order.
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE  month = 7 or month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
