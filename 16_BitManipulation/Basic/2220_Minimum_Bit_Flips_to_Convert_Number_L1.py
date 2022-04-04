""" https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
XOR and count "1"
"""
class Solution:
    def minBitFlips(self, S: int, G: int) -> int:
        return bin(S^G).count('1')

class Solution:
    def minBitFlips(self, S: int, G: int) -> int:
        ans = 0
        for s, g in zip_longest(bin(S)[2:].zfill(32), bin(G)[2:].zfill(32)):
            if s!=g: ans += 1
        return ans