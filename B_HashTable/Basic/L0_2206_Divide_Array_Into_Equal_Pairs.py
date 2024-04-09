""" https://leetcode.com/problems/divide-array-into-equal-pairs/
check if all the frequencies are even
"""


class Solution:
    def divideArray(self, A: List[int]) -> bool:
        for k, v in Counter(A).items():
            # if frequency is odd
            if v & 1:
                return False
        return True
