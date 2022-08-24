""" https://leetcode.com/problems/jump-game-vii/

"""
from header import *

class Solution:
    def canReach(self, A: str, mn: int, mx: int) -> bool:
        if A[-1]!='0': return False
        
        diff = [0]*(len(A)+1)
        cnt = 0
        diff[mn], diff[mx+1] = 1, -1
        for i, x in enumerate(A):
            cnt += diff[i]
            if x=='1' or cnt==0: continue
            diff[min(i+mn, len(A))] += 1
            diff[min(i+mx+1, len(A))] -= 1
        return cnt>0
            

# Note that DP will TLE due to time complexity is O(n^2)
class Solution:
    def canReach(self, A: str, mn: int, mx: int) -> bool:
        @cache
        def dp(i):
            if i==len(A)-1: return True
            ans = False
            for j in range(i+mn, min(i+mx+1, len(A))):
                if A[j]=='0':
                    ans |= dp(j)
            return ans
        
        return dp(0)