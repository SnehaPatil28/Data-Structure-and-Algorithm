# Write your MySQL query statement below
SELECT *, IF(x+y > z and z+x > y and y+z > x, "Yes", "No") AS triangle FROM triangle