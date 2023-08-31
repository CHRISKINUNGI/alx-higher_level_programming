-- script that creates a table `id_not_null`
-- 	id INT default value 1
--	name VARCHAR(256)
-- database is passed as an argument of the mysql command
-- if table exists your script should not fail

CREATE TABLE IF NOT EXISTS `id_not_null` (
	`id` INT	DEFAULT 1,
	`name` VARCHAR(256)
);
