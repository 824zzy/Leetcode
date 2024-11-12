""" https://leetcode.com/problems/most-beautiful-item-for-each-query/
sort the items and precalculate maximum at each elements, then use binary search to find the correct index for a beautiful item
"""

from header import *


class Solution:
    def maximumBeauty(self, A: List[List[int]], Q: List[int]) -> List[int]:
        A.sort(key=lambda x: (x[0], -x[1]))
        P = [a[0] for a in A]

        ma = 0
        B = [0] + [ma := max(a[1], ma) for a in A]

        ans = []
        for q in Q:
            idx = bisect_right(P, q)
            ans.append(B[idx])
        return ans
