-- script that creates a table: unique_id
--	id INT, default value of 1 and must be unique
-- 	name VARCHAR(256)
-- database name will be passed as an argument of mysql command
-- script should not fail if unique_id table already exists

CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT	DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
