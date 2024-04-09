""" https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
greedily assign prefix size people to a group
"""


class Solution:
    def maximumGroups(self, A: List[int]) -> int:
        n = len(A)
        prefix = 0
        while prefix < n:
            prefix += 1
            n -= prefix
        return prefix
