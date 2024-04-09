""" https://leetcode.com/problems/longest-cycle-in-a-graph/
copy from dafu: https://leetcode.com/problems/longest-cycle-in-a-graph/discuss/2357799/Python-short-cycle-detection-code-learned-from-problem-1192
"""
from header import *


class Solution:
    def longestCycle(self, E: List[int]) -> int:
        n = len(E)
        seen = set()
        low = [inf] * n

        def dfs(i, step):
            if i in seen or E[i] == -1:
                return -1
            if low[i] < step:
                return step - low[i]
            low[i] = step
            ans = dfs(E[i], step + 1)
            seen.add(i)
            return ans

        return max([dfs(i, 0) for i in range(n)])
