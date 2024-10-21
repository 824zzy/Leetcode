""" https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
backtracking template
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def dfs(i):
            if i == len(s):
                return len(seen)
            ans = 0
            for j in range(i, len(s)):
                if s[i : j + 1] not in seen:
                    seen.add(s[i : j + 1])
                    ans = max(ans, dfs(j + 1))
                    seen.remove(s[i : j + 1])
            return ans

        return dfs(0)
