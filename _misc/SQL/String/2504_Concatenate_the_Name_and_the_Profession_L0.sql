""" https://leetcode.com/problems/concatenate-the-name-and-the-profession/description/
string concatenation and substring
"""
SELECT 
    person_id, 
    CONCAT(name, "(", LEFT(profession, 1), ")") AS name
FROM Person
ORDER BY 1 DESC