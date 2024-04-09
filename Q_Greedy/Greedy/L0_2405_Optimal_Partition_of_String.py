""" https://leetcode.com/problems/optimal-partition-of-string/
greedily find the longest non-duplicated substring by set.
"""


class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        ans = 0

        for i in range(len(s)):
            if s[i] in seen:
                seen = set()
                ans += 1
            seen.add(s[i])
        return ans + 1
