""" https://leetcode.com/problems/largest-local-values-in-a-matrix/
since N=100 is very small, just solve it by brute force simulation

Time complexity: O(3*3*N^2)
"""


class Solution:
    def largestLocal(self, A: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(A) - 2)] for _ in range(len(A[0]) - 2)]
        for i in range(len(A[0]) - 2):
            for j in range(len(A) - 2):
                ans[i][j] = 0
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        ans[i][j] = max(ans[i][j], A[ii][jj])
        return ans
