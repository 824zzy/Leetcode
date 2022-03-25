""" https://leetcode.com/problems/sliding-window-maximum/
1. maintain a monotonic decreasing queue
2. pop element based on its index
"""
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        dq = deque()
        ans = []
        for i, x in enumerate(A):
            # monotonic decreasing queue
            while dq and dq[-1][1]<=x: dq.pop()
            # pop left element if its index out of window size
            while dq and dq[0][0]<=i-k: dq.popleft()
            dq.append((i, x))
            # add largest element
            if i>=k-1: ans.append(dq[0][1])
        return ans