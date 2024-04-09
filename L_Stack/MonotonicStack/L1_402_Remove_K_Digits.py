""" https://leetcode.com/problems/remove-k-digits/
1. maintain a monotonic increasing stack for finding the smalllest possible integer
2. the poped element count reach to k then stop poping
3. the answer will be the first least elements leave in the stask
"""


class Solution:
    def removeKdigits(self, A: str, k: int) -> str:
        if k >= len(A):
            return '0'

        stk = []
        for i, x in enumerate(A):
            while stk and stk[-1] > x and k:
                stk.pop()
                k -= 1
            stk.append(x)
        return str(int(''.join(stk[:-k or None])))
