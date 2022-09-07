""" https://leetcode.com/problems/sliding-window-maximum/
define a monotonic queue state as (idx, val) and we want to ensure
1. current index is within the window size
2. val is in descending order
"""
from header import *

# heap implementation
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        pq = []
        ans = []
        for i in range(len(A)):
            while pq and i-pq[0][1]>=k: heappop(pq)
            heappush(pq, (-A[i], i))
            if i>=k-1: ans.append(-pq[0][0])
        return ans


# deque implementation
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i, x in enumerate(A):
            while dq and dq[0][0]<=i-k: dq.popleft()
            while dq and dq[-1][1]<=x: dq.pop()
            dq.append((i, x))
            if i>=k-1: ans.append(dq[0][1])
        return ans