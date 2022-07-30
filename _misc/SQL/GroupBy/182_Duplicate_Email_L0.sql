""" https://leetcode.com/problems/duplicate-emails/
use groupby-count to find duplicate emails.
"""
select email as Email 
from Person 
group by email 
having count(email)>1;