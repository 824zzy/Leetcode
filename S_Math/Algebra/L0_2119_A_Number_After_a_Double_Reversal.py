""" https://leetcode.com/problems/a-number-after-a-double-reversal/
check 0 and mod 10
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == int(str(int(str(num)[::-1]))[::-1])
