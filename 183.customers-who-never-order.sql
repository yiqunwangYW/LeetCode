select c.name Customers
from Customers c
where c.id not in (select customerId from Orders );
