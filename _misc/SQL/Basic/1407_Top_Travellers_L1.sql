""" https://leetcode.com/problems/top-travellers/
use ifnull to replace null with 0
"""
select name, ifnull(sum(distance), 0) as travelled_distance
from Rides r
right join Users u
on r.user_id=u.id
group by user_id
order by travelled_distance desc, name asc;