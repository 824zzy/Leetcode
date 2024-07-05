""" https://leetcode.com/problems/count-of-integers/
digit dp with leading zero and low/high limit
"""
from header import *


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7
        high = str(num2)
        n = len(high)
        low = str(num1).zfill(n)
        # print(low, high)

        @cache
        def dfs(i, limit_low, limit_high, is_num, sm):
            if i == n:
                if min_sum <= sm <= max_sum:
                    return 1
                else:
                    return 0
            ans = 0
            if not is_num and low[i] == "0":
                ans += dfs(i + 1, True, False, False, 0)
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            d0 = 0 if is_num else 1
            for d in range(max(lo, d0), hi + 1):
                ans += dfs(
                    i + 1, limit_low and lo == d, limit_high and hi == d, True, sm + d
                )
            return ans % MOD

        return dfs(0, True, True, False, 0) % MOD


"""
"1"
"12"
1
8
"1"
"5"
1
5
"4179205230"
"7748704426"
8
46
"4859473643"
"30159981595"
58
59
"""

"""
"1"
"12"
1
8
"1"
"5"
1
5
"1000000007"
"2000000014"
1
400
"""
