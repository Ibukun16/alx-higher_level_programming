-- A script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- tv_genres table contains only one record with name = Comedy but id could be different.
-- Each record displays: tv_shows.title
-- Result is sorted in ascending order by the show title
-- SELECT statement is usable only once.
SELECT title FROM tv_shows LEFT JOIN tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = 'Comedy' GROUP BY title ORDER BY title ASC;
