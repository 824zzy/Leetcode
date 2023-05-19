""" https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
Transform the problem to find the shortest sliding window with sum >= k,
we can use a monotonic increasing queue to maintain the prefix sum,
and try to make queue head as small(but larger than k) as possible and queue tail as large as possible.
"""
from header import *

class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        A = list(accumulate(A, initial=0))
        dq = deque()
        ans = inf
        for i in range(len(A)):
            # update ans based on head of queue
            while dq and A[i]-A[dq[0]]>=k: ans = min(ans, i-dq.popleft())
            # ensure monotonic increasing
            while dq and A[dq[-1]]>=A[i]: dq.pop()
            dq.append(i)
        return ans if ans!=inf else -1