# Quote Of TheDay
Quote of The Day Program. Really simple, non-formated results and console program. This program is inpired in the Quote of The Day Protocol, but, in this case the program doesn't make usage of any protocol, just some harcoded quotes in a database table. The purpose of this program is to test some basic Python language basic concepts.

## What is a Quote of The Day Program?
As defined in [Gokberk Yaltirakli - Quote of the Day (QOTD) Protocol](https://www.gkbrk.com/wiki/qotd_protocol/) a Quote of the Day is: 
> (...) a simple protocol that is used to deliver daily quotes. Although its usage is almost nonexistent these days, there are still a few public servers. The protocol is defined by RFC865. According to the RFC, a QOTD server is run on port 17 for TCP and UDP connections. It is an excellent protocol to learn the socket API and to write your first server.

For more detailded information read the article [here](https://www.gkbrk.com/wiki/qotd_protocol/).

## Database
### Diagram

![Database Diagram](https://github.com/jduarte98/QuoteOfTheDay/blob/main/Snapshots/db_diagram.png)
### DDL

Run this SQL Script to create the database of the application and its respective table.

```
# Database Creation Query
CREATE DATABASE `quote_of_the_day_2022`;

# Quotes Table Creation Query
CREATE TABLE `quotes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `likes` int DEFAULT NULL,
  `dislikes` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Application Usage
Before running the application you'll need to create a ``` .env ``` file in the project root directory. The file needs to contain the following information in the presented structure:

```
DB_PTH = path_to_your_mysql_server (i.e. localhost or 127.0.0.1)
DB_NM = your_database_name
DB_USR = your_mysql_user
DB_PW = your_mysql_password
```

### Usage Snapshot

![Usage Snapshot](https://github.com/jduarte98/QuoteOfTheDay/blob/main/Snapshots/exec_snapshot.png)

This is how the program will run / present the Quote of The Day.

 ## Technologies
 * [Python](https://www.python.org);
 * [MySQL Databse](https://www.mysql.com);
 
 
