""" https://leetcode.com/problems/relative-ranks/
simulation using hash table
"""
from header import *


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        mp = {x: i for i, x in enumerate(sorted(score, reverse=True))}
        ans = []
        for s in score:
            if mp[s] == 0:
                ans.append("Gold Medal")
            elif mp[s] == 1:
                ans.append("Silver Medal")
            elif mp[s] == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(mp[s] + 1))
        return ans
