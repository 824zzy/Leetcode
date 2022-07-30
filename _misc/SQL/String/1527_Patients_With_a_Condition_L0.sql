""" https://leetcode.com/problems/patients-with-a-condition/
search for two string like conditions
"""
select * 
from Patients 
where (conditions like 'DIAB1%') or (conditions like '% DIAB1%');