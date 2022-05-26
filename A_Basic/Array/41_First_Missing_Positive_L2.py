""" https://leetcode.com/problems/first-missing-positive/
"""
# Time Complexity: O(N), Space Complexity: O(1)
class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        # mark outliers
        for i in range(len(A)):
            if A[i]<=0 or A[i]>len(A): A[i] = len(A)+1
        
        # use abs() to avoid index out of range
        for a in A:
            a = abs(a)
            if a<=len(A) and A[a-1]>=0: A[a-1] *= -1
        
        for i, a in enumerate(A):
            if a>0: return i+1
        
        return len(A)+1