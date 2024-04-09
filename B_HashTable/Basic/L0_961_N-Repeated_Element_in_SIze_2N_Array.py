""" https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
find the element whose frequency equals to len(A)//2
"""


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for k, v in Counter(A).items():
            if v == len(A) // 2:
                return k
