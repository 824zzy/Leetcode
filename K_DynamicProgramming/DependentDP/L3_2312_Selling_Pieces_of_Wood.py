""" https://leetcode.com/problems/selling-pieces-of-wood/
3D DP: cut across all possible height or width of the piece.
For saving time, we only need to try i / 2 and j / 2 cuts because of the symmetry property.



Time complexity: O(n^3)
"""


class Solution:
    def sellingWood(self, m: int, n: int, A: List[List[int]]) -> int:
        mp = defaultdict(int)
        for i, j, k in A:
            mp[(i, j)] = k

        @cache
        def dp(i, j):
            if i == 0 or j == 0:
                return 0

            ans = mp[(i, j)]
            # cut through width
            for k in range(1, j // 2 + 1):
                ans = max(ans, dp(i, k) + dp(i, j - k))
            # cut through height
            for k in range(1, i // 2 + 1):
                ans = max(ans, dp(k, j) + dp(i - k, j))
            return ans

        return dp(m, n)
