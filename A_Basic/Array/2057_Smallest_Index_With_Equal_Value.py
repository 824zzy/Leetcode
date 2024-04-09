""" L0: https://leetcode.com/problems/smallest-index-with-equal-value/
find i%10==v
"""


class Solution:
    def smallestEqual(self, A: List[int]) -> int:
        for i, v in enumerate(A):
            if i % 10 == v:
                return i
        return -1
