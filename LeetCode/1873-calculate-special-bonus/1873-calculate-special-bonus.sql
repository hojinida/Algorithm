# Write your MySQL query statement below
select employee_id, if(employee_id%2 != 0 and name not like "M%",salary*1,0) as bonus
from Employees
order by employee_id