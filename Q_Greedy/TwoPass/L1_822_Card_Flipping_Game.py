""" https://leetcode.com/problems/card-flipping-game/
Essentially, it is asking to look for the smallest number which doesn't appear on front and back of the same card.
"""


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {ff for ff, bb in zip(fronts, backs) if ff == bb}
        return min((x for x in fronts + backs if x not in same), default=0)
