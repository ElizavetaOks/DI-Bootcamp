-- Use SQL to get the following from the database:
-- 1.All items, ordered by price (lowest to highest).
SELECT * FROM items
ORDER BY price

-- 2.Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT * FROM items
WHERE price >= 80
ORDER BY price DESC

-- 3.The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
SELECT name, last_name FROM customers
ORDER BY name

-- 4.All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT last_name FROM customers
ORDER BY last_name DESC