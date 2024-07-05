""" https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/
1. only focus on the different part
2. three options for each different digit
"""
from header import *


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        A = [i for i, (x, y) in enumerate(zip(s1, s2)) if x != y]

        @cache
        def dp(i, can_flip):
            if i == len(A):
                if can_flip == 0:
                    return 0
                else:
                    return inf
            # op1
            ans1 = A[i + 1] - A[i] + dp(i + 2, can_flip) if i < len(A) - 1 else inf
            # op2
            ans2 = x + dp(i + 1, can_flip + 1)
            # canFlip
            ans3 = dp(i + 1, can_flip - 1) if can_flip else inf
            return min(ans1, ans2, ans3)

        ans = dp(0, 0)
        return ans if ans != inf else -1


"""
"1100011000"
"0101001010"
2
"10110"
"00011"
4
"""
