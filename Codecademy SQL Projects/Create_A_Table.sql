-- Create a table for friends
CREATE TABLE friends (id INTEGER, name TEXT, birthday DATE);

-- Add Ororo to the table with their information
INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

-- Make sure Ororo Munroe got added to the table and that the table was created
-- SELECT * FROM friends

-- Add two of my friends to the table
INSERT INTO friends (id, name, birthday)
VALUES (2, 'Sean Wiltshire', '2007-01-17');
INSERT INTO friends (id, name, birthday)
VALUES (3, 'Tyler Wiltshire', '2000-05-04');

-- Change Ororo's name to storm
UPDATE friends
SET name = 'Storm'
WHERE id = 1;

-- Add a new column for email
ALTER TABLE friends
ADD COLUMN email TEXT;

-- Update Storm's email
UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

-- Update Sean's email
UPDATE friends
SET email = 'seanwiltshire17@gmail.com'
WHERE id = 2;

-- Update Tyler's email
UPDATE friends
SET email = 'tylerwiltshire15@gmail.com'
WHERE id = 3;

-- Delete Storm from the friends table
DELETE FROM friends
WHERE id = 1;

-- Get the result of the final friends table
SELECT * FROM friends

-- AI Review - Your code creates a friends table, inserts Ororo Munroe (later renamed Storm) and two friends, adds an email column, updates emails, and prints the final table. It follows the task sequence and uses standard SQL syntax.
-- The final output aims to show the end state of the table after all operations. It should reflect two remaining rows (Storm with email, plus Sean and Tyler if not deleted).
-- The SQL statements are mostly straightforward and in logical order (CREATE, INSERT, UPDATE, ALTER, DELETE, SELECT).
-- Operations are executed sequentially as exercises; performance concerns are minimal for this task.
-- Redundant checks: ensure you SELECT after major changes to verify state. Consider separating tasks into individual scripts for clarity.