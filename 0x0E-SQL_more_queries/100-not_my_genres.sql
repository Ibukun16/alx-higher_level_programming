-- A script that uses database `hbtn_0d_tvshows` to list all
-- genres not linked to show Dexter.
-- Table `tv_shows` contains only one record and title = Dexter but id could be different.
-- Each record displays: tv_genres.name
-- Result sorted in ascending order by the genre name
-- Maximum of 2 SELECT statement usable.
SELECT name FROM tv_genres WHERE name NOT IN (SELECT name FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter') GROUP BY name, ORDER BY name ASC;
