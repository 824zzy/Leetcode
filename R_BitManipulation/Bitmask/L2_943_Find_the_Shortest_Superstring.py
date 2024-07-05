""" https://leetcode.com/problems/find-the-shortest-superstring/
TSP(travel salesman problem) problem
1. pre-compute the y's difference of x and y
2. dp to find shortest path from any word to all the other words.
"""


class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        def y_diff(x, y):
            for i in reversed(range(len(x) + 1)):
                if x[-i:] == y[:i]:
                    return y[i:]
            return y

        N = len(A)
        G = [[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                if i != j:
                    G[i][j] = y_diff(A[i], A[j])

        @cache
        def dp(mask, i):
            if mask == (1 << N) - 1:
                return ""
            ans = "0" * 240
            for j in range(len(A)):
                if not mask & (1 << j):
                    ans = min(ans, G[i][j] + dp(mask ^ (1 << j), j), key=len)
            return ans

        return min([A[i] + dp(1 << i, i) for i in range(len(A))], key=len)
