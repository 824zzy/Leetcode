""" https://leetcode.com/problems/airplane-seat-assignment-probability/
try 1,2,3,4 and find pattern.
"""


class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        else:
            return 0.5
