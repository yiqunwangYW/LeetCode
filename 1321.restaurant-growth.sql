-- Write your MySQL query statement below
with a as(
    select distinct visited_on
    from Customer 
),
b as (
select a.visited_on,
sum(c.amount) amount,
round(sum(c.amount)/7,2) average_amount       
from a
join Customer c 
on c.visited_on between date_sub(a.visited_on, INTERVAL 6 DAY) and a.visited_on 
group by a.visited_on
order by a.visited_on
)
select * from b
where visited_on>= (select min(visited_on) from Customer) + 6
