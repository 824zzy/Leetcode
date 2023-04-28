""" https://leetcode.com/problems/find-maximal-uncovered-ranges/
Sort the ranges and iterate over intervals, if start of new interval bigger than the rightmost of previous intervals, there is a hole, so put that interval into output.
"""
from header import *

class Solution:
    def findMaximalUncoveredRanges(self, n: int, A: List[List[int]]) -> List[List[int]]:
        A.sort()
        ans = []
        start = 0
        for i, j in A:
            if start<i:
                ans.append([start, i-1])
                start = j+1
            else:
                start = max(start, j+1)
            
        if start<n: ans.append([start, n-1])
        return ans
    
"""
10
[[3,5],[7,8]]
3
[[0,2]]
7
[[2,4],[0,3]]
"""