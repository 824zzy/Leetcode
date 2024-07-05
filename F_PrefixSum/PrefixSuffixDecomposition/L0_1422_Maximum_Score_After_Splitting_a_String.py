""" https://leetcode.com/problems/maximum-score-after-splitting-a-string/
two pass prefix suffix decomposition
"""


class Solution:
    def maxScore(self, s: str) -> int:
        suf1 = []
        suf = 0
        for i in reversed(range(len(s))):
            if s[i] == "1":
                suf += 1
            suf1.append(suf)
        suf1.reverse()

        ans = 0
        pre = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                pre += 1
            x, y = pre, suf1[i + 1]
            ans = max(ans, x + y)
        return ans
