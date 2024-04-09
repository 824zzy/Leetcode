""" https://leetcode.com/problems/isomorphic-strings/submissions/
the same as 290
use two hash table to check s and t with each other
"""
from header import *

# on-the-fly solution


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        i2j, j2i = {}, {}
        for i, j in zip(s, t):
            if j not in j2i:
                j2i[j] = i
            if i not in i2j:
                i2j[i] = j
            if j2i[j] != i or i2j[i] != j:
                return False
        return True


class Solution:
    def isIsomorphic(self, S: str, T: str) -> bool:
        seenS, seenT = defaultdict(list), defaultdict(list)
        for i, (s, t) in enumerate(zip(S, T)):
            seenS[s].append(i)
            seenT[t].append(i)
        return sorted(seenS.values()) == sorted(seenT.values())
