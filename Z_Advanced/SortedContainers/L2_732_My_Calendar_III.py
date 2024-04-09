""" https://leetcode.com/problems/my-calendar-iii/
learn from: https://leetcode.com/problems/my-calendar-iii/discuss/1646167/Python-O(n-2)-using-SortedDict

a sweep line algorithm implemented by sorted containers
"""
from sortedcontainers import SortedList
from header import *


class MyCalendarThree:
    def __init__(self):
        self.cnt = SortedDict()

    def book(self, s: int, e: int) -> int:
        # Insert current event into the SortedDict
        self.cnt[s] = self.cnt.get(s, 0) + 1
        self.cnt[e] = self.cnt.get(e, 0) - 1
        # Return maximum overlap count
        return max(accumulate(self.cnt.values()))


# SortedList implementation


class MyCalendarThree:
    def __init__(self):
        self.SL = SortedList()

    def book(self, i: int, j: int) -> int:
        self.SL.add([i, 1])
        self.SL.add([j, -1])

        cnt = 0
        ans = 0
        for x, i in self.SL:
            cnt += i
            ans = max(ans, cnt)
        return ans


# use binary search to maintain a sorted list
class MyCalendarThree:
    def __init__(self):
        self.A = []

    def book(self, i: int, j: int) -> int:
        insort(self.A, [i, 1])
        insort(self.A, [j, -1])

        cnt = 0
        ans = 0
        for i, x in self.A:
            cnt += x
            ans = max(ans, cnt)
        return ans
