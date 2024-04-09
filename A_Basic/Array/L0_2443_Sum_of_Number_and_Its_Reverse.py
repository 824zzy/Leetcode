""" https://leetcode.com/problems/sum-of-number-and-its-reverse/
brute force
"""


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for x in range(num + 1):
            if int(str(x)) + int(str(x)[::-1]) == num:
                return True
        return False
