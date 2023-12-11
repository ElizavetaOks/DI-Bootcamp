-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5),
-- 	('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Leonardo','DiCaprio','11/11/1974', 1);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Angelina','Jolie','01/06/1975', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Johny','Depp','09/06/1963', 0),
-- 	('Tom', 'Cruise', '03/07/1962', 0),
-- 	('Meryl', 'Streep', '22/07/1949', 3),
-- 	('Tom', 'Hanks', '09/07/1956', 2),
-- 	('Robert', 'Downey Jr', '04/04/1965', 0);

-- select count(actor_id) from actors

INSERT INTO actors (first_name, last_name)
VALUES('Scarlett','Johansson');