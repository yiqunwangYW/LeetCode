select firstName, lastName, city, a.state
from Person p 
left join Address a 
on p.personId = a.personId ;