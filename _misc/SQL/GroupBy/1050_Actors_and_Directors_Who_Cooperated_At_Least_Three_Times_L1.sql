""" https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
group by two conditions
"""
select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(*)>=3;