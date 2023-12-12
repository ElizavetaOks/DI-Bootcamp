SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL)
-- Output 0

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5)
-- Output 2

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab)
-- Output 0

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- Output 2