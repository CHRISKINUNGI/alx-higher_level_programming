-- script that creates table: force_name 
-- id INT
-- name VARCHAR(256) can't be NULL

-- database name will be passed as an argument of mysql command
-- if table exists the script should not fail

CREATE TABLE IF NOT EXISTS `force_name` (
	`id` INT,
	`name` VARCHAR(256) NOT NULL
);
