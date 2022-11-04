""" https://leetcode.com/problems/insert-interval/
insert then merge, the same as 56
"""
from header import *

class Solution:
    def insert(self, A: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        A.append(newInterval)
        A.sort()
        
        ans = []
        for x, y in sorted(A): 
            if not ans or ans[-1][1] < x: ans.append([x, y]) # new interval 
            else: ans[-1][1] = max(ans[-1][1], y) # overlapped 
        return ans