""" https://leetcode.com/problems/range-sum-query-immutable/
pre-calculate prefix sum
"""


class NumArray:
    def __init__(self, A: List[int]):
        self.prefix = list(accumulate(A, initial=0))

    def sumRange(self, l: int, r: int) -> int:
        return self.prefix[r + 1] - self.prefix[l]
