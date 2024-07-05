""" https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
use sweep line/difference array to find the non-overlapped point
"""


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        SL = [0] * 52
        for i, j in ranges:
            SL[i] += 1
            SL[j + 1] -= 1

        cnt = 0
        for i in range(1, 51):
            cnt += SL[i]
            if left <= i <= right and cnt == 0:
                return False
        return True
