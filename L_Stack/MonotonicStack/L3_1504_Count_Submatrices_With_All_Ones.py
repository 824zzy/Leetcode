""" https://leetcode.com/problems/count-submatrices-with-all-ones/
TODO:
https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/721999/Python3-O(MN)-histogram-model
"""


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        # precipitate mat to histogram
        for i in range(m):
            for j in range(n):
                if mat[i][j] and i > 0:
                    mat[i][j] += mat[i - 1][j]  # histogram

        ans = 0
        for i in range(m):
            stack = []  # mono-stack of indices of non-decreasing height
            cnt = 0
            for j in range(n):
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    jj = stack.pop()  # start
                    kk = stack[-1] if stack else -1  # end
                    # adjust to reflect lower height
                    cnt -= (mat[i][jj] - mat[i][j]) * (jj - kk)

                cnt += mat[i][j]  # count submatrices bottom-right at (i, j)
                ans += cnt
                stack.append(j)

        return ans
