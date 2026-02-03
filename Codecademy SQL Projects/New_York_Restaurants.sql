-- Jacob Wiltshire
-- 02/03/2026

-- View the table to understand its contents
SELECT *
FROM nomnom;

-- Find the distinct neighborhoods
SELECT DISTINCT neighborhood
FROM nomnom;

-- Find the distinct cuisine
SELECT DISTINCT cuisine
FROM nomnom;

-- Find all Chinese food options
SELECT *
FROM nomnom
WHERE cuisine = 'Chinese';

-- Return the restaurants with 4 stars and above
SELECT *
FROM nomnom
WHERE review >= 4;

-- Return restaurants that are Italian and $$$
SELECT *
FROM nomnom
WHERE cuisine = 'Italian' and price = '$$$';

-- Find the restaurant that contains 'meatball'
SELECT *
FROM nomnom
WHERE name LIKE '%meatball%';

-- Find all restaurants that are in midtown, downtown, or chinatown
SELECT *
FROM nomnom
WHERE neighborhood = 'Midtown' OR neighborhood = 'Downtown' OR neighborhood = 'Chinatown';

-- Find all the restaurants with a pending health grade
SELECT *
FROM nomnom
WHERE health IS NULL;

-- Create a top 10 restaurants ranking based on reviews
SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 10;

-- Using case, change the rating system to words rather than numbers and rename the column
SELECT name,
  CASE
    WHEN review > 4.5 THEN 'Extraordinary'
    WHEN review > 4 THEN 'Excellent'
    WHEN review > 3 THEN 'Good'
    WHEN review > 2 THEN 'Fair'
    ELSE 'Poor'
  END AS 'taste review'
FROM nomnom;

-- AI Review - Your SQL queries align with the project tasks: exploring the nomnom table, filtering by cuisine, neighborhood, price, and rating, plus a top-10 and a CASE-based rating label.
-- Good use of clear SQL keywords and straightforward queries. Minor readability tweaks could help future readers.
-- Queries are direct and index-friendly guesses likely work well on typical SQL engines. Consider a couple of small improvements for readability and robustness.