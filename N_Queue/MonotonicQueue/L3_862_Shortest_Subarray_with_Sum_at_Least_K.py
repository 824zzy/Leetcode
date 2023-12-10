""" https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
Transform the problem to find the shortest sliding window with sum >= k,
we can use a monotonic increasing queue to maintain the prefix sum,
and try to make queue head as small(but larger than k) as possible and queue tail as large as possible.
"""
from header import *

class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        A = list(accumulate(A, initial=0))
        q = deque()
        ans = inf
        for i in range(len(A)):
            # in: ensure monotonic increasing
            while q and A[q[-1]]>=A[i]:
                q.pop()
            q.append(i)
            # out: pop when the window sum larger than k
            while q and A[i]-A[q[0]]>=k:
                ans = min(ans, i-q[0])
                q.popleft()
        return ans if ans!=inf else -1