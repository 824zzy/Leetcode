""" https://leetcode.com/problems/jump-game-vi/
Let dp[i] (mx_score) the maximum score you can get when you arrive at A[i], and transform the problem into: find the k-size sliding window maximum of dp array
"""
from header import *


class Solution:
    def maxResult(self, A: List[int], k: int) -> int:
        dq = deque([(0, A[0])])
        for i in range(1, len(A)):
            while dq and i - dq[0][0] > k:
                dq.popleft()
            mx_score = dq[0][1] + A[i]
            while dq and dq[-1][1] < mx_score:
                dq.pop()
            dq.append((i, mx_score))
        return dq[-1][1]
