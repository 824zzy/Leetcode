""" https://leetcode.com/problems/bank-account-summary-ii/
join the two tables and group by the account_id
"""
select name, sum(amount) as balance
from Users u
left join Transactions t
on u.account=t.account
group by name
having balance>10000;