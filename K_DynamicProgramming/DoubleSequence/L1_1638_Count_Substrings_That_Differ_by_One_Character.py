""" https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
sum the number of substrings ending at s[i] and t[j] with k=0/1 difference.
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        @cache
        def dfs(i, j, diff):
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1, diff) + (diff == 0)
            elif diff == 0:
                return 0
            else:
                return 1 + dfs(i - 1, j - 1, 0)

        return sum(dfs(i, j, 1) for i in range(len(s)) for j in range(len(t)))
