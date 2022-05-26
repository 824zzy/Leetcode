""" https://leetcode.com/problems/132-pattern/
use sortedlist to keep track of the maximal pair of "32" pattern

Time: O(n*nlogn)
"""
# suboptimal solution, better to refer to monotonic decreasing stack solution
from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, A: List[int]) -> bool:
        SL = SortedList()
        last = -inf
        for x in reversed(A):
            if x<last: return True
            # keep track of the maximal pair of "32" pattern
            idx = SL.bisect_left(x)
            if idx>0: last = max(last, SL[idx-1])
                
            SL.add(x)
        return False