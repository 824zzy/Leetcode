""" https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
Data structure optimized DP, learn from: https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/solution/dong-tai-gui-hua-you-hua-pythonjavacgo-b-axv0/
"""
from header import *


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i, j))  # 相同元素放在同一组，统计位置

        ans = 0
        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in sorted(g.items(), key=lambda p: p[0]):
            # 先把最大值算出来，再更新 row_max 和 col_max
            mx = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            ans = max(ans, max(mx))
            for (i, j), f in zip(pos, mx):
                row_max[i] = max(row_max[i], f)  # 更新第 i 行的最大 f 值
                col_max[j] = max(col_max[j], f)  # 更新第 j 列的最大 f 值
        return ans
