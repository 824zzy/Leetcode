""" https://leetcode.com/problems/smallest-integer-divisible-by-k/
remove even number and multiple of 5 then greedily find n
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k & 1 == 0 or k % 5 == 0:
            return -1
        x = 1
        while x % k != 0:
            x = x * 10 + 1
        return len(str(x))
