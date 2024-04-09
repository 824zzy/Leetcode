""" https://leetcode.com/problems/sentence-similarity/
save the similar pairs in a hash table, then compare the two sentences.
"""
from header import *


class Solution:
    def areSentencesSimilar(self,
                            s1: List[str],
                            s2: List[str],
                            similarPairs: List[List[str]]) -> bool:
        if len(s1) != len(s2):
            return False

        mp = defaultdict(set)
        for x, y in similarPairs:
            mp[x].add(y)
            mp[y].add(x)

        for x, y in zip(s1, s2):
            if x != y and x not in mp[y]:
                return False
        return True
