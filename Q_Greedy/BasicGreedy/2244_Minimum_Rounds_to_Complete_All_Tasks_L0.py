""" https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
1. it is not possible to complete all the tasks if there is any task appears only once.
2. greedily assign 3 level tasks as much as possible
"""
from header import *

class Solution:
    def minimumRounds(self, A: List[int]) -> int:
        cnt = Counter(A)
        ans = 0
        for _, v in cnt.items():
            if v==1: return -1
            ans += ceil(v/3)
        return ans