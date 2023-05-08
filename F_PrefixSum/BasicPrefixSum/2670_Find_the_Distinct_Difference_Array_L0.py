""" https://leetcode.com/problems/find-the-distinct-difference-array/
simulation by prefix sum
"""
from header import *

class Solution:
    def distinctDifferenceArray(self, A: List[int]) -> List[int]:
        pre = [0]*(len(A)+1)
        seen = set()
        for i, x in enumerate(A):
            seen.add(x)
            pre[i] = len(seen)
        
        suf = [0]*(len(A)+1)
        seen = set()
        for i, x in enumerate(reversed(A)):
            seen.add(x)
            suf[~i-1] = len(seen)
        
        ans = []
        for i in range(len(A)):
            ans.append(pre[i]-suf[i+1])
        return ans