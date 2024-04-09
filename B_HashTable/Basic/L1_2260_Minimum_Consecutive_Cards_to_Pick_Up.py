""" https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
use hash table to keep track of last seen card to find the minimum number of consecutive cards
"""


class Solution:
    def minimumCardPickup(self, A: List[int]) -> int:
        ans = inf
        seen = {}
        for i, c in enumerate(A):
            if c not in seen:
                seen[c] = i
            else:
                ans = min(ans, i - seen[c] + 1)
                seen[c] = i
        if ans == inf:
            return -1
        else:
            return ans
