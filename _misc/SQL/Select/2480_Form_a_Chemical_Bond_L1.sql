""" https://leetcode.com/problems/form-a-chemical-bond/description/
select two columns from one table
"""
SELECT 
    a.symbol AS metal, 
    b.symbol AS nonmetal 
FROM Elements a, Elements b 
WHERE a.type = 'Metal' AND b.type = 'Nonmetal'