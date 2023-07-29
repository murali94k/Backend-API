DROP SCHEMA IF EXISTS `app_db`;
CREATE SCHEMA `app_db` DEFAULT CHARACTER SET utf8;
use app_db;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `user_id` tinyint(3) NOT NULL AUTO_INCREMENT,
    `user_name` VARCHAR(50) NOT NULL,
    `user_email` VARCHAR(50) DEFAULT NULL,
    `user_password` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`user_id`),
    UNIQUE KEY `unique_users` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO users(user_name, user_email, user_password) VALUES ('user1','user1@gmail.com','pass1');