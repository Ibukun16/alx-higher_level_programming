-- A script that lists all shows without the genre Comedy in the database
-- tv_genres table contains only one record where name = Comedy but could be different.
-- Each record displa: tv_shows.title
-- Result sorted in ascending order by show title.
-- Maximum of two SELECT statement usable.
SELECT title FROM tv_shows WHERE title NOT IN (SELECT title FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = 'Comedy') GROUP BY title ORDER BY title ASC;
