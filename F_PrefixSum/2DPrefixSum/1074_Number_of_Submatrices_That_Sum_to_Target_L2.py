""" https://leetcode.com/problems/number-of-submatrices-that-sum-to-t/submissions/
2D prefix sum + subarray sum equals to t(problem 560)
"""
class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], t: int) -> int:
        # 2D prefix sum
        m, n = len(A), len(A[0])
        ans = 0 
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m): 
            for j in range(n): 
                prefix[i+1][j+1] = A[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
        # subarray sum equals to t
        for i in range(m):
            for ii in range(i+1):
                freq = Counter()
                for j in range(n+1):
                    diff = prefix[i+1][j]-prefix[ii][j]
                    ans += freq[diff-t]
                    freq[diff] += 1
        return ans 