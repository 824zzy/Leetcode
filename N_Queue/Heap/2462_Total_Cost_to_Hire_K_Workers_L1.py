""" https://leetcode.com/problems/total-cost-to-hire-k-workers/description/
1. maintain two heaps by two pointers
2. greedily find the minimum cost of hiring k workers
"""
from header import *

class Solution:
    def totalCost(self, A: List[int], k: int, cnt: int) -> int:
        if 2*cnt>=len(A): return sum(sorted(A)[:k])

        l, r = cnt, len(A)-cnt-1
        lheap, rheap = A[:l], A[r+1:]
        heapify(lheap)
        heapify(rheap)
        
        ans = 0
        while l<=r and k:
            if lheap[0]<=rheap[0]:
                ans += heappop(lheap)
                heappush(lheap, A[l])
                l += 1
            else:
                ans += heappop(rheap)
                heappush(rheap, A[r])
                r -= 1
            k -= 1
        return ans+sum(sorted(lheap+rheap)[:k])