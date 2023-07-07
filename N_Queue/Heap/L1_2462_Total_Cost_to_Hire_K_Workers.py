""" https://leetcode.com/problems/total-cost-to-hire-k-workers/description/
greedily find the minimum cost of hiring k workers using heap
"""
from header import *

class Solution:
    def totalCost(self, A: List[int], k: int, c: int) -> int:
        n = len(A)
        A = [[A[i], i] for i in range(n)]
        Q = []
        for i in range(c):
            if A:
                Q.append(A.pop(0)+['l'])
            if A:
                Q.append((A.pop()+['r']))
        heapify(Q)
        ans = 0
        for _ in range(k):
            x, _, y = heappop(Q)
            ans += x
            if A:
                if y=='l':
                    heappush(Q, A.pop(0)+['l'])
                else:
                    heappush(Q, A.pop()+['r'])
        return ans