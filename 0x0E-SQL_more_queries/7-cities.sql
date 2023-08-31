-- script that creates the database: hbtn_0d_usa and table: cities
-- cities desciption:
--	id INT, unique, auto generated, can't be NULL, PK
--	state_id INT, can't be NULL, Foreign key that references
--		to id of the states table
--	name VARCHAR(256) can't be NULL
-- script does not fail if database or table already exists

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
