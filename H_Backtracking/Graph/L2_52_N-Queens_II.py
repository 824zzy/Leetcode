""" https://leetcode.com/problems/n-queens-ii/
The same as 51, but no need to save puzzle state
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0

        def dfs(i):
            if i == n:
                self.ans += 1
                return
            for j in range(n):
                if (
                    j not in seen["col"]
                    and i + j not in seen["ldiag"]
                    and i - j not in seen["rdiag"]
                ):
                    seen["col"].append(j)
                    seen["ldiag"].append(i + j)
                    seen["rdiag"].append(i - j)
                    dfs(i + 1)
                    seen["col"].pop()
                    seen["ldiag"].pop()
                    seen["rdiag"].pop()

        seen = defaultdict(list)
        dfs(0)
        return self.ans
