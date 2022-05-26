""" https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
1. maintain a monotonic decreasing queue
2. update ans 
"""
class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        A = list(accumulate(A, initial=0))
        dq = deque()
        ans = inf
        for i in range(len(A)):
            # update ans based on head of queue
            while dq and A[i]-A[dq[0]]>=k: ans = min(ans, i-dq.popleft())
            # ensure monotonic decreasing
            while dq and A[dq[-1]]>=A[i]: dq.pop()
            dq.append(i)
        return ans if ans!=inf else -1