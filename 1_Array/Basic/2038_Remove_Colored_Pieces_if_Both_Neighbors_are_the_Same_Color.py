""" L0: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
groupby the colors and count triple "A" or "B"
"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        L = [(k, len(list(v))) for k, v in itertools.groupby(colors)]
        Alice, Bob = 0, 0
        for k, v in L:
            if v>2:
                if k=='A': Alice += v-2
                else: Bob += v-2
        return Alice>Bob