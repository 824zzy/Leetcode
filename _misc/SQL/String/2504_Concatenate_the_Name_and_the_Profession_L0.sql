""" https://leetcode.com/problems/concatenate-the-name-and-the-profession/description/
string concatenation and substring
"""
select person_id, concat(name, '(', substring(profession, 0, 1), ')') as name
from Person
order by 1 desc