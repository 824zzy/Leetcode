""" https://leetcode.com/problems/get-the-maximum-score/
use two pointers to greedily find the maximum score
"""
class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        i, j, sumi, sumj, ans = 0, 0, 0, 0, 0
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                sumi += A[i]
                i += 1
            elif A[i]>B[j]:
                sumj += B[j]
                j += 1
            else:
                ans += max(sumi, sumj)+A[i]
                sumi, sumj = 0, 0
                i, j = i+1, j+1
        ans += max(sumi+sum(A[i:]), sumj+sum(B[j:]))
        return ans % (10**9+7)