""" https://leetcode.com/problems/sliding-window-maximum/
1. maintain a monotonic decreasing queue
2. pop element based on its index
"""
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        pq = []
        ans = []
        for i in range(len(A)):
            while pq and i-pq[0][1]>=k: heappop(pq)
            heappush(pq, (-A[i], i))
            if i>=k-1: ans.append(-pq[0][0])
        return ans