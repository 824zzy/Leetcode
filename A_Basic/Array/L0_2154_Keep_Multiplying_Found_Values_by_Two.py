""" https://leetcode.com/problems/keep-multiplying-found-values-by-two/
"""


class Solution:
    def findFinalValue(self, A: List[int], x: int) -> int:
        while x in A:
            x *= 2
        return x
