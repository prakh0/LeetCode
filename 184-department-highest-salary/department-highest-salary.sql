-- select d.name as Department,e.name as Employee ,e.salary as Salary
-- from employee e
-- join department d on e.departmentId = d.id
-- order by e.salary desc
-- limit 3

with t1 as (
    select e.departmentId, max(e.salary) salary from employee e group by e.departmentId
),
t2 as (select d.name as Department, e.name Employee,t1.salary Salary
from t1
join employee e on e.departmentid = t1.departmentid and e.salary = t1.salary 
join department d on d.id = e.departmentid)
select * from t2