with e as (
    select email Email,
    row_number() over(partition by email) email_count
    from Person
)
select distinct Email from e 
where email_count >1;