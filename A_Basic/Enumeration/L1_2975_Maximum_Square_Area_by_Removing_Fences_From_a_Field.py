""" https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
1. enumerate possible length of hFences and vFences
2. find the maximum of intersection
"""
from header import *

class Solution:
    def maximizeSquareArea(self, m: int, n: int, H: List[int], V: List[int]) -> int:
        H.sort()
        V.sort()
        MOD = 10**9+7
        def find_cand(A):
            seen = set()
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    seen.add(A[j]-A[i])
            return seen
        
        H, V = [1]+H+[m], [1]+V+[n]
        A = find_cand(H)
        B = find_cand(V)
        mx = max(A&B, default=0)
        return pow(mx, 2, MOD) if mx else -1
        
"""
4
3
[2,3]
[2]
6
7
[2]
[4]
3
9
[2]
[8,6,5,4]
"""