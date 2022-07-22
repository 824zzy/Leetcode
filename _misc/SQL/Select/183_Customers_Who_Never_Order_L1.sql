""" https://leetcode.com/problems/customers-who-never-order/
"""
-- use `in` statement:
select c.name as Customers
from Customers c
where c.id not in (
    select o.customerid from Orders o
);

-- or use `left join` statement:
select c.name as Customers from Customers c
left join Orders o on c.id=o.customerId
where o.customerId is null;