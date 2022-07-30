""" https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
left join + group by
"""
select customer_id, count(Visits.visit_id) as count_no_trans
from Visits
left join Transactions on Visits.visit_id=Transactions.visit_id
where Transactions.visit_id is NULL
group by customer_id;