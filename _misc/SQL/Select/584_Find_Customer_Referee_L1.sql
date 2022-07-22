""" https://leetcode.com/problems/find-customer-referee/
referee_id 
"""
select name 
from Customer 
where referee_id!=2 or referee_id is null;