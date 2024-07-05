""" https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
Solution 1: XOR and count "1"
Solution 2: compare bit by bit
"""


class Solution:
    def minBitFlips(self, S: int, G: int) -> int:
        return bin(S ^ G).count("1")


class Solution:
    def minBitFlips(self, s: int, g: int) -> int:
        ans = 0
        while s or g:
            s, ss = divmod(s, 2)
            g, gg = divmod(g, 2)
            if ss != gg:
                ans += 1
        return ans
