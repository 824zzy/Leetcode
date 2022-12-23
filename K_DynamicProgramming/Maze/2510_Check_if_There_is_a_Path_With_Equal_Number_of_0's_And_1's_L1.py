""" https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/solutions/2936796/python-dp/
typical maze dp problem
"""
from header import *

class Solution:
    def isThereAPath(self, G: List[List[int]]) -> bool:
        @cache
        def dp(x, y, cnt):
            if not (0<=x<len(G) and 0<=y<len(G[0])): return False
            if x==len(G)-1 and y==len(G[0])-1:
                if cnt==0:
                    return True
                else:
                    return False
            if G[x][y]==1:
                cnt += 1
            else:
                cnt -= 1            
            return dp(x+1, y, cnt) or dp(x, y+1, cnt)

        if G[0][0]==0:
            return dp(0, 0, -1)
        else:
            return dp(0, 0, 1)