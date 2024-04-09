""" https://leetcode.com/problems/wildcard-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            elif i == len(s) and set(p[j:]) == {'*'}:
                return True
            elif i == len(s) or j == len(p):
                return False

            if s[i] == p[j] or p[j] == '?':
                return dfs(i + 1, j + 1)
            elif p[j] == '*':
                return dfs(i, j + 1) or (i < len(s) and dfs(i + 1, j))
            else:
                return False

        return dfs(0, 0)
