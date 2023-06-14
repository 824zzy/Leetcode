""" https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
Similar to 2731: Movement of Robots
The ants change their way when they meet is equivalent to continue moving without changing their direction.
"""
from header import *

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = max(left, default=0)
        for r in right:
            ans = max(ans, n-r)
        return ans