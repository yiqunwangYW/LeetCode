select min(request_at) Day,
round(cast(sum(case when status like '%cancelled%' then 1 else 0 end) as decimal)/
      count(*), 2) 'Cancellation Rate'
from Trips 
where client_id not in 
  (select users_id from Users where role='client' and banned ='Yes')
  and driver_id not in
  (select users_id from Users where role='driver' and banned ='Yes')
  and request_at>="2013-10-01" and request_at<="2013-10-03"
group by request_at;