-- Fetch the first four students. You have to order the four students alphabetically by last_name.
SELECT last_name, first_name, birth_date 
FROM students
ORDER BY last_name ASC
LIMIT 4

--Fetch the details of the youngest student.
SELECT last_name, first_name, birth_date
FROM students
ORDER BY birth_date DESC
LIMIT 1

-- Fetch three students skipping the first two students.
SELECT first_name, last_name, birth_date
FROM students
LIMIT 3 OFFSET 2