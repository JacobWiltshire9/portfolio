-- Jacob Wiltshire
-- 02/06/2026

-- Examine the 3 tables
SELECT * FROM trips;
SELECT * FROM riders;
SELECT * FROM cars;

-- Cross join between riders and cars
SELECT riders.first,
   riders.last,
   cars.model
FROM riders, cars;

-- Left join riders and trips
SELECT trips.date, 
   trips.pickup, 
   trips.dropoff, 
   trips.type, 
   trips.cost,
   riders.first, 
   riders.last,
   riders.username
FROM trips
LEFT JOIN riders 
  ON trips.rider_id = riders.id;

-- Inner join trips and cars
SELECT *
FROM trips
JOIN cars
  ON trips.car_id = cars.id;

-- stack riders and riders2
SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

-- Find the average cost of the trip
SELECT ROUND(AVG(cost),2)
FROM trips;

-- Find riders that have used lyft less than 500 times
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

-- Calculate the number of cars that are active
SELECT COUNT(*)
FROM cars
WHERE status = 'active';

-- Find which two cars have the highest trips completed
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;

-- AI Review -Your code demonstrates key SQL tasks from the Lyft Trip Data project: selecting from three tables, performing joins (LEFT and INNER), stacking with UNION, aggregating (AVG), filtering, counting, and ranking top cars. It shows practical usage of cross joins and joins across multiple tables to create a trip log and insights.
-- Compliment: You used multiple join types to integrate data across tables, showing understanding of LEFT and INNER joins.
-- Suggestion: Add explicit table aliases and consistent indentation to improve readability and reduce ambiguity.
-- Compliment: Your queries cover key performance tasks like aggregation (AVG) and counting, which are efficient for insight generation.
-- Suggestion: Prefer explicit column lists over SELECT * in production queries to reduce I/O and improve performance; also use proper JOIN syntax over implicit cross joins unless intended.