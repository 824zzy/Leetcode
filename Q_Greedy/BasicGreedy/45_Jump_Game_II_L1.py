""" https://leetcode.com/problems/jump-game-ii/
find maximum reach index by curr and when i larger than previous maximum index, ans += 1
"""
from header import *

class Solution:
    def jump(self, A: List[int]) -> int:
        ans = pre = cur = 0
        for i, x in enumerate(A):
            if pre<i:
                ans, pre = ans+1, cur
            cur = max(cur, i+x)
        return ans