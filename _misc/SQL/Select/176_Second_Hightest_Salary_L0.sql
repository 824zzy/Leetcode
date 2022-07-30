""" https://leetcode.com/problems/second-highest-salary/
select maximum of maximum
"""
select max(salary) as SecondHighestSalary
from Employee
where salary<(select max(salary) from Employee);


-- or use limit with offset
(select distinct(salary) as SecondHighestSalary
from Employee
order by salary desc
limit 1, 1)
union
(select NULL)
limit 1;