""" https://leetcode.com/problems/remove-interval/
greedily find valid intervals under three cases
time complexity: O(n)
"""
from header import *
class Solution:
    def removeInterval(self, A: List[List[int]], removed: List[int]) -> List[List[int]]:
        ans = []
        ii, jj = removed
        for i, j in A:
            if j<=ii or i>=jj: ans.append([i, j])
            if i<ii<j: ans.append([i, ii])
            if i<=jj<j: ans.append([jj, j])
        return ans
            
            

""" https://leetcode.com/problems/remove-interval/
sweep line template

time complexity: O(nlogn)
"""
class Solution:
    def removeInterval(self, A: List[List[int]], removed: List[int]) -> List[List[int]]:
        SL = []
        for i, j in A:
            SL.append([i, 1])
            SL.append([j, -1])
        SL.append([removed[0], -1])
        SL.append([removed[1], 1])
        SL.sort()
        
        ans = []
        cnt = 0
        l = inf
        for i, x in SL:
            cnt += x
            if cnt==1: l = i
            elif cnt==0 and l!=inf:
                ans.append([l, i])
                l = inf
        return ans
        
        
"""
[1,1,0,1,0,1,1]
[1,0,-1,0,-1,0,1,0]
"""