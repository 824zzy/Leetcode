""" https://leetcode.com/problems/complement-of-base-10-integer/
use mask 11...1 and XOR to flip num
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ (1 << n.bit_length()) - 1
