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
            while pq and i - pq[0][1] >= k:
                heappop(pq)
            heappush(pq, (-A[i], i))
            if i >= k - 1:
                ans.append(-pq[0][0])
        return ans


# deque implementation
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        q = deque()  # monotonic decreasing queue
        ans = []
        for i, x in enumerate(A):
            # in
            while q and A[q[-1]] <= x:
                q.pop()
            q.append(i)
            # out
            while q and i - q[0] >= k:
                q.popleft()
            if i >= k - 1:
                ans.append(A[q[0]])
        return ans
