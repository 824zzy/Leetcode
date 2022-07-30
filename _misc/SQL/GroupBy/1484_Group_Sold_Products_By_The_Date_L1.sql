""" https://leetcode.com/problems/group-sold-products-by-the-date/
the challange of this problem is how to aggregate the product names in one cell. 
In MySql, this can be done using GROUP_CONCAT.
"""
select sell_date, count(distinct product) as num_sold, group_concat(distinct product order by product asc separator ',') as products
from Activities 
group by sell_date 
order by sell_date asc;