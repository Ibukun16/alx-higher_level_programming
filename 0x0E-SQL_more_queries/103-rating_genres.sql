-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_genres.name, rating sum.
-- Result sorted in descending order by their rating.
-- Only one SELECT statement is permissible.
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id GROUP BY title ORDER BY rating DESC;
