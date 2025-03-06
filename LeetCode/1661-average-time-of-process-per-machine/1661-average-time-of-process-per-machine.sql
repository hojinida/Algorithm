# Write your MySQL query statement below
select b.machine_id, round(avg(b.time),3) as processing_time
from 
(select a.machine_id, b.timestamp-a.timestamp as time
from Activity a
join Activity b
on a.process_id = b.process_id
and a.machine_id = b.machine_id
and a.timestamp < b.timestamp) as b
group by machine_id

