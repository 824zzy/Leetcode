""" https://leetcode.com/problems/minimum-time-to-complete-all-tasks/
1. Sort the tasks in ascending order of end time
2. Greedily run the task as late as possible so that later tasks can run simultaneously.

Time complexity: O(2000*n)
"""
from header import *


class Solution:
    def findMinimumTime(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: x[1])
        run = [0] * 2001
        for s, e, d in A:
            d -= sum(run[s : e + 1])
            if d > 0:
                for i in range(e, s - 1, -1):
                    if run[i]:
                        continue
                    run[i] = True
                    d -= 1
                    if d == 0:
                        break
        return sum(run)


"""
[[2,3,1],[4,5,1],[1,5,2]]
[[1,3,2],[2,5,3],[5,6,2]]
[[14,20,5],[2,18,7],[6,14,1],[3,16,3]]
[[10,16,3],[10,20,5],[1,12,4],[8,11,2]]
"""
