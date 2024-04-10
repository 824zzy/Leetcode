""" https://leetcode.com/problems/reveal-cards-in-increasing-order/
simulation while keeping track of indices
"""
from header import *


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = [0]*len(deck)
        idx = deque(range(len(deck)))
        for x in sorted(deck):
            ans[idx.popleft()] = x
            if idx:
                idx.append(idx.popleft())
        return ans
