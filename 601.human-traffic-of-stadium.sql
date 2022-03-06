with f as (
    select s1.visit_date d1, s2.visit_date d2, s3.visit_date d3 
    from Stadium s1
    join Stadium s2 on s1.id+1=s2.id
    join Stadium s3 on s2.id+1=s3.id
    where s1.people>=100 and s2.people>=100 and s3.people>=100
)
select * from Stadium
where visit_date in (select d1 from f)
or visit_date in ( select d2 from f)
or visit_date in ( select d3 from f);