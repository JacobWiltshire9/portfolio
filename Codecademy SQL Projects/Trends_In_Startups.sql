-- Jacob Wiltshire
-- 02/02/2026

-- Analyze the startups table
SELECT *
FROM startups;

-- Calculate the total number of companies in the table
SELECT COUNT(*)
FROM startups;

-- Get the toal value of all companies in the table
SELECT SUM(valuation)
FROM startups;

-- Find the highest amount raised by a startup in the seed stage
SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

-- Find the year in which the oldest company was founded
SELECT MIN(founded)
FROM startups;

-- Return the average valuation
SELECT AVG(valuation)
FROM startups;

-- Return the average valuation in each category
SELECT category, AVG(valuation)
FROM startups
GROUP BY category;

-- Return the average valuation in each category rounding to 2 decimal places
SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category;

-- Return the average valuation in each category rounding to 2 decimal places and order the list from the highest averages to the lowest
SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY 1
ORDER BY 2 DESC;

-- Return the name of each category and the total number of companies that belong to it
SELECT category, COUNT(*)
FROM startups
GROUP BY category;

-- Put the top 3 markets in order
SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3
ORDER BY 2 DESC;

-- Find the average size of a startup in each location
SELECT location, AVG(employees)
FROM startups
GROUP BY location;

-- Find the avaerage size of a startup in each location with average sizes being above 500
SELECT location, AVG(employees)
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;

-- AI Review - Your code implements the intended SQL tasks by using aggregate functions to summarize the startups table. It covers counts, sums, max, min, averages, grouping, rounding, and basic filtering.
-- The queries align with the project goals to analyze valuations, counts per category, and location-based statistics.
-- Nice use of clear SQL structure and comments to outline each task. The indentation makes the logic easy to follow.
-- Consider aligning casing and spacing for consistency (e.g., uppercase SQL keywords).
-- Add brief inline comments for non-obvious logic to improve maintainability.
-- You’ve effectively used aggregate functions with GROUP BY and HAVING for filtering, which is efficient for these tasks.
-- Where applicable, reuse computed values to avoid repeated scans (e.g., compute AVG and then reuse in ORDER BY).