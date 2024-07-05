""" https://leetcode.com/problems/find-duplicate-file-in-system/
hash table + string
"""
from header import *


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for path in paths:
            P = path.split(" ")
            for i in range(1, len(P)):
                fname, s = P[i].split("(")
                mp[s].append("/".join([P[0], fname]))

        return [v for _, v in mp.items() if len(v) > 1]
