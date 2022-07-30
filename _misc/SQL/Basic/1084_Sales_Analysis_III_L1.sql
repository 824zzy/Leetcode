""" https://leetcode.com/problems/sales-analysis-iii/
"""
select p.product_id, p.product_name
from Product p
right join Sales s
on p.product_id=s.product_id
group by product_id
having "2019-01-01"<=date(min(sale_date)) and 
        date(max(sale_date))<='2019-03-31';