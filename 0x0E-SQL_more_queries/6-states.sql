-- script that creates the database: hbtn_0d_usa, table: states
-- states description:
--	id INT, unique, auto genereated, can't be null, primarykey
--	name VARCHAR(256) can't be NULL
-- script should not fail if database or table already exists

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
