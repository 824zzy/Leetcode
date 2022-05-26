""" https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
Maintain a monotonic priority queue to find the minimum range, 
in other words, pop pq while the prefix range sum larger or equal than k.

Also, 

pq[0]
"""
class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        A = list(accumulate(A, initial=0))
        pq = []
        ans = inf
        for i in range(len(A)):
            # pop pq while the prefix range sum larger or equal than k
            while pq and A[i]-pq[0][0]>=k: 
                ans = min(ans, i-pq[0][1])
                heappop(pq)
            heappush(pq, (A[i], i))
        return ans if ans!=inf else -1