""" https://leetcode.com/problems/maximum-strength-of-a-group/
"""
from header import *

# Kadane's algorithm
class Solution:
    def maxStrength(self, A: List[int]) -> int:
        mx, mn = A[0], A[0]
        for x in A[1:]:
            mx, mn = max(mx, x, mx*x, mn*x), min(mn, x, mx*x, mn*x)
        return mx
    
# greedy solution
class Solution:
    def maxStrength(self, A: List[int]) -> int:
        A.sort()
        neg = []
        ans = 0
        for x in A:
            if x<0:
                neg.append(x)
            elif x>0:
                if ans==0: ans = x
                else: ans *= x
        
        neg.sort()
        if len(neg)&1==0:
            for x in neg:
                if ans==0:
                    ans = x
                else:
                    ans *= x
            return ans
        else:
            for i in range(len(neg)-1):
                if ans==0:
                    ans = neg[i]
                else:
                    ans *= neg[i]
        if ans==0: return max(A)
        else: return ans
        
# brute force backtracking due to the small data size
# O(2^n)
class Solution:
    def maxStrength(self, A: List[int]) -> int:
        n = len(A)
        self.ans = -inf
        def dfs(i, s, is_empty):
            if i==len(A):
                if not is_empty:
                    self.ans = max(self.ans, s)
                return
            dfs(i+1, s, is_empty)
            dfs(i+1, s*A[i], False)
        dfs(0, 1, True)
        return self.ans
                
        
    
"""
[3,-1,-5,2,5,-9]
[-4,-5,-4]
[8,6,0,5,-4,-8,-4,9,-1,6,-4,8,-5]
[0,-1]
[-4,-3]
[-9]
"""