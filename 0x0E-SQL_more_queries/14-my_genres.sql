-- A script that uses the hbtn_0d_tvshows database to lists all
-- genres of the show Dexter.
-- tv_shows table contains only one record where title = Dexter but could be different.
-- Each record displays: tv_genres.name.
-- Result sorted in ascending order by the genre name.
-- SELECT statement could be used only once.
SELECT name FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter' GROUP BY name ORDER BY name ASC;
