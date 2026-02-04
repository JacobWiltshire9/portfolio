 -- Jacob Wiltshire
 -- 02/04/2026
 
 -- See the hacker news table and get the top 5 stories
SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

-- Find the total score of all the stories
SELECT SUM(score)
FROM hacker_news;

-- Find the users that havre gotten a combined score of 200 and their combined scores
SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

--  Add the scores of the users and divide them by the total to get the percentage
SELECT ROUND((517 + 309 + 304 + 282) / 6366.0, 2);

-- Find out how many user have been victim to Rick Rolling
SELECT user, COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY 1
ORDER BY 2 DESC;

-- Catergorize each story based on their source
SELECT CASE
   WHEN url LIKE '%github%' THEN 'GitHub'
   WHEN url LIKE '%medium.com%' THEN 'Medium'
   WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;

-- Find what time is best for posting
SELECT strftime('%H', timestamp) AS 'Hour', 
   ROUND(AVG(score), 2) AS 'Average Score',
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp is NOT NULL
GROUP BY 1
ORDER BY 2 DESC;

-- AI Review - Your code demonstrates an understanding of the Hacker News analytics tasks: pulling top stories, aggregating scores by user, and exploring sources and posting times. It shows correct SQL structure for many tasks.
-- The queries are mostly readable but some names and grammar in comments could be improved.
-- Good use of comments and straightforward SQL; consider consistent casing and alignments for readability.
-- Some identifiers use mixed case and underscores inconsistently; prefer camelCase or snake_case consistently based on project/style guide.
-- Overall performance looks fine; some tasks hard-code values where you can compute from data for accuracy.