""" https://leetcode.com/problems/sliding-window-maximum/
"""
class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        if k==1: return A
        pq = [(-A[i], i) for i in range(k)]
        heapq.heapify(pq)
        ans = []
        for i in range(k-1, len(A)):
            while pq and i-pq[0][1]>=k: heapq.heappop(pq)
            heapq.heappush(pq, (-A[i], i))
            ans.append(-pq[0][0])
        return ans