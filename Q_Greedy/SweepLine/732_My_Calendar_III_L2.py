""" https://leetcode.com/problems/my-calendar-iii/
1. maintain a sorted list for events
2. apply sweep line to find maximum overlapping event count.
"""
class MyCalendarThree:
    def __init__(self):
        self.SL = []
        

    def book(self, i: int, j: int) -> int:
        bisect.insort(self.SL, (i, 1))
        bisect.insort(self.SL, (j, -1))
        
        cnt = 0
        ans = 0
        for x, i in self.SL:
            cnt += i
            ans = max(ans, cnt)
        return ans