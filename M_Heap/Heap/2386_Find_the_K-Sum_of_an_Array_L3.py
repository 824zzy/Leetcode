""" https://leetcode.com/problems/find-the-k-sum-of-an-array/
learn from god ye: https://leetcode.com/problems/find-the-k-sum-of-an-array/discuss/2456675/Python3-priority-queue
"""
from header import *
class Solution:
    def kSum(self, A: List[int], k: int) -> int:
        mx = sum(x for x in A if x>0)
        A = sorted(abs(x) for x in A)
        pq = [(-mx, 0)]
        for _ in range(k):
            x, i = heappop(pq)
            if i<len(A):
                heappush(pq, (x+A[i], i+1))
                if i: heappush(pq, (x-A[i-1]+A[i], i+1))
        return -x