""" https://leetcode.com/problems/jump-game-ii/
find maximum reach index by curr and when i larger than previous maximum index, ans += 1
"""
from header import *


class Solution:
    def jump(self, A: List[int]) -> int:
        right_most = 0
        ans = 0
        mx = 0
        for i in range(len(A)):
            if i > right_most:
                right_most = mx
                ans += 1
            mx = max(mx, i + A[i])
        return ans
