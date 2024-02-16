""" https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/
"""
from header import *

class Solution:
    def countMatchingSubarrays(self, A: List[int], p: List[int]) -> int:
        def fn(x, y):
            if y>x: 
                return 1
            elif y==x: 
                return 0
            else:
                return -1
        
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z
            
        A = p+[fn(A[i], A[i+1]) for i in range(len(A)-1)]
        z = z_function(A)
        return sum(x>=len(p) for x in z[len(p):])