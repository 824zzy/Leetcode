""" https://leetcode.com/problems/course-schedule-iii/
greedy sort + priority queue
"""
from header import *


class Solution:
    def scheduleCourse(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: x[1])
        time = 0
        pq = []
        for x, y in A:
            time += x
            heappush(pq, -x)
            while time > y:
                time += heappop(pq)
        return len(pq)
