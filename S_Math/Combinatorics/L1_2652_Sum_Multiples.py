""" https://leetcode.com/problems/sum-multiples/
1. The sum of all valid integers of factor x:
    sm = (1+2+...+n)*x
2. The sum of all valid integers: sm = sm1 + sm2 + sm3 - sm12 - sm23 - sm13 + sm123
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def fn(x):
            f = n // x
            return f * (f + 1) // 2 * x

        return fn(3) + fn(5) + fn(7) - fn(15) - fn(35) - fn(21) + fn(105)


# brute force also works due to small n


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                ans += i
        return ans
