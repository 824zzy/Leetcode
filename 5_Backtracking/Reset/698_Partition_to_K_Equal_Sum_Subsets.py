""" L2: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/submissions/
Backtracking + DP
plagiarize from lee: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/108741/Solution-with-Reference
use T as dp array.
"""
class Solution:
    def canPartitionKSubsets(self, A: List[int], k: int) -> bool:
        t = sum(A)//k
        if sum(A)%k: return False
        A.sort(reverse=True)
        
        T = [t] * k
        def dfs(idx):
            if idx==len(A): return True
            for i in range(k):
                if T[i]>=A[idx]:
                    T[i] -= A[idx]
                    if dfs(idx+1): return True
                    T[i] += A[idx]
            return False

        return dfs(0)