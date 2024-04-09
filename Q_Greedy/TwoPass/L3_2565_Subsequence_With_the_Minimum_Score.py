""" https://leetcode.com/problems/subsequence-with-the-minimum-score/
TODO:
"""


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        suffix = [-1] * len(s)
        j = len(t) - 1
        for i in reversed(range(len(s))):
            if 0 <= j and s[i] == t[j]:
                j -= 1
            suffix[i] = j
        ans = j + 1
        j = 0
        for i, ch in enumerate(s):
            ans = min(ans, max(0, suffix[i] - j + 1))
            if j < len(t) and s[i] == t[j]:
                j += 1
        return min(ans, len(t) - j)
