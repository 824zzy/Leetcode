""" L3: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
"""


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        M = 10**9 + 7

        def check(pos):
            return all(a != b for a, b in zip(pos, pos[1:]))

        def neighs(pos1, pos2):
            return all(a != b for a, b in zip(pos1, pos2))

        states = [''.join(pos)
                  for pos in product('RGB', repeat=m) if check(pos)]
        adj = {}
        for state in states:
            adj[state] = [
                next_state for next_state in states if neighs(
                    state, next_state)]

        @cache
        def dfs(prv_state, N):
            if N == 0:
                return 1
            return sum(dfs(next_state, N - 1)
                       for next_state in adj[prv_state]) % M

        return sum(dfs(state, n - 1) for state in states) % M
