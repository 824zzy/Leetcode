""" https://leetcode.com/problems/maximum-population-year/
sweep line to find maximum population and its year.
"""
from header import *

class Solution:
    def maximumPopulation(self, A: List[List[int]]) -> int:
        SL = []
        for i, j in A:
            SL.extend([(i, 1), (j, -1)])
        SL.sort()
        
        cnt = 0
        ans = [-inf, inf]
        for y, x in SL:
            cnt += x
            if cnt>ans[0]:
                ans = (cnt, y)
        return ans[1]


# brute force is also available due to the small size of the input
class Solution:
    def maximumPopulation(self, A: List[List[int]]) -> int:
        cnt = Counter()
        for i, j in A:
            for x in range(i, j):
                cnt[x] += 1
        return sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0]