-- script that creates database: hbtn_0d_2 and user: user_0d_2
-- the user only has SELECT previlegeges in that database
-- Password: user_0d_2_pwd
-- script does not fail if database or user already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY `user_0d_2_pwd`;
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`;
FLUSH PRIVILEGES;
