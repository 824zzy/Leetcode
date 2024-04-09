""" https://leetcode.com/problems/count-the-hidden-sequences/
Compute the range of variation from differences. Compuare this range with allowed range upper - lower.
If it is within this range, then a solutions exists i.e. upper - lower - range otherwise return 0.
"""


class Solution:
    def numberOfArrays(
            self,
            differences: List[int],
            lower: int,
            upper: int) -> int:
        prefix = mn = mx = 0
        for x in differences:
            prefix += x
            mn = min(mn, prefix)
            mx = max(mx, prefix)
        return max(0, (upper - lower) - (mx - mn) + 1)
