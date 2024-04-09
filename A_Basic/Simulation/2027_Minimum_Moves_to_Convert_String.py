""" L1: greedily remove 'X'
"""


class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s):
            if s[i] == "X":
                ans += 1
                i += 3
            else:
                i += 1
        return ans


class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = 0
        s = list(s) + ['O', 'O']
        for i in range(len(s)):
            if s[i] == 'X':
                ans += 1
                s[i + 1] = 'O'
                s[i + 2] = 'O'
        return ans
