""" https://leetcode.com/problems/my-calendar-iii/
learn from: https://leetcode.com/problems/my-calendar-iii/discuss/1646167/Python-O(n-2)-using-SortedDict
"""
from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.cnt = SortedDict()

    def book(self, s: int, e: int) -> int:
        # Insert current event into the SortedDict
        self.cnt[s] = self.cnt.get(s, 0)+1
        self.cnt[e] = self.cnt.get(e, 0)-1
        # Return maximum overlap count
        return max(accumulate(self.cnt.values()))