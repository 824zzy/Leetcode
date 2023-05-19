""" https://leetcode.com/problems/maximize-distance-to-closest-person/
two corner cases:
1. A starts with '0': ans = max(ans, j) by set i=-1
2. A ends with '0': ans = max(ans, j-i)
"""
class Solution:
    def maxDistToClosest(self, A: List[int]) -> int:
        i = -1
        ans = 0
                
        for j in range(len(A)):
            if A[j]==1:
                if i<0: ans = max(ans, j)
                else: ans = max(ans, (j-i)//2)
                i = j
        return max(ans, j-i)