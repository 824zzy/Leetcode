""" https://leetcode.com/problems/minimum-processing-time/submissions/
reading comprehensive + greedy
"""
from header import *


class Solution:
    def minProcessingTime(self, P: List[int], T: List[int]) -> int:
        P.sort()
        T.sort(reverse=True)
        ans = 0
        for i in range(0, len(T), 4):
            ans = max(ans, P[i // 4] + T[i])
        return ans


"""
[8,10]
[2,2,3,1,8,7,4,5]
[10,20]
[2,3,1,2,5,8,4,3]
"""
