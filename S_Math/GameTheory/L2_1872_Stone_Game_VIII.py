""" https://leetcode.com/problems/stone-game-viii/
TODO: from https://leetcode.com/problems/stone-game-viii/discuss/1225850/Python3-top-down-dp
"""


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        A = list(accumulate(stones, initial=0))

        @cache
        def dp(i):
            if i + 1 == len(stones):
                return A[-1]
            return max(dp(i + 1), A[i + 1] - dp(i + 1))

        return dp(1)
