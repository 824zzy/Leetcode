""" L0: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
find minimum element in a prefix array
"""


class Solution:
    def minStartValue(self, A: List[int]) -> int:
        pref = list(itertools.accumulate(A))
        return max(1, -1 * min(pref) + 1)
