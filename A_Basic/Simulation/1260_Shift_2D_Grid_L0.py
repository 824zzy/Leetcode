""" https://leetcode.com/problems/shift-2d-grid/
1. make a copy of A and elements
2. reindex the copy
"""
class Solution:
    def shiftGrid(self, A: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(A), len(A[0])
        k %= M*N
        vals = [A[i][j] for i in range(M) for j in range(N)]
        ans = A

        for idx in range(M*N):
            i, j = idx//N, idx%N
            ans[i][j] = vals[idx-k]
        return ans