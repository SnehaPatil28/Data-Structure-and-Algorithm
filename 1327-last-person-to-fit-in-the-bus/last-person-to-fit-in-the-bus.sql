# Write your MySQL query statement below
with Que_weight as(
    SELECT person_id, person_name, weight, turn,
    SUM(weight) OVER (ORDER BY turn) as sum_w
    FROM Queue
)

SELECT person_name 
FROM Que_weight 
WHERE sum_w <= 1000
ORDER BY turn DESC
LIMIT 1;