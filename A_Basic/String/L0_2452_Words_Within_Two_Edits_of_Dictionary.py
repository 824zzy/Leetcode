""" https://leetcode.com/problems/words-within-two-edits-of-dictionary/
"""
from header import *

# brute force
class Solution:
    def twoEditWords(self, Q: List[str], D: List[str]) -> List[str]:
        ans = []
        for q in Q:
            for d in D:
                diff = sum([1 for c1, c2 in zip(q, d) if c1!=c2])
                if diff<=2:
                    ans.append(q)
                    break
        return ans
                