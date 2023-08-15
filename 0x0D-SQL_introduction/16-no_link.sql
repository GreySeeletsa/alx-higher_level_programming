-- script that lists all records of the table
SELECT score, name FROM second_table HAVING name IS NOT NULL ORDER BY score DESC;
