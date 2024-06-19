-- A script that lists all shows, and all genres linked to
-- that show from the database hbtn_0d_tvshows.
-- If show doesn't have a genre, it display NULL in genre column
-- Each record displays: tv_shows.title, tv_genres.name
-- Result of the display sorted in ascending order by the show title and genre name.
-- SELECT statement usable only once.
SELECT title, name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genres_id = tv_genres.id ORDER BY title ASC, name ASC;
