""" https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/
digit dp with leading zero and low/high limit

(pre*10+d)%k to avoid MLE
"""
from header import *


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        high = str(high)
        n = len(high)
        low = str(low).zfill(n)

        @cache
        def dfs(i, limit_low, limit_high, is_num, cnt, pre):
            if i == n:
                if is_num and cnt == 0 and pre % k == 0:
                    return 1
                else:
                    return 0
            ans = 0
            if not is_num and low[i] == '0':
                ans += dfs(i + 1, True, False, False, 0, 0)

            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            d0 = 0 if is_num else 1
            for d in range(max(lo, d0), hi + 1):
                ans += dfs(i + 1,
                           limit_low and d == lo,
                           limit_high and d == hi,
                           True,
                           cnt + (1 if d % 2 else -1),
                           (pre * 10 + d) % k)
            return ans

        return dfs(0, True, True, False, 0, 0)


"""
10
20
3
1
10
1
5
5
2
349863935
772153463
11
"""
