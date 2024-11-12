""" https://leetcode.com/problems/minimum-array-end/
convert the problem into:
    Given bits of n-1 (10) and x (100), integrate n-1 to the bits in x that is not 1.
"""


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        n -= 1
        for i in range(60):
            if x & (1 << i):
                continue
            if n & 1:
                ans ^= 1 << i
            n >>= 1
        return ans


"""
100
101
110

0111
1111
"""

"""
6715154
7193485
"""
