# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country, 
count(state) as trans_count, 
SUM(case When state = 'approved' then 1 else 0 end) as approved_count, 
sum(amount) as trans_total_amount, 
SUM(case When state = 'approved' then amount else 0 end) as approved_total_amount
FROM Transactions
Group BY month, country