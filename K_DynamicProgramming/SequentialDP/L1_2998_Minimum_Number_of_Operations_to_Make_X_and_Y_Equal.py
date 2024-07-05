""" https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/
1. bfs + categorization, time complexity: O(x), at most visit x elements
2. dp + categorization
"""
from header import *


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # case 1 when x<y
        if x < y:
            return y - x
        # case 2 when x>y, the worst case is decrease x to y
        seen = set()
        Q = [x]
        ans = 0
        while Q:
            nxtQ = []
            for x in Q:
                if x == y:
                    return ans
                if x % 11 == 0 and x // 11 not in seen:
                    seen.add(x // 11)
                    nxtQ.append(x // 11)
                if x % 5 == 0 and x // 5 not in seen:
                    seen.add(x // 5)
                    nxtQ.append(x // 5)
                if x - 1 not in seen:
                    seen.add(x - 1)
                    nxtQ.append(x - 1)
                if x + 1 not in seen:
                    seen.add(x + 1)
                    nxtQ.append(x + 1)
            Q = nxtQ
            ans += 1


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def dp(x):
            if x <= y:
                return y - x
            # check distance to 11
            xx, rem = divmod(x, 11)  # low
            ans1 = dp(xx) + rem + 1
            ans2 = dp(xx + 1) + 11 - rem + 1
            # check distance to 5
            xx, rem = divmod(x, 5)  # low
            ans3 = dp(xx) + rem + 1
            ans4 = dp(xx + 1) + 5 - rem + 1
            return min(ans1, ans2, ans3, ans4, x - y)

        return dp(x)


"""
26
1
54
2
25
30
54
3
54
4
54
5
54
6
"""
