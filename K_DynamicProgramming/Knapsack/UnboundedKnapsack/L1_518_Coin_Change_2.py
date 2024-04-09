""" https://leetcode.com/problems/coin-change-2/
time dependent knap sack problem.
have to use j to avoid duplicate ans, otherwise E.g. n=3, coin=[1, 2]. [1, 2], [2, 1] will be calculated twice.
"""


class Solution:
    def change(self, n: int, A: List[int]) -> int:
        A.sort(reverse=True)

        @cache
        def dfs(i, n):
            if n == 0:
                return 1
            return sum(dfs(j, n - A[j])
                       for j in range(i, len(A)) if n - A[j] >= 0)

        return dfs(0, n)
