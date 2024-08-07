""" https://leetcode.com/problems/complement-of-base-10-integer/
use mask 11...1 and XOR to flip num
"""


class Solution:
    def findComplement(self, num: int) -> int:
        k = 0
        while 2 ** k <= num:
            k += 1
        return num ^ (2 ** k - 1)
