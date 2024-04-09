""" https://leetcode.com/problems/confusing-number-ii/
dfs with x, the rotated x and digits
"""


class Solution:
    def confusingNumberII(self, n: int) -> int:
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.ans = 0

        def dfs(x, _x, d):
            if x != _x:
                self.ans += 1
            for k, v in mapping.items():
                if (x != 0 or k != 0) and x * 10 + k <= n:
                    dfs(x * 10 + k, v * d + _x, d * 10)

        dfs(0, 0, 1)
        return self.ans
