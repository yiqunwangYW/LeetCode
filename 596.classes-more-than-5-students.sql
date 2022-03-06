with a as(
select class, count(student) students
from Courses
group by class)
select class from a where students>=5;