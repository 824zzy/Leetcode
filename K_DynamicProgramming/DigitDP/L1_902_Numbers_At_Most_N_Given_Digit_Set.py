""" https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
digit dp with leading zero
"""
from header import *


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = list(map(int, digits))
        high = str(n)
        n = len(high)

        @cache
        def dfs(i, limit_high, is_num):
            if i == n:
                return is_num
            ans = 0
            if not is_num:
                ans += dfs(i + 1, False, False)
            hi = int(high[i]) if limit_high else 9
            for d in range(hi + 1):
                if d in digits:
                    ans += dfs(i + 1, limit_high and hi == d, True)
            return ans
        return dfs(0, True, False)


"""
["1","3","5","7"]
100
["1","4","9"]
1000000000
["7"]
8
["3","4","5","6"]
64
"""
