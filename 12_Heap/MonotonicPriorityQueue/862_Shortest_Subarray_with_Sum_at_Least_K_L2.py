""" https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
use deque rather than heap
"""
class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        A = list(accumulate(A, initial=0))
        dq = deque()
        ans = inf
        for i in range(len(A)):
            while dq and A[i]-A[dq[0]]>=k:
                ans = min(ans, i-dq.popleft())
            while dq and A[dq[-1]]>=A[i]: 
                dq.pop()
            dq.append(i)
        return ans if ans!=inf else -1