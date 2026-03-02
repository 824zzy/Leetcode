""" https://leetcode.com/problems/toggle-light-bulbs/
Toggling a bulb twice cancels out. A bulb is on iff it appears an odd number
of times. Count occurrences with Counter, return sorted odd-count keys.
"""


class Solution:
    def toggleLightBulbs(self, A: list[int]) -> list[int]:
        return sorted([k for k, v in Counter(A).items() if v & 1])
