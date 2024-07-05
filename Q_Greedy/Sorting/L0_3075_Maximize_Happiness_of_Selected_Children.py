""" https://leetcode.com/problems/maximize-happiness-of-selected-children/
reading comprehension + greedy sort
"""
from header import *


class Solution:
    def maximumHappinessSum(self, A: List[int], k: int) -> int:
        A.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += max(A[i] - i, 0)
        return ans


"""
[1,2,3]
3
[1,2,3]
2
[1,1,1,1]
2
[2,3,4,5]
1
[2,83,62]
3
"""
