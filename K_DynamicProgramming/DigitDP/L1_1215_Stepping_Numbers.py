""" https://leetcode.com/problems/stepping-numbers/
digit dp with lower and upper bound and leading zero

the same as 2801. Since the data range is small, we can use dfs instead of digit dp.
"""
from header import *


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        self.ans = [0] if low == 0 else []
        high = str(high)
        n = len(high)
        low = str(low).zfill(n)

        def dfs(i, limit_low, limit_high, is_num, x):
            if i == n:
                if is_num:
                    self.ans.append(int(x))
                return
            if not is_num and low[i] == '0':
                dfs(i + 1, True, False, False, "")
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            d0 = 0 if is_num else 1
            for d in range(max(d0, lo), hi + 1):
                if x == '' or abs(d - int(x[-1])) == 1:
                    dfs(i + 1, limit_low and d == lo,
                        limit_high and d == hi, True, x + str(d))
        dfs(0, True, True, False, "")
        return self.ans
