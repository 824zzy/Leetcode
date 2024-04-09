""" https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
1. initialize a heap for the first row, each element is [A[0]+B[j], 0, j]
2. pop the smallest pair from the heap, say [A[i]+B[j], i, j]
3. if i+1<m, push [A[i+1]+B[j], i+1, j] to the heap
"""
from header import *


class Solution:
    def kSmallestPairs(self,
                       A: List[int],
                       B: List[int],
                       k: int) -> List[List[int]]:
        m, n = len(A), len(B)
        ans = []
        pq = [[A[0] + B[j], 0, j] for j in range(n)]
        heapify(pq)
        for _ in range(min(k, m * n)):
            _, i, j = heappop(pq)
            ans.append([A[i], B[j]])
            if i + 1 < m:
                heappush(pq, [A[i + 1] + B[j], i + 1, j])
        return ans


"""
[1,7,11]
[2,4,6]
3
[1,1,2]
[1,2,3]
2
[1,2]
[3]
3
[1,1,2]
[1,2,3]
10
[1,2,4,5,6]
[3,5,7,9]
3
"""
