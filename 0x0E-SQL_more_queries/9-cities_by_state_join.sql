-- A script that lists all the cities contained in database `hbtn_0d_usa`.
-- Record display cities.id - cities.name - states.name.
-- Result must be sorted in ascending order by cities.id
SELECT cities.id, cities.name states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id;
