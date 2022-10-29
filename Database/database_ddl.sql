# Quote Of The Day - 2022 #
# Author: João Duarte

#Database Creation Query
CREATE DATABASE `quote_of_the_day_2022`;

# Quotes Table Creation #
CREATE TABLE `quotes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `likes` int DEFAULT NULL,
  `dislikes` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


