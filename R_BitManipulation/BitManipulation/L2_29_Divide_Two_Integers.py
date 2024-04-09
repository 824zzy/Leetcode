""" https://leetcode.com/problems/divide-two-integers/
The solution has a sense of greedy.
We loop bits from 31-th bit to 0-th bit. At i-th bit, we check if a>=(2^i * b),
if so, we can remove (2^i * b) from a, which also means there are b can be added 2^i time to a.
"""


class Solution:
    def divide(self, A: int, B: int) -> int:
        if (A == -2147483648 and B == -1):
            return 2147483647
        a = abs(A)
        b = abs(B)
        ans = 0
        for i in reversed(range(32)):
            if a >= b << i:
                ans += 1 << i
                a -= b << i

        if (A > 0) == (B > 0):
            return ans
        else:
            return -ans
