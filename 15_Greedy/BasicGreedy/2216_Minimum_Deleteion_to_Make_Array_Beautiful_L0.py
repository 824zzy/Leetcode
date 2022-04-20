""" https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
1. use shift to indicate the index parity
2. check array length parity at the end
"""
class Solution:
    def minDeletion(self, A: List[int]) -> int:
        ans = 0
        shift = 0
        for j in range(len(A)-1):
            if A[j]==A[j+1] and (j+shift)%2==0:
                ans += 1
                shift += 1
        
        if (len(A)-ans)%2==0: return ans
        else: return ans+1