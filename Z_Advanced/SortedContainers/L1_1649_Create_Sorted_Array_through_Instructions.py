""" https://leetcode.com/problems/create-sorted-array-through-instructions/
sortedcontainers save your life from dumb trees
"""
from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        sl = SortedList()
        ans = 0
        for i, x in enumerate(A):
            less = sl.bisect_left(x)
            greater = i - sl.bisect_right(x)
            sl.add(x)
            ans += min(less, greater)
        return ans % (10**9 + 7)
