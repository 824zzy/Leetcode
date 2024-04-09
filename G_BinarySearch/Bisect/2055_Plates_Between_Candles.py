""" L2: https://leetcode.com/problems/plates-between-candles/
Use prefix sum to calculate candles numbers in interval,
find candles by binary search.
"""
# prefix sum + binary search


class Solution:
    def platesBetweenCandles(
            self, s: str, queries: List[List[int]]) -> List[int]:
        P = [0]
        C = []
        for i, c in enumerate(s):
            if c == '|':
                C.append(i)
                P.append(P[-1])
            else:
                P.append(P[-1] + 1)
        ans = []
        for i, j in queries:
            l = bisect_left(C, i)
            r = bisect_right(C, j) - 1
            if r >= 0 and l < len(C) and l <= r:
                ans.append(P[C[r] + 1] - P[C[l]])
            else:
                ans.append(0)
        return ans
