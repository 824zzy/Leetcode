""" https://leetcode.com/problems/make-number-of-distinct-characters-equal/
brute force on characters
there are only two cases the answer is true:
1. if x==y and len(c1)==len(c2)
2. if x!=y, if c==1 then length -= 1, if y not in c1 then length += 1
"""
from header import *

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for x, c in c1.items():
            for y, d in c2.items():
                if x==y:
                    if len(c1)==len(c2): return True
                elif len(c1)-(c==1)+(y not in c1) == len(c2)-(d==1)+(x not in c2):
                    return True
        return False

# suboptimal solution but easy to understand
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        for x in cnt1:
            for y in cnt2:
                c1, c2 = cnt1.copy(), cnt2.copy()
                c1[x] -= 1
                c2[x] += 1
                c1[y] += 1
                c2[y] -= 1
                if not c1[x]: c1.pop(x)
                if not c2[y]: c2.pop(y)
                if len(c1)==len(c2):  
                    return True
        return False