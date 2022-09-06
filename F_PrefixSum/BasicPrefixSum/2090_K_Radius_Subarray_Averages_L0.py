""" https://leetcode.com/problems/k-radius-subarray-averages/
use prefix sum array to find range average
"""
class Solution:
    def getAverages(self, A: List[int], k: int) -> List[int]:
        prefix = [0]+list(accumulate(A))
        ans = [-1] * len(A)
        for i in range(k, len(A)-k):
            ans[i] = (prefix[i+k+1]-prefix[i-k])//(2*k+1)
        return ans