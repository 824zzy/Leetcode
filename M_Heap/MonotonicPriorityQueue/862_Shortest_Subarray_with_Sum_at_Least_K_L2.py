""" https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
1. maintain a monotonic priority queue
2. update pq by top values
3. update ans by index
"""
class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        A = list(accumulate(A, initial=0))
        pq = []
        ans = inf
        for i in range(len(A)):
            # update pq by top values
            while pq and A[i]-pq[0][0]>=k: 
                # update ans by index
                ans = min(ans, i-pq[0][1])
                heappop(pq)
            heappush(pq, (A[i], i))
        return ans if ans!=inf else -1