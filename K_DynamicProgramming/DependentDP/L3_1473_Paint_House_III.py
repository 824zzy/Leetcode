""" https://leetcode.com/problems/paint-house-iii/
Too god damn hard fxxk it
TODO: https://leetcode.com/problems/paint-house-iii/discuss/675630/Python3-top-down-dp-with-comments
Return total cost of painting 0-ith house
j - (j+1)st color
k - k neighborhoods
"""


class Solution:
    def minCost(
        self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int
    ) -> int:
        @cache
        def fn(i, j, k):

            if i < 0:
                return 0  # $0 cost before painting any house
            if k <= 0 or k > i + 1:
                return inf  # impossible to have neighborhoods <= 0 or more than houses
            if houses[i] and houses[i] != j + 1:
                # invalid if houses[i] is already painted with a different
                # color
                return inf
            prev = min(
                fn(i - 1, j, k), min(fn(i - 1, jj, k - 1) for jj in range(n) if jj != j)
            )  # cost of painting houses[:i]
            # cost of painting houses[:i+1]
            return prev + (0 if houses[i] else cost[i][j])

        ans = min(
            fn(m - 1, j, target) for j in range(n)
        )  # minimum cost of painting houses[:m]
        return ans if ans < inf else -1
