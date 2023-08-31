-- Lists all records in second_table with a score
-- greater than or equal to 10
-- in descending order

SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;