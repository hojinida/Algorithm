SELECT e.employee_id, e.name, 
       manager.reports_count AS reports_count, 
       round(manager.average_age,0) AS average_age
FROM employees e
JOIN (
    SELECT reports_to AS employee_id, 
           COUNT(*) AS reports_count, 
           AVG(age) AS average_age
    FROM employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
) manager
ON e.employee_id = manager.employee_id
order by employee_id