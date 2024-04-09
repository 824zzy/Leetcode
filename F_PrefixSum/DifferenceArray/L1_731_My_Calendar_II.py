""" https://leetcode.com/problems/my-calendar-ii/
create sweep line on the fly and check if the overlapping is less than 3
"""


class MyCalendarTwo:
    def __init__(self):
        self.A = []

    def book(self, l: int, r: int) -> bool:
        tmp = self.A.copy()
        bisect.insort(self.A, (l, 1))
        bisect.insort(self.A, (r, -1))

        cnt = 0
        for x, i in self.A:
            cnt += i
            if cnt == 3:
                self.A = tmp
                return False
        return True
