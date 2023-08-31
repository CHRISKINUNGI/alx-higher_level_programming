-- lists all records of second_table
-- don't lists rows without a name value
-- display score then name in descending order
-- database name will be passed as an argument to the sql command

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;