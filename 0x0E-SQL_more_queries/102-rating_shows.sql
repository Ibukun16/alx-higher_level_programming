-- A script that list all shows from hbtn_0d_tvshows_rate by their rating
-- Each record display: tv_shows.title - rating sum
-- Result sorted in descending order by rating
-- Only one SELECT statement usable.
SELECT title, SUM(tv_show_ratings.rate) 'rating' FROM tv_shows LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id GROUP BY title ORDER BY rating DESC;
