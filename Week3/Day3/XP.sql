-- Exercise 1: DVD Rental
-- Get a list of all the languages, from the language table.
SELECT DISTINCT name FROM language

-- Get a list of all films joined with their languages – select the following details: 
-- film title, description, and language name.

SELECT f.title, f.description, l.name FROM film AS f
JOIN language AS l
ON f.language_id = l.language_id

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
CREATE TABLE new_film(
	id SERIAL UNIQUE,
	name VARCHAR (45) NOT NULL);
	
INSERT INTO new_film (name)
VALUES 
	('Titanic'),
	('Thor'),
	('Harry Potter and the Philosophers Stone');

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
CREATE TABLE customer_review(
	review_id SERIAL PRIMARY KEY,
	film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title VARCHAR(50) NOT NULL,
	score INTEGER CHECK (score BETWEEN 1 AND 10),
	review_text TEXT,
	last_update DATE NOT NULL,
	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
	FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE CASCADE);

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update)
VALUES 
((SELECT id FROM new_film where name = 'Titanic'), (SELECT language_id FROM language where name = 'English'),
'Titanic', 10, 'Very beautiful and cinematic movie with lots of classic scenes.Also extremely sad at times.Absolute 90s classic.',
'2001-08-10')

INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
VALUES 
((SELECT id FROM new_film where name = 'Thor'), (SELECT language_id FROM language where name = 'English'),
'Thor', 2, 'Christian Bale is great, Russell Crowe has a good moment, Hemsworth is good but this movie cannot be saved from a terrible script, 
 bad direction and stupid humour that overstays its welcome.','2022-07-07')
 
 -- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film WHERE name = 'Titanic'
SELECT * FROM customer_review -- 'Titanic' was deleted


Exercise 2 : DVD Rental
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE language SET name ='Russian' WHERE language_id = 7;

-- We created a new table called customer_review. Drop this table. 
-- Is this an easy step, or does it need extra checking?
DROP TABLE customer_review -- no extra checking

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT count(rental_id) FROM rental
WHERE return_date IS NULL

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT film_id, title, rental_rate FROM film
WHERE film_id IN (
SELECT film_id FROM inventory
WHERE inventory_id IN (SELECT inventory_id FROM rental
WHERE return_date IS NULL))
ORDER BY rental_rate DESC
LIMIT 30

-- Your friend is at the store, and decides to rent a movie.
-- He knows he wants to see 4 movies, but he can’t remember their names. 
-- Can you help him find which movies he wants to rent?

-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT title FROM film
WHERE description ILIKE '%sumo wrestler%' AND film_id IN (
	SELECT film_id FROM film_actor
	WHERE actor_id = (
		SELECT actor_id FROM actor 
		WHERE (first_name = 'Penelope' AND last_name = 'Monroe')))
		
-- Output: Park Citizen

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT title FROM film
WHERE length <= 60 AND film_id IN (
	SELECT film_id FROM film_category
	WHERE category_id = (
		SELECT category_id FROM category
		WHERE name = 'Documentary') AND film_id IN (
			SELECT film_id FROM film
			WHERE rating = 'R'))
			
-- Output: "Cupboard Sinners"

-- The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
	
SELECT title, rental_rate from film
WHERE rental_rate >= 4.00 AND film_id IN (
SELECT film_id FROM inventory 
WHERE inventory_id IN (
SELECT inventory_id FROM rental
WHERE (return_date >= '2005-07-28' AND return_date <= '2005-08-01'
AND customer_id = (
	SELECT customer_id FROM customer
	WHERE first_name = 'Matthew' AND last_name = 'Mahan'))))
	
-- Output: "Sugar Wonka"

-- The 4th film : His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

SELECT title, replacement_cost FROM film
WHERE (title ILIKE '%boat%' OR description ILIKE '%boat%')
AND film_id IN (SELECT film_id FROM inventory 
WHERE inventory_id IN (
SELECT inventory_id FROM rental
WHERE customer_id = (
	SELECT customer_id FROM customer
	WHERE first_name = 'Matthew' AND last_name = 'Mahan')))
ORDER BY replacement_cost DESC

-- Output: "Stone Fire" (19.99), "Money Harold" (17.99), "Masked Bubble" (12.99), "Talented Homicide" (9.99)
