-- A script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- Column 1 being genre, column 2 being number_of_shows.
-- Genre that doesn't have any shows linked should not be displayed.
-- Result must be sorted in descending order by number of shows linked.
-- SELECT statement can only be used once.
SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows' FROM tv_genres RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genre ORDER BY number_of_shows DESC;
