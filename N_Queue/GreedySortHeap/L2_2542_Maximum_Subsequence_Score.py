""" https://leetcode.com/problems/maximum-subsequence-score/
the same as 857. Minimum Cost to Hire K Workers

1. Greedily sort A by their nums2 from largest to smallest
2. Greedily update the answer using heap
"""
from header import *

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        A = list(zip(nums1, nums2))
        A.sort(key=lambda x: -x[1])
        pq = [x for x, _ in A[:k]]
        heapify(pq)
        sm = sum(pq)
        ans = sm*A[k-1][1]
        for a, b in A[k:]:
            x = heappop(pq)
            sm -= x
            heappush(pq, a)
            sm += a
            ans = max(ans, sm*b)
        return ans