""" https://leetcode.com/problems/single-row-keyboard/description/
simulation
"""
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mp = {c: i for i, c in enumerate(keyboard)}
        ans = 0
        cur = 0
        for c in word:
            ans += abs(cur-mp[c])
            cur = mp[c]
        return ans