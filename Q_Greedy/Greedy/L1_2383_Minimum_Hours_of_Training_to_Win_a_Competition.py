""" https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/
greedily go through each opponent, once energy or experience is exhausted, we update answer and reset energy and experience.
"""
from header import *

class Solution:
    def minNumberOfHours(self, en: int, ex: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        for x, y in zip(energy, experience):
            if en<=x:
                ans += x+1-en
                en = x+1
            if ex<=y:
                ans += y+1-ex
                ex = y+1
            en -= x
            ex += y
        return ans