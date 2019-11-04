""" Facebook
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1, c2 = Counter(s), Counter(t)
        return c1==c2

# 3/*/2019
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d, t_d = {}, {}
        for c in s:
            if c not in s_d.keys():
                s_d[c] = 1
            else:
                s_d[c] += 1
            
        for c in t:
            if c not in t_d.keys():
                t_d[c] = 1
            else:
                t_d[c] += 1
        
        if s_d == t_d:
            return True
        else:
            return False
        
        