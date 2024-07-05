""" https://leetcode.com/problems/range-product-queries-of-powers/
1. compute `powers` list by checking bit 1 in n
2. prefix product to compute the answer
"""
from header import *


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        M = 10 ** 9 + 7
        A = []
        for i in range(32):
            if n & (1 << i):
                A.append(1 << i)

        pref = list(accumulate(A, mul, initial=1))
        ans = []
        for i, j in queries:
            ans.append((pref[j + 1] // pref[i]) % M)
        return ans


"""
15
[[0,1],[2,2],[0,3]]
2
[[0,0]]
13
[[1,2],[1,1]]
919
[[5,5],[4,4],[0,1],[1,5],[4,6],[6,6],[5,6],[0,3],[5,5],[5,6],[1,2],[3,5],[3,6],[5,5],[4,4],[1,1],[2,4],[4,5],[4,4],[5,6],[0,4],[3,3],[0,4],[0,5],[4,4],[5,5],[4,6],[4,5],[0,4],[6,6],[6,6],[6,6],[2,2],[0,5],[1,4],[0,3],[2,4],[5,5],[6,6],[2,2],[2,3],[5,5],[0,6],[3,3],[6,6],[4,4],[0,0],[0,2],[6,6],[6,6],[3,6],[0,4],[6,6],[2,2],[4,6]]
"""
