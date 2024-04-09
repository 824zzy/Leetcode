""" https://leetcode.com/problems/single-number-ii/
Perform bit-by-bit summation and modulo each bit sum by 3.
"""


class Solution:
    def singleNumber(self, A: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for x in A:
                cnt += (x >> i) & 1
            ans |= (cnt % 3) << i
        return ans - 2**32 if ans >= 2**31 else ans
