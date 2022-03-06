with top3 as (
    select d.name Department_name, d.id, e.Salary, 
    DENSE_RANK() over (partition by d.name order by e.Salary desc) dept_rank
    from Employee  e
    join Department  d
    on e.departmentId =d.id
)
select distinct Department_name as Department, 
e.name as Employee , e.Salary 
from Employee e
join top3 
on top3.id= e.departmentId  and top3.Salary=e.Salary
where dept_rank<=3;