""" https://leetcode.com/problems/visit-array-positions-to-maximize-score/
"""
from header import *
class Solution:
    def maxScore(self, A: List[int], x: int) -> int:
        o = A[0] if A[0]&1 else -x
        e = A[0] if not A[0]&1 else -x
        for i in range(1, len(A)):
            if A[i]&1:
                o = A[i]+max(o, e-x)
            else:
                e = A[i]+max(e, o-x)
        return max(o, e)
                
            
            
"""
[2,3,6,1,9,2]
5
[2,4,6,8]
3
[38,92,23,30,25,96,6,71,78,77,33,23,71,48,87,77,53,28,6,20,90,83,42,21,64,95,84,29,22,21,33,36,53,51,85,25,80,56,71,69,5,21,4,84,28,16,65,7]
52
"""