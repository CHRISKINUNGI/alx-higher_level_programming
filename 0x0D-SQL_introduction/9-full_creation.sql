-- script that creates a second_table and has::
-- id int
-- name VARCHAR(256)
-- score int
-- database name is passed as an argument, if table
-- does not exist script does not fail
-- no use of SELECT OR SHOW

CREATE TABLE IF NOT EXISTS second_table (id INT,
name VARCHAR(256),
score INT);
INSERT INTO second_table
	(id, name, score)
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);

