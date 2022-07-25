""" https://leetcode.com/problems/delete-duplicate-emails/
1. deleted records by temporarily creating a table with the ids to be deleted
2. use multi-table to match rows to be deleted
"""
delete from Person where id not in (
    select tmp.id from (
        select min(id) as id from Person group by email
    ) as tmp
)

delete p1 from Person p1, Person p2 where p1.email=p2.email and p1.id>p2.id;