""" https://leetcode.com/problems/maximum-matrix-sum/
Greedy by 3 rules:
1. If we have a zero anywhere we can use it to flip all negatives into positives.
2. If we have even number of negatives, we can turn all negatives into positives.
3. Otherwise, we turn the smallest absolute value into a negative, and everything else - into positives.
"""
class Solution:
    def maxMatrixSum(self, A: List[List[int]]) -> int:
        negs = []
        sm = 0
        zeros = 0
        mn = inf
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==0: zeros += 1
                elif A[i][j]<0: negs.append(A[i][j])
                sm += abs(A[i][j])
                mn = min(A[i][j], mn, key=abs)
        
        if not max(len(negs)-zeros, 0)&1:
            return sm
        else:
            return sm-2*mn
        
"""
[[1,-1],[-1,1]]
[[1,2,3],[-1,-2,-3],[1,2,3]]
[[-1,0,-1],[-2,1,3],[3,2,2]]
[[-3,0,0],[0,0,0],[0,3,2]]
[[2,9,3],[5,4,-4],[1,7,1]]
"""