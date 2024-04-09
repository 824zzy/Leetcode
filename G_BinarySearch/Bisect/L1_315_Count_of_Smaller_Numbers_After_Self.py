""" https://leetcode.com/problems/count-of-smaller-xbers-after-self/
bisect.insort to build binary search tree
bisect.bisect_left to find position to insert(how many nodes smaller than itself)

Notet that SortedList is way much faster
"""
from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, A):
        SList, ans = SortedList(), []
        for x in A[::-1]:
            idx = SortedList.bisect_left(SList, x)
            ans.append(idx)
            SList.add(x)
        return ans[::-1]
