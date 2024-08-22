""" https://leetcode.com/problems/number-complement/
use mask 11...1 and XOR to flip num
"""


class Solution:
    def findComplement(self, n: int) -> int:
        return n ^ (1 << n.bit_length()) - 1
