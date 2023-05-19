""" https://leetcode.com/problems/minimum-cost-to-connect-sticks/
greedily connect the shortest two sticks using heap
"""
from header import *

class Solution:
    def connectSticks(self, A: List[int]) -> int:
        heapify(A)
        ans = 0
        while len(A)>1:
            x = heappop(A)
            y = heappop(A)
            ans += x+y
            heappush(A, (x+y))
        return ans