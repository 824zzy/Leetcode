""" https://leetcode.com/problems/group-anagrams/
Group anagrams by using hash table whose key is the sorted string and value is the list of anagrams.
"""
from header import *

class Solution:
    def groupAnagrams(self, A: List[str]) -> List[List[str]]:
        D = defaultdict(list)
        for x in A:
            D[tuple(sorted(x))].append(x)
        return D.values()