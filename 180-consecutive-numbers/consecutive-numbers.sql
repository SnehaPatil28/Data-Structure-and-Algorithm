# Write your MySQL query statement below
WITH consecutive_num AS (
    SELECT num, LEAD(num, 1) OVER(ORDER BY id) AS next_num,
    LEAD(num, 2) OVER(ORDER BY id) AS prev_num
    FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums FROM consecutive_num WHERE prev_num = num and next_num =num