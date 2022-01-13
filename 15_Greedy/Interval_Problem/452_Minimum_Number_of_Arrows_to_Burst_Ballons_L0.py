""" https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/
the same as 435: use ma to greedily keep track of maximum end value
"""
class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: x[1])        
        ans = 0
        ma = -inf
        for i, j in A:
            if ma<i:
                ma = j
                ans += 1
        return ans