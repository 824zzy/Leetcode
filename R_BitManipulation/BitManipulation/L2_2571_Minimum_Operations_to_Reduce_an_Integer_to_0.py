""" https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/
"""


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n & 1 == 0:
                # 10
                n >>= 1
            elif n & 2 > 0:
                # 11
                n += 1
                ans += 1
            else:
                # 101
                n >>= 2
                ans += 1
        return ans


"""
39
54
"""
