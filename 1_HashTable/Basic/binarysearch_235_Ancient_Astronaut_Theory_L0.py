""" https://binarysearch.com/problems/Ancient-Astronaut-Theory
1. use hashmap to record corresponding index of every characters
2. use t as threshold of minimum legit index, if any of character in s smaller than t, then return False
"""
class Solution:
    def solve(self, D, s):
        mp = {c: i for i, c in enumerate(D)}
        t = 0
        for c in s:
            if c in mp:
                if t <= mp[c]: t = mp[c]
                else: break
        else: return True
        return False